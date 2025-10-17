import customtkinter as ctk
from PIL import Image, ImageTk
import variaveis as var


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

        self.canvas.create_text(700,400,text=f'karma total : {self.karma}',
                                font=('arial',75))