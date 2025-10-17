import customtkinter as ctk
from PIL import Image, ImageTk
import variaveis as var
import cenarios as cen
import final as fim

class Init_Jogo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title('Jogo da Vida')
        self.resizable(False,False)
        self.karma = 0
        self.fases_lista = ['faculdade','escola','trabalho','familia']

        #Cria canvas 
        self.canvas = ctk.CTkCanvas(self, width=var.WIN_LARGURA, height=var.WIN_ALTURA, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        #Imagem background 
        self.background_img = Image.open(var.caminho_main_img).resize((var.WIN_LARGURA,var.WIN_ALTURA))
        self.background_photo = ImageTk.PhotoImage(self.background_img)
        self.canvas.create_image(0,0,image=self.background_photo,anchor='nw')

        #Edificio- trabalho
        self.trabalho_img = Image.open(var.caminho_trabalho_img).resize((330,430))
        self.trabalho_photo = ImageTk.PhotoImage(self.trabalho_img)
        self.canvas.create_image(400, 520, image=self.trabalho_photo, tags='trabalho')
        self.canvas.tag_bind(f"trabalho", "<Button-1>", lambda _: self.chamar_fase('trabalho'))

        #Edificio- escola
        self.escola_img = Image.open(var.caminho_escola_img).resize((300,320))
        self.escola_photo = ImageTk.PhotoImage(self.escola_img)
        self.canvas.create_image(400, 200, image=self.escola_photo, tags='escola')
        self.canvas.tag_bind(f"escola", "<Button-1>", lambda _: self.chamar_fase('escola'))

        #Edificio- familia
        self.familia_img = Image.open(var.caminho_familia_img).resize((390,400))
        self.familia_photo = ImageTk.PhotoImage(self.familia_img)
        self.canvas.create_image(955, 560, image=self.familia_photo, tags='familia')
        self.canvas.tag_bind(f"familia", "<Button-1>", lambda _: self.chamar_fase('familia'))

        #Edificio- faculdade
        self.faculdade_img = Image.open(var.caminho_faculdade_img).resize((270,280))
        self.faculdade_photo = ImageTk.PhotoImage(self.faculdade_img)
        self.canvas.create_image(960, 180, image=self.faculdade_photo, tags='faculdade')
        self.canvas.tag_bind(f"faculdade", "<Button-1>", lambda _: self.chamar_fase('faculdade'))
        

    def chamar_fase(self,fase):
        '''Chama classe dos cenários e passa o valor da fase de acordo com  o 'botão' clicado '''
        self.jogo_fase = cen.JogoDaVida(self,fase)

    def calcular_karma(self, karma, fase):
        '''Remove a fase realizada da lista de fases, calcula o karma total e chama o final do jogo'''
        self.fases_lista.remove(fase)
        #Adiciona ao karma total o valor do karma relativo (karma totalizado do cenário) após a finalização da fase respectiva
        self.karma += karma

        #Quando todas as fases forem finalizadas, o final do jogo é chamado
        if len(self.fases_lista) == 0:
            self.final_jogo = fim.FinalJogo(self,self.karma)
            
    
        
if __name__ == '__main__':
    jogo = Init_Jogo()
    jogo.mainloop()

