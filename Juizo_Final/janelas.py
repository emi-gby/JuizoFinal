import customtkinter as ctk

class Label(ctk.CTkLabel):
    def __init__(self,master,bg,font,text):
        super().__init__(master,bg_color=bg,font=font,text=text)
        self.pack()

class Botao(ctk.CTkButton):
    def __init__(self,master,fg,font,text,func,col,chave):
        super().__init__(master,fg_color=fg,font=font,text=text,
                         command=lambda:func(chave),corner_radius=35,
                         width=300,height=200)
        self.grid(row=0,column=col,pady=5,padx=10,sticky='nswe')

class BotaoFrame(ctk.CTkFrame):
    def __init__(self,master,larg,alt):
        super().__init__(master,width=larg,
                         height=alt)
        self.pack(side='bottom',pady=10)

        self.columnconfigure((0,1,2),weight=1,uniform='a')
        self.rowconfigure(0,weight=1)
        