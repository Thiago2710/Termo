from tela import *
from customtkinter import *
from labels_escrita import *
from palavras_chutaveis import *
from palavras_possivels import *
from random import *





p_certa  = "STEAM"
letras_erradas = []
letras_digitadas = []
palavra = []
labels = []
##controle
acertou = False
letra_atual=0
linha_atual=0
letra_digitada = CTkLabel(frame_escrita,text="",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
mostra = CTkLabel(frame_escrita,text="_________",bg_color="gray",fg_color="gray",font=("Comic Sans MS", 20, "bold"))


def chama_mostra():
    global letra_atual,letra_digitada, linha_atual, mostra, acertou
    mostra.grid(row=linha_atual, column=letra_atual,padx=0,pady=0)



def funcao_q():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "Q" in letras_erradas:
        return
    letra_q = CTkLabel(frame_escrita, text="Q", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_q.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_q)
    letra_digitada = letra_q
    palavra.append("Q")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_w():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "W" in letras_erradas:
        return
    letra_w = CTkLabel(frame_escrita, text="W", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_w.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_w)
    letra_digitada = letra_w
    palavra.append("W")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_e():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "E" in letras_erradas:
        return
    letra_e = CTkLabel(frame_escrita, text="E", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_e.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_e)
    letra_digitada = letra_e
    palavra.append("E")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_r():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "R" in letras_erradas:
        return
    letra_r = CTkLabel(frame_escrita, text="R", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_r.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_r)
    letra_digitada = letra_r
    palavra.append("R")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_t():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "T" in letras_erradas:
        return
    letra_t = CTkLabel(frame_escrita, text="T", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_t.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_t)
    letra_digitada = letra_t
    palavra.append("T")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_y():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "Y" in letras_erradas:
        return
    letra_y = CTkLabel(frame_escrita, text="Y", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_y.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_y)
    letra_digitada = letra_y
    palavra.append("Y")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_u():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "U" in letras_erradas:
        return
    letra_u = CTkLabel(frame_escrita, text="U", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_u.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_u)
    letra_digitada = letra_u
    palavra.append("U")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_i():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "I" in letras_erradas:
        return
    letra_i = CTkLabel(frame_escrita, text="I", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_i.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_i)
    letra_digitada = letra_i
    palavra.append("I")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_o():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "O" in letras_erradas:
        return
    letra_o = CTkLabel(frame_escrita, text="O", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_o.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_o)
    letra_digitada = letra_o
    palavra.append("O")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_p():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "P" in letras_erradas:
        return
    letra_p = CTkLabel(frame_escrita, text="P", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_p.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_p)
    letra_digitada = letra_p
    palavra.append("P")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_a():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "A" in letras_erradas:
        return
    letra_a = CTkLabel(frame_escrita, text="A", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_a.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_a)
    letra_digitada = letra_a
    palavra.append("A")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_s():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "S" in letras_erradas:
        return
    letra_s = CTkLabel(frame_escrita, text="S", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_s.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_s)
    letra_digitada = letra_s
    palavra.append("S")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_d():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "D" in letras_erradas:
        return
    letra_d = CTkLabel(frame_escrita, text="D", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_d.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_d)
    letra_digitada = letra_d
    palavra.append("D")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_f():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "F" in letras_erradas:
        return
    letra_f = CTkLabel(frame_escrita, text="F", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_f.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_f)
    letra_digitada = letra_f
    palavra.append("F")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_g():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "G" in letras_erradas:
        return
    letra_g = CTkLabel(frame_escrita, text="G", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_g.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_g)
    letra_digitada = letra_g
    palavra.append("G")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_h():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "H" in letras_erradas:
        return
    letra_h = CTkLabel(frame_escrita, text="H", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_h.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_h)
    letra_digitada = letra_h
    palavra.append("H")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_j():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "J" in letras_erradas:
        return
    letra_j = CTkLabel(frame_escrita, text="J", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_j.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_j)
    letra_digitada = letra_j
    palavra.append("J")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_k():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "K" in letras_erradas:
        return
    letra_k = CTkLabel(frame_escrita, text="K", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_k.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_k)
    letra_digitada = letra_k
    palavra.append("K")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_l():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "L" in letras_erradas:
        return
    letra_l = CTkLabel(frame_escrita, text="L", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_l.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_l)
    letra_digitada = letra_l
    palavra.append("L")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_z():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "Z" in letras_erradas:
        return
    letra_z = CTkLabel(frame_escrita, text="Z", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_z.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_z)
    letra_digitada = letra_z
    palavra.append("Z")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_x():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "X" in letras_erradas:
        return
    letra_x = CTkLabel(frame_escrita, text="X", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_x.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_x)
    letra_digitada = letra_x
    palavra.append("X")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_c():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "C" in letras_erradas:
        return
    letra_c = CTkLabel(frame_escrita, text="C", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_c.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_c)
    letra_digitada = letra_c
    palavra.append("C")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_v():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "V" in letras_erradas:
        return
    letra_v = CTkLabel(frame_escrita, text="V", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_v.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_v)
    letra_digitada = letra_v
    palavra.append("V")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_b():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "B" in letras_erradas:
        return
    letra_b = CTkLabel(frame_escrita, text="B", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_b.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_b)
    letra_digitada = letra_b
    palavra.append("B")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_n():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "N" in letras_erradas:
        return
    letra_n = CTkLabel(frame_escrita, text="N", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_n.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_n)
    letra_digitada = letra_n
    palavra.append("N")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()


def funcao_m():
    global letra_atual, letra_digitada, linha_atual, mostra, acertou
    if letra_atual == 5 or linha_atual == 6 or acertou == True or "M" in letras_erradas:
        return
    letra_m = CTkLabel(frame_escrita, text="M", bg_color="transparent", fg_color="transparent", font=("Comic Sans MS", 20, "bold"))
    letra_m.grid(row=linha_atual, column=letra_atual, padx=0, pady=0)
    letra_atual += 1
    letras_digitadas.append(letra_m)
    letra_digitada = letra_m
    palavra.append("M")
    mostra.grid_forget()
    if letra_atual == 5:
        return
    chama_mostra()

def apaga():
    global letra_atual,letra_digitada
    if letra_atual == 0:
        return
    letra_atual -=1
    letra_removida = letras_digitadas.pop()
    
    palavra.pop()
    letra_removida.grid_forget()
    mostra.grid_forget()
    chama_mostra()
    if len(letras_digitadas)>0:
        letra_digitada = letras_digitadas[-1]

letras_erradas1 = []
letras_fixas = []

def enter_func():
    global letra_atual,letra_digitada, linha_atual,acertou,palavra_chutada

    if letra_atual < 5 or acertou == True:
        return

    palavra_chutada = palavra[0] + palavra[1] + palavra[2] + palavra[3] + palavra[4]
    if palavra_chutada not in palavras_chutaveis:
        informe = CTkLabel(tela, text="Não Possuimos esta palavra", font=("Comic Sans", 30,"bold" ))
        informe.place(relx=0.35, rely=0.01)
        tela.after(1357, informe.place_forget)
        return
        

    #letra um
    if palavra[0] == p_certa[0]: #se a letra estiver no lugar certo
        l_certa = CTkLabel(frame_escrita, text=f"____{palavra[0]}____", bg_color="darkgreen", fg_color="darkgreen", font=("Comic Sans MS", 20, "bold"))
        l_certa.grid(row=linha_atual, column=0, padx=0, pady=0)
        letras_fixas.append(l_certa)
    elif palavra[0] in p_certa: # se a letra estiver no lugar errado
        l_certa = CTkLabel(frame_escrita, text=f"____{palavra[0]}____", bg_color="#B68918", fg_color="#B68918", font=("Comic Sans MS", 20, "bold"))
        l_certa.grid(row=linha_atual, column=0, padx=0, pady=0)
        letras_fixas.append(l_certa)
    else:
        l_certa = CTkLabel(frame_escrita, text=f"____{palavra[0]}____", bg_color="darkred", fg_color="darkred", font=("Comic Sans MS", 20, "bold"))
        l_certa.grid(row=linha_atual, column=0, padx=0, pady=0)
        letras_erradas1.append(palavra[0])
        letras_fixas.append(l_certa)

    #letra dois
    if palavra[1] == p_certa[1]:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[1]}____", bg_color="darkgreen", fg_color="darkgreen", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=1, padx=0, pady=0)
            letras_fixas.append(l_certa)
    elif palavra[1] in p_certa:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[1]}____", bg_color="#B68918", fg_color="#B68918", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=1, padx=0, pady=0)
            letras_fixas.append(l_certa)
    else:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[1]}____", bg_color="darkred", fg_color="darkred", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=1, padx=0, pady=0)
            letras_erradas1.append(palavra[1])
            letras_fixas.append(l_certa)

    if palavra[2] == p_certa[2]:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[2]}____", bg_color="darkgreen", fg_color="darkgreen", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=2, padx=0, pady=0)
            letras_fixas.append(l_certa)
    elif palavra[2] in p_certa:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[2]}____", bg_color="#B68918", fg_color="#B68918", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=2, padx=0, pady=0)
            letras_fixas.append(l_certa)
    else:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[2]}____", bg_color="darkred", fg_color="darkred", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=2, padx=0, pady=0)
            letras_erradas1.append(palavra[2])
            letras_fixas.append(l_certa)


    if palavra[3] == p_certa[3]:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[3]}____", bg_color="darkgreen", fg_color="darkgreen", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=3, padx=0, pady=0)
            letras_fixas.append(l_certa)
    elif palavra[3] in p_certa:
                l_certa = CTkLabel(frame_escrita, text=f"____{palavra[3]}____", bg_color="#B68918", fg_color="#B68918", font=("Comic Sans MS", 20, "bold"))
                l_certa.grid(row=linha_atual, column=3, padx=0, pady=0)
                letras_fixas.append(l_certa)

    else:
                l_certa = CTkLabel(frame_escrita, text=f"____{palavra[3]}____", bg_color="darkred", fg_color="darkred", font=("Comic Sans MS", 20, "bold"))
                l_certa.grid(row=linha_atual, column=3, padx=0, pady=0)
                letras_erradas1.append(palavra[3])
                letras_fixas.append(l_certa)


    if palavra[4] == p_certa[4]:
            l_certa = CTkLabel(frame_escrita, text=f"____{palavra[4]}____", bg_color="darkgreen", fg_color="darkgreen", font=("Comic Sans MS", 20, "bold"))
            l_certa.grid(row=linha_atual, column=4, padx=0, pady=0)
            letras_fixas.append(l_certa)
    elif palavra[4] in p_certa:
                l_certa = CTkLabel(frame_escrita, text=f"____{palavra[4]}____", bg_color="#DAA520", fg_color="#B68918", font=("Comic Sans MS", 20, "bold"))
                l_certa.grid(row=linha_atual, column=4, padx=0, pady=0)
                letras_fixas.append(l_certa)
    else:
                l_certa = CTkLabel(frame_escrita, text=f"____{palavra[4]}____", bg_color="darkred", fg_color="darkred", font=("Comic Sans MS", 20, "bold"))
                l_certa.grid(row=linha_atual, column=4, padx=0, pady=0)
                letras_erradas1.append(palavra[4])
                letras_fixas.append(l_certa)
    for l in letras_erradas1:
            atualiza_cor(l)

    if palavra[0] == p_certa[0] and palavra[1] == p_certa[1] and palavra[2] == p_certa[2] and palavra[3] == p_certa[3] and palavra[4] == p_certa[4]:
        acertou=True
        palavra_correta()
    else:
        if linha_atual == 5:
            perdeu()
            return
        letra_atual = 0
        linha_atual += 1
        palavra.clear()

acertos = StringVar()
acertos1 = 0
acertos.set(acertos1)
mostra_acertos = CTkLabel(tela,text=f"Acertos:{acertos.get()}",font=("Comic Sans MS", 20, "bold"))
mostra_acertos.grid(row=0, column=0, padx=0, pady=0)

def palavra_correta():
    global acertos1, letra_atual,letras_digitadas, letra_digitada,acertou,linha_atual,p_certa, letras_erradas1
    if acertou == True:
        for letra in letras_digitadas:
            letra.grid_forget()
        letras_digitadas.clear()
        for l in letras_erradas1:
            atualiza_cor(l)
        letras_erradas1 = []
        contador=0
        while letras_fixas:
            removida = letras_fixas.pop(contador)
            removida.grid_forget()

        
            
        acertos1+=1
        acertos.set(acertos1)
        mostra_acertos.configure(text=f"Acertos:{acertos.get()}",font=("Comic Sans MS", 20, "bold"))
        letra_atual =0
        letras_digitadas.clear()
        palavra.clear()
        letra_digitada.grid_forget()
        mostra.grid_forget()
        letras_erradas.clear()
        letra_atual = 0
        linha_atual = 0
        chama_mostra()
        if len(letras_digitadas)>0:
            letra_digitada = letras_digitadas[-1]
        acertou=False
        num = randint(0, 110)
        p_certa=palavras_possiveis[num]
    
def perdeu():
    acertos1 = 0
    acertos.set(acertos1)
    termina()


def atualiza_cor(l):
    if acertou == True:
         dicionario_letras[l].configure(bg_color="#303030",fg_color="#525252")
         return
         
    dicionario_letras[l].configure(bg_color="#161616",fg_color="#161616")



q =  CTkButton(frame_teclado, text="Q",width=80,height=40,command=funcao_q,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
q.grid(row=0, column=0, padx=5, pady=5)



w =  CTkButton(frame_teclado, text="W",width=80,height=40,command = funcao_w, bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
w.grid(row=0, column=1, padx=5, pady=5)

e =  CTkButton(frame_teclado, text="E",command=funcao_e,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
e.grid(row=0, column=2, padx=5, pady=5)


r = CTkButton(frame_teclado, text="R",command=funcao_r,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
r.grid(row=0, column=3, padx=5, pady=5)

t = CTkButton(frame_teclado, text="T",command=funcao_t,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))   
t.grid(row=0, column=4, padx=5, pady=5)

y = CTkButton(frame_teclado, text="Y",command=funcao_y,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
y.grid(row=0, column=5, padx=5, pady=5)

u = CTkButton(frame_teclado, text="U",command=funcao_u,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
u.grid(row=0, column=6, padx=5, pady=5)

i= CTkButton(frame_teclado, text="I",command=funcao_i,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
i.grid(row=0, column=7, padx=5, pady=5)

o = CTkButton(frame_teclado, text="O",command=funcao_o,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
o.grid(row=0, column=8, padx=5, pady=5)

p = CTkButton(frame_teclado, text="P",command=funcao_p,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
p.grid(row=0, column=9, padx=5, pady=5)

a = CTkButton(frame_teclado, text="A",command=funcao_a,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
a.grid(row=1, column=0, padx=5, pady=5)

s = CTkButton(frame_teclado, text="S",command=funcao_s,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
s.grid(row=1, column=1, padx=5, pady=5)

d = CTkButton(frame_teclado, text="D",command=funcao_d,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
d.grid(row=1, column=2, padx=5, pady=5)

f = CTkButton(frame_teclado, text="F",command=funcao_f,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
f.grid(row=1, column=3, padx=5, pady=5)

g = CTkButton(frame_teclado, text="G",command=funcao_g,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
g.grid(row=1, column=4, padx=5, pady=5)

h = CTkButton(frame_teclado, text="H",command=funcao_h,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
h.grid(row=1, column=5, padx=5, pady=5)

j = CTkButton(frame_teclado, text="J",command=funcao_j,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
j.grid(row=1, column=6, padx=5, pady=5)

k = CTkButton(frame_teclado, text="K",command=funcao_k,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
k.grid(row=1, column=7, padx=5, pady=5)

l = CTkButton(frame_teclado, text="L",command=funcao_l,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
l.grid(row=1, column=8, padx=5, pady=5)

z = CTkButton(frame_teclado, text="Z",command=funcao_z,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
z.grid(row=2, column=0, padx=5, pady=5)

x = CTkButton(frame_teclado, text="X",command=funcao_x,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
x.grid(row=2, column=1, padx=5, pady=5)

c = CTkButton(frame_teclado, text="C",command=funcao_c,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
c.grid(row=2, column=2, padx=5, pady=5)

v = CTkButton(frame_teclado, text="V",command=funcao_v,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
v.grid(row=2, column=3, padx=5, pady=5)

b = CTkButton(frame_teclado, text="B",command=funcao_b,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
b.grid(row=2, column=4, padx=5, pady=5)

n = CTkButton(frame_teclado, text="N",command=funcao_n,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
n.grid(row=2, column=5, padx=5, pady=5)

m = CTkButton(frame_teclado, text="M",command=funcao_m,width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
m.grid(row=2, column=6, padx=5, pady=5)

backspace = CTkButton(frame_teclado, text="Delete",command=apaga,width=80,height=40,bg_color="#303030",fg_color="#6B0000",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
backspace.grid(row=2, column=7, padx=5, pady=5)

enter = CTkButton(frame_teclado, text="ENTER",command=enter_func,width=80,height=40,bg_color="#303030",fg_color="#006411",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
enter.grid(row=2, column=8, padx=5, pady=5)

dicionario_letras = { "A": a, "B": b, "C": c, "D": d, "E": e, "F": f,
    "G": g, "H": h, "I": i, "J": j, "K": k, "L": l,
    "M": m, "N": n, "O": o, "P": p, "Q": q, "R": r,
    "S": s, "T": t, "U": u, "V": v, "W": w, "X": x,
    "Y": y, "Z": z}

tela.bind("<a>", lambda e: funcao_a())
tela.bind("<b>", lambda e: funcao_b())
tela.bind("<c>", lambda e: funcao_c())
tela.bind("<d>", lambda e: funcao_d())
tela.bind("<e>", lambda e: funcao_e())
tela.bind("<f>", lambda e: funcao_f())
tela.bind("<g>", lambda e: funcao_g())
tela.bind("<h>", lambda e: funcao_h())
tela.bind("<i>", lambda e: funcao_i())
tela.bind("<j>", lambda e: funcao_j())
tela.bind("<k>", lambda e: funcao_k())
tela.bind("<l>", lambda e: funcao_l())
tela.bind("<m>", lambda e: funcao_m())
tela.bind("<n>", lambda e: funcao_n())
tela.bind("<o>", lambda e: funcao_o())
tela.bind("<p>", lambda e: funcao_p())
tela.bind("<q>", lambda e: funcao_q())
tela.bind("<r>", lambda e: funcao_r())
tela.bind("<s>", lambda e: funcao_s())
tela.bind("<t>", lambda e: funcao_t())
tela.bind("<u>", lambda e: funcao_u())
tela.bind("<v>", lambda e: funcao_v())
tela.bind("<w>", lambda e: funcao_w())
tela.bind("<x>", lambda e: funcao_x())
tela.bind("<y>", lambda e: funcao_y())
tela.bind("<z>", lambda e: funcao_z())

tela.bind("<Return>", lambda e: enter_func())
tela.bind("<BackSpace>", lambda e: apaga())
