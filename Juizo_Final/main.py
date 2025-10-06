import customtkinter as ctk
from PIL import Image
import variaveis as var
from janelas import *

class JogoDaVida(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1350x800')
        self.title('Jogo da Vida')
        self.resizable(False,False)

        #questão atual --> no começo do jogo
        self.questao_atual = '1'    

        #Tela de fundo - label    
        background_img = ctk.CTkImage(Image.open(var.caminho_bg_img),size=(1350,800))
        background_lbl = ctk.CTkLabel(self, text='', image=background_img)
        background_lbl.place(x=0, y=0)

        #Display do texto da questão
        self.questao_label = Label(self,bg='black',font=('consolas',28),text='') 

        #Criação da imagem do personagem
        imagem_personagem = ctk.CTkImage(Image.open(var.caminho_person_img),size=(200,300))
        imagem_label = ctk.CTkLabel(self,image=imagem_personagem,text='')
        imagem_label.pack(pady=60)

        #Frame dos butões de pergunta / Utiliza metódo de layout diferente (grid)
        self.botao_frame = BotaoFrame(self,larg=1000,alt=300)

        self.botao_lista = []

        self.update_interface()
        
    def update_interface(self):
        '''Atualiza a interface com os textos das perguntas e das repostas a partir da questão atual'''
        print(self.questao_atual)

        #se não tiver mais questões o jogo acaba
        if self.questao_atual is None:
            print('Acabou')
            return

        #dados referentes a questão atual
        self.dados_questao = var.dados['perguntas'][self.questao_atual]

        #Definir texto da questao
        self.questao_label.configure(text=self.dados_questao['texto'])

        #Criar os botoes das respostas
        respostas = list(self.dados_questao['respostas'].keys())
        self.criar_botoes(respostas)   #resposta é uma lista com os textos das repostas e vai ser passada como uma chave porque cada texto é a chave do dicionario de respostas.

        #Definir texto dos botões
        for i, texto_repostas in enumerate(respostas):
            self.botao_lista[i].configure(text=texto_repostas)


    def criar_botoes(self,chave):
        '''Criar lista com os botões de reposta para facilitar o acesso futuro'''
        #Apaga botões antigos se tiver
        for btn in self.botao_lista:
            btn.destroy()

        self.botao_lista = []
        for i in range(3):  #cria os três botoes
            btn = Botao(self.botao_frame, fg='green', font=('consolas', 20), text='', func=self.clicar_botao, col=i, chave=chave[i]) #ao passar o texto como chave, a função clicar_botao terá acesso aos atributos referentes ao botao clicado.
            self.botao_lista.append(btn)

    def clicar_botao(self,chave):
        #chave corresponde ao texto da resposta 
        self.questao_atual = self.dados_questao['respostas'][chave]['prox_q']

        self.update_interface()
        
if __name__ == '__main__':
    jogo = JogoDaVida()
    jogo.mainloop()