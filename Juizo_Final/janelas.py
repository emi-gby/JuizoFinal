import customtkinter as ctk

class Canvas(ctk.CTkCanvas):
    def __init__(self,master):
        super().__init__(master,width=1350, height=750,highlightthickness=0)
        self.pack(expand=True,fill='both')
        