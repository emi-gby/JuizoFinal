import customtkinter as ctk
from PIL import Image, ImageTk
import caminhos as var


class FinalJogo(ctk.CTkToplevel):
    def __init__(self,master,karma):
        super().__init__(master)
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title(f'Juizo Final')
        self.resizable(False,False)
        self.karma = karma

        #Cria canvas 
        self.canvas = ctk.CTkCanvas(self, width=var.WIN_LARGURA, height=var.WIN_ALTURA, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)


        #Imagem Inferno
        self.inferno_img = Image.open(var.caminho_inferno_bg).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.inferno_photo = ImageTk.PhotoImage(self.inferno_img)

        #Imagem Paraiso
        self.paraiso_img = Image.open(var.caminho_paraiso_bg).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.paraiso_photo = ImageTk.PhotoImage(self.paraiso_img)

        #Imagem Purgatorio
        self.purgatorio_img = Image.open(var.caminho_purgatorio_bg).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.purgatorio_photo = ImageTk.PhotoImage(self.purgatorio_img)

        #Imagem Morte (teste)
        self.morte_img = Image.open('imagens/morte.png').resize((650,650))
        self.morte_photo = ImageTk.PhotoImage(self.morte_img)


        self.canvas.create_text(700,400,text=f'karma total : {self.karma}',font=('arial',75))
        self.canvas.create_image(0,0,image='',anchor='nw',tags='bg')

        self.juizo_final()
        
    def juizo_final(self):
        print(self.karma)
        if self.karma <= -20:
            self.canvas.itemconfig('bg',image=self.inferno_photo)
        elif self.karma >= 35:
            self.canvas.itemconfig('bg',image=self.paraiso_photo)
        else:
            self.canvas.itemconfig('bg',image=self.purgatorio_photo)
            self.canvas.create_image((600,500),image=self.morte_photo) #(teste)
