from customtkinter import *
from tela import *
from funcoes_botoes import *
from PIL import Image






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
