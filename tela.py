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
        self.frame_final = CTkFrame(self.tela, width=1280, height=720,bg_color="transparent",fg_color="transparent")


terminou = False
app_tela = Tela()
tela = app_tela.tela

def inicia():
    global app_tela,tela,tela_cheia,frame_teclado,frame_escrita, frame_final, terminou,recomecar,fim
    terminou = False

    tela_cheia = StringVar(value="True")
    frame_teclado = app_tela.frame_teclado
    frame_escrita = app_tela.frame_escrita
    frame_final = app_tela.frame_final
    fim = CTkLabel(tela,text="Parabens Você Acertou!",font=("Comic Sans MS", 30, "bold"))
    fim.place(relx=0.37, rely=0.5)
    recomecar = CTkButton(tela,text="Jogar Novamente",command=inicia,width=80,height=40)
    recomecar.place(relx=0.37, rely=0.6)
    if  terminou == False:
            recomecar.place_forget()
            fim.place_forget()




inicia()  


     


def termina():
    global terminou
    terminou = True
    frame_escrita.place_forget()
    frame_teclado.place_forget()
    fim = CTkLabel(tela,text="Parabéns, Você Perdeu!",font=("Comic Sans MS", 30, "bold"))
    fim.place(relx=0.37, rely=0.5)
    recomecar = CTkButton(tela,text="Jogar Novamente",command=inicia,width=80,height=40)
    recomecar.place(relx=0.37, rely=0.6)
    
    

  

tela.bind("<Escape>", lambda e: tela.attributes('-fullscreen', False) or tela_cheia.set("False"))
tela.bind("<F11>", lambda e: tela.attributes('-fullscreen', True) or tela_cheia.set("True"))




