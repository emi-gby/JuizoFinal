import customtkinter as ctk
from PIL import Image, ImageTk
from caminhos import WIN_ALTURA, WIN_LARGURA

class Canvas(ctk.CTkCanvas):
    def __init__(self,master):
        super().__init__(master, width=WIN_LARGURA, height=WIN_ALTURA)
        self.pack(fill="both", expand=True)
        self.master = master

        #mantem referencia para os objetos PhotoImage 
        self.imagens_photo_lista = []

        self.final_photos_dict = {}
    
    def criar_imagem(self,caminho,tamanho, x,y, tags, anchor):
        '''Abre imagens, coverte para PhotoImage e bind tags se tiver'''
        imagem = Image.open(caminho).resize(tamanho)
        imagem_photo = ImageTk.PhotoImage(imagem)

        #salva referencia para previnir o 'garbage collection' do python
        self.imagens_photo_lista.append(imagem_photo)

        self.create_image(x,y, image=imagem_photo, tags=tags, anchor=anchor)

        if tags == "inicio_botao":
            self.tag_bind(tags, "<Button-1>", lambda _: self.master.tela_principal())

        elif tags != None and tags != "inicio_img":
            self.tag_bind(tags, "<Button-1>", lambda _: self.master.chamar_fase(tags))

    def importar_img_final(self,caminho,tags):
        '''Abre e converte as imagens do final do jogo'''
        imagem = Image.open(caminho).resize((WIN_LARGURA,WIN_ALTURA))
        imagem_photo = ImageTk.PhotoImage(imagem)

        self.final_photos_dict[tags] = imagem_photo


    
