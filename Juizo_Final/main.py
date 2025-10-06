import customtkinter as ctk
from PIL import Image, ImageTk
import variaveis as var
from janelas import *

class JogoDaVida(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title('Jogo da Vida')
        self.resizable(False,False)

        #Questão atual --> no começo do jogo
        self.questao_atual = '1'    

        #Imagem background 
        self.background_img = Image.open(var.caminho_bg_img).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.background_photo = ImageTk.PhotoImage(self.background_img)

        #Cria canvas 
        self.canvas = ctk.CTkCanvas(self, width=var.WIN_LARGURA, height=var.WIN_ALTURA, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0,0,image=self.background_photo,anchor='nw')

        #Criação da imagem do personagem
        self.personagem_img = Image.open(var.caminho_person_img).resize((150,200))
        self.personagem_photo = ImageTk.PhotoImage(self.personagem_img)
        self.canvas.create_image(var.WIN_LARGURA/2, 340, image=self.personagem_photo)

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
            print('Acabou')
            return

        #Dados referentes a questão atual
        self.dados_questao = var.dados['perguntas'][self.questao_atual]

        #Definir texto da questao
        self.canvas.itemconfig('texto_questao', text=self.dados_questao['texto'])

        #Armazena os textos das respostas
        respostas = list(self.dados_questao['respostas'].keys())  #resposta é uma lista com os textos das repostas e vai ser passada como uma chave porque cada texto é a chave do dicionario de respostas.

        self.criar_botao_img(respostas)  #Chama a função que cria os botões
        for i in range(3):    
            #Passa o texto corresponde ao botão para a função clicar_botao e cria um evento de clicar para cada botao de acordo com sua tag
            self.canvas.tag_bind(f"botao{i}", "<Button-1>", lambda event: self.clicar_botao(respostas[i]))


    def criar_botao_img(self,chave):
        ''' Cria a imagem e o texto dos botões no canvas a partir das funções create_image/create_text'''

        mult_x_coord = [1,3,5]
        for i, mult in enumerate(mult_x_coord):
            #cria e posiciona cada imagem e texto do botao e associa cada um a uma tag correspondente
            self.canvas.create_image(var.WIN_LARGURA/6*mult,630, image=self.botao_photo,tags=f'botao{i}')
            self.canvas.create_text(var.WIN_LARGURA/6*mult,630,text=chave[i],fill='white',font=('consolas',15),tags=f'botao{i}')


    def clicar_botao(self,chave):
        '''Atualiza a questão atual e deleta os botões antigos'''
        #chave corresponde ao texto da resposta 
        self.questao_atual = self.dados_questao['respostas'][chave]['prox_q']

        #deleta os botões
        for i in range(3):
            self.canvas.delete(f'botao{i}')

        self.update_interface()
        
if __name__ == '__main__':
    jogo = JogoDaVida()
    jogo.mainloop()

