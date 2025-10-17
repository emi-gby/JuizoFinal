import customtkinter as ctk
from PIL import Image, ImageTk
import variaveis as var
import cenarios as cen
from janelas import *

class Init_Jogo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title('Jogo da Vida')
        self.resizable(False,False)
        self.karma = 0

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
        self.canvas.tag_bind(f"trabalho", "<Button-1>", lambda _: self.chamar_fase('trabalho'))

        #Edificio- escola
        self.escola_img = Image.open(var.caminho_escola_img).resize((200,250))
        self.escola_photo = ImageTk.PhotoImage(self.escola_img)
        self.canvas.create_image(490, 150, image=self.escola_photo, tags='escola')
        self.canvas.tag_bind(f"escola", "<Button-1>", lambda _: self.chamar_fase('escola'))

        #Edificio- familia
        self.familia_img = Image.open(var.caminho_familia_img).resize((265,230))
        self.familia_photo = ImageTk.PhotoImage(self.familia_img)
        self.canvas.create_image(700, 310, image=self.familia_photo, tags='familia')
        self.canvas.tag_bind(f"familia", "<Button-1>", lambda _: self.chamar_fase('familia'))

        #Edificio- faculdade
        self.faculdade_img = Image.open(var.caminho_faculdade_img).resize((270,280))
        self.faculdade_photo = ImageTk.PhotoImage(self.faculdade_img)
        self.canvas.create_image(1190, 290, image=self.faculdade_photo, tags='faculdade')
        self.canvas.tag_bind(f"faculdade", "<Button-1>", lambda _: self.chamar_fase('faculdade'))

        self.jogo_fase = None  

    def chamar_fase(self,fase):
        if self.jogo_fase is not None:
            self.jogo_fase.destroy()
        self.jogo_fase = cen.JogoDaVida(self,fase,self.karma)
        
if __name__ == '__main__':
    jogo = Init_Jogo()
    jogo.mainloop()

