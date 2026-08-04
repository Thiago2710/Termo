from customtkinter import *

#tela principal

class Tela:

    def __init__(self):
        self.tela = CTk()
        self.tela.attributes('-fullscreen')
        self.tela.geometry("1280x720")

        self.tela.title("Termooo")
        self.frame_teclado = CTkFrame(self.tela, width=800, height=600)
        self.frame_teclado.place(relx=0.5, rely=0.98, anchor=S)
        self.frame_escrita = CTkFrame(self.tela, width=400, height=400,bg_color="transparent",fg_color="transparent")
        self.frame_escrita.place(relx=0.5, rely=0.1, anchor=N)



app_tela = Tela()
tela = app_tela.tela
tela_cheia = StringVar(value="True")
frame_teclado = app_tela.frame_teclado
frame_escrita = app_tela.frame_escrita

tela.bind("<Escape>", lambda e: tela.attributes('-fullscreen', False) or tela_cheia.set("False"))
tela.bind("<F11>", lambda e: tela.attributes('-fullscreen', True) or tela_cheia.set("True"))




