from customtkinter import *
from tela import *
from PIL import Image


q =  CTkButton(frame_teclado, text="Q",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
q.grid(row=0, column=0, padx=5, pady=5)

w =  CTkButton(frame_teclado, text="W",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
w.grid(row=0, column=1, padx=5, pady=5)

e =  CTkButton(frame_teclado, text="E",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
e.grid(row=0, column=2, padx=5, pady=5)

r = CTkButton(frame_teclado, text="R",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
r.grid(row=0, column=3, padx=5, pady=5)

t = CTkButton(frame_teclado, text="T",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))   
t.grid(row=0, column=4, padx=5, pady=5)

y = CTkButton(frame_teclado, text="Y",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
y.grid(row=0, column=5, padx=5, pady=5)

u = CTkButton(frame_teclado, text="U",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
u.grid(row=0, column=6, padx=5, pady=5)

i= CTkButton(frame_teclado, text="I",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
i.grid(row=0, column=7, padx=5, pady=5)

o = CTkButton(frame_teclado, text="O",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
o.grid(row=0, column=8, padx=5, pady=5)

p = CTkButton(frame_teclado, text="P",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
p.grid(row=0, column=9, padx=5, pady=5)

a = CTkButton(frame_teclado, text="A",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
a.grid(row=1, column=0, padx=5, pady=5)

s = CTkButton(frame_teclado, text="S",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
s.grid(row=1, column=1, padx=5, pady=5)

d = CTkButton(frame_teclado, text="D",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
d.grid(row=1, column=2, padx=5, pady=5)

f = CTkButton(frame_teclado, text="F",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
f.grid(row=1, column=3, padx=5, pady=5)

g = CTkButton(frame_teclado, text="G",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
g.grid(row=1, column=4, padx=5, pady=5)

h = CTkButton(frame_teclado, text="H",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
h.grid(row=1, column=5, padx=5, pady=5)

j = CTkButton(frame_teclado, text="J",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
j.grid(row=1, column=6, padx=5, pady=5)

k = CTkButton(frame_teclado, text="K",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
k.grid(row=1, column=7, padx=5, pady=5)

l = CTkButton(frame_teclado, text="L",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
l.grid(row=1, column=8, padx=5, pady=5)

z = CTkButton(frame_teclado, text="Z",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
z.grid(row=2, column=0, padx=5, pady=5)

x = CTkButton(frame_teclado, text="X",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
x.grid(row=2, column=1, padx=5, pady=5)

c = CTkButton(frame_teclado, text="C",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
c.grid(row=2, column=2, padx=5, pady=5)

v = CTkButton(frame_teclado, text="V",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
v.grid(row=2, column=3, padx=5, pady=5)

b = CTkButton(frame_teclado, text="B",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
b.grid(row=2, column=4, padx=5, pady=5)

n = CTkButton(frame_teclado, text="N",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
n.grid(row=2, column=5, padx=5, pady=5)

m = CTkButton(frame_teclado, text="M",width=80,height=40,bg_color="#303030",fg_color="#525252",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
m.grid(row=2, column=6, padx=5, pady=5)

backspace = CTkButton(frame_teclado, text="Delete",width=80,height=40,bg_color="#303030",fg_color="#6B0000",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
backspace.grid(row=2, column=7, padx=5, pady=5)


enter = CTkButton(frame_teclado, text="ENTER",width=80,height=40,bg_color="#303030",fg_color="#006411",border_width=2,border_color="#020202",font=("Comic Sans MS", 20, "bold"))
enter.grid(row=2, column=8, padx=5, pady=5)





#parte de digitacao

#primera linha de escrita

linha1_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha1_letra1.grid(row=0, column=0,padx=5, pady=0)

linha1_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha1_letra2.grid(row=0, column=1,padx=5, pady=0)

linha1_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha1_letra3.grid(row=0, column=2,padx=5, pady=0)

linha1_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha1_letra4.grid(row=0, column=3,padx=5, pady=0)

linha1_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha1_letra5.grid(row=0, column=4,padx=5, pady=0)

# segunda linha

linha2_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha2_letra1.grid(row=1, column=0,padx=5, pady=60)

linha2_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha2_letra2.grid(row=1, column=1,padx=5, pady=60)

linha2_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha2_letra3.grid(row=1, column=2,padx=5, pady=60)

linha2_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha2_letra4.grid(row=1, column=3,padx=5, pady=60)

linha2_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha2_letra5.grid(row=1, column=4,padx=5, pady=60)

#terceira linha

linha3_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha3_letra1.grid(row=2, column=0,padx=5, pady=5)

linha3_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha3_letra2.grid(row=2, column=1,padx=5, pady=5)

linha3_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha3_letra3.grid(row=2, column=2,padx=5, pady=5)

linha3_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha3_letra4.grid(row=2, column=3,padx=5, pady=5)

linha3_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha3_letra5.grid(row=2, column=4,padx=5, pady=5)

#quarta linha

linha4_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha4_letra1.grid(row=3, column=0,padx=5, pady=60)

linha4_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha4_letra2.grid(row=3, column=1,padx=5, pady=60)

linha4_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha4_letra3.grid(row=3, column=2,padx=5, pady=60)

linha4_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha4_letra4.grid(row=3, column=3,padx=5, pady=60)

linha4_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha4_letra5.grid(row=3, column=4,padx=5, pady=60)

#quinta linha

linha5_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha5_letra1.grid(row=4, column=0,padx=5, pady=0)

linha5_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha5_letra2.grid(row=4, column=1,padx=5, pady=0)

linha5_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha5_letra3.grid(row=4, column=2,padx=5, pady=0)

linha5_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha5_letra4.grid(row=4, column=3,padx=5, pady=0)

linha5_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha5_letra5.grid(row=4, column=4,padx=5, pady=0)

#sexta linha

linha6_letra1 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha6_letra1.grid(row=5, column=0,padx=5, pady=(60,0))

linha6_letra2 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha6_letra2.grid(row=5, column=1,padx=5, pady=(60,0))

linha6_letra3 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha6_letra3.grid(row=5, column=2,padx=5, pady=(60,0))

linha6_letra4 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha6_letra4.grid(row=5, column=3,padx=5, pady=(60,0))

linha6_letra5 = CTkLabel(frame_escrita,text="__________",bg_color="transparent",fg_color="transparent",font=("Comic Sans MS", 20, "bold"))
linha6_letra5.grid(row=5, column=4,padx=5, pady=(60,0))
