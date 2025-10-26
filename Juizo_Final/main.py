import customtkinter as ctk
import config as var
import cenarios as cen
import final_jogo as fim
from canvas import Canvas
from pygame import mixer

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{var.WIN_LARGURA}x{var.WIN_ALTURA}')
        self.title('Jogo da Vida')
        self.resizable(False,False)
        self.karma = 0
        self.fases_lista = ['faculdade','escola','trabalho','familia']

        mixer.init()

        #Cria canvas 
        self.canvas = Canvas(self)

        #Imagem background 
        self.canvas.criar_imagem(caminho=var.caminho_main_img,tamanho=(var.WIN_LARGURA,var.WIN_ALTURA),x=0,y=0,tags=None,anchor='nw')
    
        #Edificio- trabalho
        self.canvas.criar_imagem(caminho=var.caminho_trabalho_img,tamanho=(370,430),x=400,y=520,tags="trabalho",anchor='center')

        #Edificio- escola
        self.canvas.criar_imagem(caminho=var.caminho_escola_img,tamanho=(300,320),x=400,y=200,tags="escola",anchor='center')

        #Edificio- familia
        self.canvas.criar_imagem(caminho=var.caminho_familia_img,tamanho=(370,360),x=955,y=560,tags="familia",anchor='center')

        #Edificio- faculdade
        self.canvas.criar_imagem(caminho=var.caminho_faculdade_img,tamanho=(270,280),x=960,y=180,tags="faculdade",anchor='center')

        #Imagem Inicio
        self.canvas.criar_imagem(caminho=var.caminho_inicio_bg,tamanho=(var.WIN_LARGURA,var.WIN_ALTURA),x=0,y=0,tags= "inicio_img",anchor='nw')

        #Imagem Play Botao
        self.canvas.criar_imagem(caminho=var.caminho_play_botao,tamanho=(510,190),x=var.WIN_LARGURA/2,y=663,tags="inicio_botao",anchor='center')

        #fim.FinalJogo(self,-40)
 

    def tela_principal(self):
        '''Destroe a tela inicial do jogo e começa a soundtrack'''
        self.canvas.delete('inicio_img','inicio_botao')
        #som clique botao start
        start_som = mixer.Sound(var.caminho_botao_start_som).play()
        start_som.set_volume(0.7)

        #soundtrack
        mixer.music.load(var.caminho_soundtrack)
        mixer.music.set_volume(0.2)
        mixer.music.play(loops=-1)


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
    jogo = App()
    jogo.mainloop()

