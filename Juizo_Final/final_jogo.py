import customtkinter as ctk
from PIL import Image, ImageTk
import config as var
from canvas import Canvas
from pygame import mixer

class FinalJogo(ctk.CTkToplevel):
    def __init__(self,master,karma):
        super().__init__(master)
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title(f'Juizo Final')
        self.resizable(False,False)
        self.karma = karma
        self.frase_final = {'purgatorio':'Você plantou, \nagora colha as suas \nconsequências, bem vindo \nao seu novo lar.','inferno':'A tentação não \nfoi minha criação…\n foi sua desculpa.','paraiso':'Até na escuridão,\n você encontrou \num motivo para agir\n com luz.'}

        #Som do texto sendo escrito
        mixer.init()
        self.escrever_som = mixer.Sound(var.caminho_maquina_escrever_som)
        self.escrever_som.set_volume(0.6)

        #Cria canvas 
        self.canvas = Canvas(self)

        #Imagem Inferno
        self.canvas.importar_img_final(caminho=var.caminho_inferno_bg,tags='inferno')

        #Imagem Paraiso
        self.canvas.importar_img_final(caminho=var.caminho_paraiso_bg,tags='paraiso')

        #Imagem Purgatorio
        self.canvas.importar_img_final(caminho=var.caminho_purgatorio_bg,tags='purgatorio')

        #Imagem Morte (teste)
        self.morte_img = Image.open('imagens/demonio2.png').resize((650,650))
        self.morte_photo = ImageTk.PhotoImage(self.morte_img)

        self.canvas.create_image(0,0,image='',anchor='nw',tags='bg')

        #Imagem Balao 
        imagem_botao = Image.open(var.caminho_botao_img).resize((820,800))
        self.photo_botao = ImageTk.PhotoImage(imagem_botao)
        self.juizo_final()
        
    def juizo_final(self):
        '''Define o background a partir do karma, chama a função do efeito ao escrever e inicializa o som do efeito'''
        if self.karma <= var.KARMA_BOM:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['inferno'])
            self.efeito_escrever(self.frase_final['inferno'])
            self.escrever_som.play(loops=-1)

        elif self.karma >= var.KARMA_RUIM:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['paraiso'])
            self.efeito_escrever(self.frase_final['paraiso'])
            self.escrever_som.play(loops=-1)
        else:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['purgatorio'])
            self.canvas.create_image((600,500),image=self.morte_photo) #(teste)
            self.efeito_escrever(self.frase_final['purgatorio'])
            self.escrever_som.play(loops=-1)


        self.canvas.create_image(1000,250,image=self.photo_botao)

        self.canvas.create_text(1010,240,text='',font=('Black Goth',30),tags='texto',fill='white')


    def efeito_escrever(self,texto,index=0):
        '''Dispõe o efeito de máquina de escrever e finaliza o som quando o efeito acaba'''
        if index <= len(texto):
            self.canvas.itemconfig('texto', text=texto[:index])
            self.canvas.after(100,lambda:self.efeito_escrever(texto,index+1))
        else:
            self.escrever_som.stop()
