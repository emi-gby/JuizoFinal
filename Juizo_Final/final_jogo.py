import customtkinter as ctk
from PIL import Image, ImageTk
import caminhos as var
from canvas import Canvas


class FinalJogo(ctk.CTkToplevel):
    def __init__(self,master,karma):
        super().__init__(master)
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title(f'Juizo Final')
        self.resizable(False,False)
        self.karma = karma

        #Cria canvas 
        self.canvas = Canvas(self)

        #Imagem Inferno
        self.canvas.importar_img_final(caminho=var.caminho_inferno_bg,tags='inferno')

        #Imagem Paraiso
        self.canvas.importar_img_final(caminho=var.caminho_paraiso_bg,tags='paraiso')

        #Imagem Purgatorio
        self.canvas.importar_img_final(caminho=var.caminho_purgatorio_bg,tags='purgatorio')

        #Imagem Morte (teste)
        self.morte_img = Image.open('imagens/morte.png').resize((650,650))
        self.morte_photo = ImageTk.PhotoImage(self.morte_img)

        self.canvas.create_image(0,0,image='',anchor='nw',tags='bg')

        self.canvas.create_text(700,400,text=f'karma total : {self.karma}',font=('arial',75))

        self.juizo_final()
        
    def juizo_final(self):
        if self.karma <= -20:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['inferno'])
        elif self.karma >= 35:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['paraiso'])
        else:
            self.canvas.itemconfig('bg',image=self.canvas.final_photos_dict['purgatorio'])
            self.canvas.create_image((600,500),image=self.morte_photo) #(teste)
