import customtkinter as ctk
from PIL import Image, ImageTk
import caminhos as var
from canvas import Canvas
from pygame import mixer
class JogoDaVida(ctk.CTkToplevel):
    def __init__(self,master,fase):
        super().__init__(master)
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title(f'{fase.capitalize()}')
        self.resizable(False,False)
        self.fase_atual = fase
        self.karma = 0
        self.master = master
        var.pegar_imagem(fase)

        mixer.init()

        #Questão atual --> no começo do jogo
        self.questao_atual = '1'    

        #Cria canvas 
        self.canvas = Canvas(self)

        #Imagem background 
        self.canvas.criar_imagem(caminho=var.caminho_bg_img,tamanho=(var.WIN_LARGURA,var.WIN_ALTURA),x=0,y=0,tags=None,anchor='nw')
    
        #Imagem do balao de pergunta
        self.canvas.criar_imagem(caminho=var.caminho_balao_perg,tamanho=(1500,400),x=var.WIN_LARGURA/2,y=90,tags=None,anchor='center')

        #Display do texto da questão
        self.canvas.create_text(var.WIN_LARGURA/2,55,font=('consolas',20),text='',tags='texto_questao') 

        #Imagem do botao
        self.botao_img = Image.open(var.caminho_botao_img).resize((760,570))
        self.botao_photo = ImageTk.PhotoImage(self.botao_img)

        #Imagem Karma
        self.karma_img = Image.open(var.caminho_karma_img).resize((70,70))
        self.karma_photo = ImageTk.PhotoImage(self.karma_img)

        #Imagem Anjo
        self.anjo_img = Image.open(var.caminho_anjo_img).resize((80,80))
        self.anjo_photo = ImageTk.PhotoImage(self.anjo_img)

        #Imagem Demonio
        self.demonio_img = Image.open(var.caminho_demonio_img).resize((80,80))
        self.demonio_photo = ImageTk.PhotoImage(self.demonio_img)

        #tira o bind da fase já jogada
        self.master.canvas.tag_unbind(f'{self.fase_atual}', "<Button-1>")

        self.update_interface()
        
    def update_interface(self):
        '''Atualiza a interface com os textos das perguntas e das repostas a partir da questão atual'''

        #Se não tiver mais questões o jogo acaba
        if self.questao_atual is None:
            self.destroy()
            #passa o valor relativo do karma da respectiva fase para a função da classe inicial
            self.master.calcular_karma(self.karma, self.fase_atual)
            return 

        #Dados referentes a questão atual
        self.dados_questao = var.dados['perguntas'][self.fase_atual][self.questao_atual]

        #Definir texto da questao
        self.canvas.itemconfig('texto_questao', text=self.dados_questao['texto'])

        #Armazena os textos das respostas
        respostas = list(self.dados_questao['respostas'].keys())  #resposta é uma lista com os textos das repostas e vai ser passada como uma chave porque cada texto é a chave do dicionario de respostas.

        self.criar_botao_img(respostas)  #Chama a função que cria os botões


    def criar_botao_img(self,chave):
        ''' Cria a imagem e o texto dos botões no canvas a partir das funções create_image/create_text'''

        mult_x_coord = [1,3,5]
        for i, mult in enumerate(mult_x_coord):
            #cria e posiciona cada imagem e texto do botao e associa cada um a uma tag correspondente
            self.canvas.create_image(var.WIN_LARGURA/6*mult,630, image=self.botao_photo,tags=f'botao{i}')
            self.canvas.create_text(var.WIN_LARGURA/6*mult,630,text=chave[i],fill='white',font=('consolas',15),tags=f'botao{i}')
            
        #Passa o texto corresponde ao botão para a função clicar_botao e cria um evento de clicar para cada botao de acordo com sua tag
        self.canvas.tag_bind(f"botao{0}", "<Button-1>", lambda _: self.clicar_botao(chave[0])) 
        self.canvas.tag_bind(f"botao{1}", "<Button-1>", lambda _: self.clicar_botao(chave[1]))
        self.canvas.tag_bind(f"botao{2}", "<Button-1>", lambda _: self.clicar_botao(chave[2]))

            
    def clicar_botao(self,chave):
        '''Disabilita os botões e define um tempo de espera para a próxima questão'''

        #som do clique do botão
        mixer.Sound(var.caminho_botao_clique_som).play()

        for i in range(3):
            self.canvas.tag_unbind(f'botao{i}', "<Button-1>")

        # mostrar karma na tela
        self.mostrar_karma(self.dados_questao['respostas'][chave]['karma'])

        self.after(1000,lambda: self.processar_clique(chave))

    def mostrar_karma(self, valor):
        '''Animação da mudança e cálculo do karma'''

        self.karma += valor  #adiciona ao karma total o valor
        #adiciona sinal de mais no inicial se valor for maior ou igual a 0
        text = f"+{valor}" if valor >= 0 else f"{valor}"
        #utiliza imagens diferentes de acordo com o valor
        imagem_karma = self.anjo_photo if valor > 0 else self.karma_photo if valor == 0 else self.demonio_photo

        #cria texto e imagens referentes ao karma
        self.canvas.create_text(
            1100, 250, text=text,
            font=('consolas', 70, 'bold'),
            fill="#66DF66" if valor > 0 else "#7A6E6E" if valor == 0 else "#CA2323",
            anchor='center',tags='karma'
        )
        self.canvas.create_image(1195,250,image=imagem_karma, tags='karma')

        # parametros para a animação
        duracao = 1000  # duração total da animação
        passos = 30  #quantas 'frames' ocorrem na animação | relacionando com fps- 30 frames(passos)/ 1s(duração)
        tempo_passo = duracao // passos #tempo em que cada passo ocorre
        delta_y = -28 / passos  # movimento vertical da frame a cada passo (movimento total = 28px)

        def animacao(passo=0):
            if passo < passos:
                # move a imagem e o texto para cima
                self.canvas.move('karma', 0, delta_y)

                # chama a função animacao após passar o tempo do passo
                self.after(tempo_passo, lambda: animacao(passo + 1))
            else:
                # animação acaba - deleta o texto e a imagem
                self.canvas.delete('karma')

        animacao()


    def processar_clique(self,chave):
        '''Atualiza a questão atual e deleta os botões antigos'''
        #chave corresponde ao texto da resposta 
        self.questao_atual = self.dados_questao['respostas'][chave]['prox_q']

        #deleta os botões
        for i in range(3):
            self.canvas.delete(f'botao{i}')

        self.update_interface()
        