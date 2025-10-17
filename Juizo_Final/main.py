import customtkinter as ctk
from PIL import Image, ImageTk
import variaveis as var
from janelas import *



class Init_Jogo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title('Jogo da Vida')
        self.resizable(False,False)

        #Cria canvas 
        self.canvas = ctk.CTkCanvas(self, width=var.WIN_LARGURA, height=var.WIN_ALTURA, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        #Imagem background 
        self.background_img = Image.open(var.caminho_main_img).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.canvas.create_image(0,0,image=self.background_photo,anchor='nw')

        #Edificio- trabalho
        self.trabalho_img = Image.open(var.caminho_trabalho_img).resize((200,250))
        self.trabalho_photo = ImageTk.PhotoImage(self.trabalho_img)
        self.canvas.create_image(190, 520, image=self.trabalho_photo, tags='trabalho')
        self.canvas.tag_bind(f"trabalho", "<Button-1>", lambda event: self.chamar_fase('trabalho'))

        #Edificio- escola
        self.escola_img = Image.open(var.caminho_escola_img).resize((200,250))
        self.escola_photo = ImageTk.PhotoImage(self.escola_img)
        self.canvas.create_image(490, 150, image=self.escola_photo, tags='escola')
        self.canvas.tag_bind(f"escola", "<Button-1>", lambda event: self.chamar_fase('escola'))

        #Edificio- familia
        self.familia_img = Image.open(var.caminho_familia_img).resize((200,250))
        self.familia_photo = ImageTk.PhotoImage(self.familia_img)
        self.canvas.create_image(700, 520, image=self.familia_photo, tags='familia')
        self.canvas.tag_bind(f"familia", "<Button-1>", lambda event: self.chamar_fase('familia'))

        #Edificio- faculdade
        self.faculdade_img = Image.open(var.caminho_faculdade_img).resize((200,250))
        self.faculdade_photo = ImageTk.PhotoImage(self.faculdade_img)
        self.canvas.create_image(1010, 130, image=self.faculdade_photo, tags='faculdade')
        self.canvas.tag_bind(f"faculdade", "<Button-1>", lambda event: self.chamar_fase('faculdade'))

        self.jogo_fase = None 

    def chamar_fase(self,fase):
        if self.jogo_fase is not None:
            self.jogo_fase.destroy()
        self.jogo_fase = JogoDaVida(self,fase)

class JogoDaVida(ctk.CTkToplevel):
    def __init__(self,master,fase):
        super().__init__(master)
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title(f'{fase.capitalize()}')
        self.resizable(False,False)
        self.fase_atual = fase
        var.pegar_imagem(fase)

        #Questão atual --> no começo do jogo
        self.questao_atual = '1'    

        #Cria canvas 
        self.canvas = ctk.CTkCanvas(self, width=var.WIN_LARGURA, height=var.WIN_ALTURA, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        #Imagem background 
        self.background_img = Image.open(var.caminho_bg_img).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.canvas.create_image(0,0,image=self.background_photo,anchor='nw')

        #Imagem do balao de pergunta
        self.balao_img = Image.open(var.caminho_balao_perg).resize((1500,400))
        self.balao_photo = ImageTk.PhotoImage(self.balao_img)
        self.canvas.create_image(var.WIN_LARGURA/2, 90, image=self.balao_photo)

        #Display do texto da questão
        self.canvas.create_text(var.WIN_LARGURA/2,55,font=('consolas',20),text='',tags='texto_questao') 

        #Imagem do botao
        self.botao_img = Image.open(var.caminho_botao_img).resize((470,230))
        self.botao_photo = ImageTk.PhotoImage(self.botao_img)

        self.update_interface()
        
    def update_interface(self):
        '''Atualiza a interface com os textos das perguntas e das repostas a partir da questão atual'''

        #Se não tiver mais questões o jogo acaba
        if self.questao_atual is None:
            self.destroy()
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
        self.canvas.tag_bind(f"botao{0}", "<Button-1>", lambda event: self.clicar_botao(chave[0]))  
        self.canvas.tag_bind(f"botao{1}", "<Button-1>", lambda event: self.clicar_botao(chave[1]))
        self.canvas.tag_bind(f"botao{2}", "<Button-1>", lambda event: self.clicar_botao(chave[2]))

            
    def clicar_botao(self,chave):
        '''Atualiza a questão atual e deleta os botões antigos'''
        #chave corresponde ao texto da resposta 
        self.questao_atual = self.dados_questao['respostas'][chave]['prox_q']

        #deleta os botões
        for i in range(3):
            self.canvas.delete(f'botao{i}')

        self.update_interface()
        
if __name__ == '__main__':
    jogo = Init_Jogo()
    jogo.mainloop()

