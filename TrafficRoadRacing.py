import tkinter
import random 
# Crea la ventana
vt = tkinter.Tk()
vt.title("Traffic Road Racing")
# Ajusta el tamaño de la ventana creada
vt.geometry("600x400")
# Fondo del menu
menu = tkinter.PhotoImage(file = "Menu.png")
labelmenu = tkinter.Label(vt, image=menu).pack()
# Nombre jugadores
player1 = tkinter.Label(vt,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=150,y=250)
player2 = tkinter.Label(vt,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=150,y=285)
# Insertar nombres de los jugadores
ply1 = tkinter.StringVar()
ply2 = tkinter.StringVar()
ply1txt = tkinter.Entry(vt,textvariable=ply1,font=("Minecraft",10), fg="white", bg="black").place(x=238,y=253)
ply2txt = tkinter.Entry(vt,textvariable=ply2,font=("Minecraft",10), fg="white", bg="black").place(x=238,y=288)
# Imagenes de niveles
nivel1 = tkinter.PhotoImage(file="Level1player1.png")
nivel11 = tkinter.PhotoImage(file="Level1Player2.png")
nivel2 = tkinter.PhotoImage(file="Level2.png")
nivel22 = tkinter.PhotoImage(file="Level22.png")
nivel3 = tkinter.PhotoImage(file="Level3.png")
nivel33 = tkinter.PhotoImage(file="Level32.png")
nivel4 = tkinter.PhotoImage(file="Level4.png")
nivel44 = tkinter.PhotoImage(file="Level42.png")
nivel5 = tkinter.PhotoImage(file="Level5.png")
nivel55 = tkinter.PhotoImage(file="Level52.png")
# Imagen Explosion
explosion = tkinter.PhotoImage(file="Explosion2.png")
# Funcion abrir Lvl 1
presiono = False
x = None
y = None
m = None
m2 = None
i = 0
j = 0
k = 0
t = 0
contador = 0
contadorr = 0
contadorr2 = 0
contadorm = 0
contadorm2 = 0
contadorf = 0
contadorf2 = 0
contadorg = 60
contadorg2 = 60
contadorgaso = 0
contadorgaso2 = 0
contadoraceite = 0
contadoraceite2 = 0
score = tkinter.StringVar()
score2 = tkinter.StringVar()

l = 0
equis = random.uniform(0,100)
# Imagenes de carros
player01 = tkinter.PhotoImage(file="Player01.png")
player02 = tkinter.PhotoImage(file="Player02.png")
fighter = tkinter.PhotoImage(file="Fighter.png")
fighter2 = tkinter.PhotoImage(file="Fighter2.png")
runner = tkinter.PhotoImage(file="Runner.png")
runner2 = tkinter.PhotoImage(file="Runner2.png")
minivan = tkinter.PhotoImage(file="Minivan.png")
minivan2 = tkinter.PhotoImage(file="Minivan2.png")

# Carro volteado
vol1 = tkinter.PhotoImage(file="Voltea1.png")
vol2 = tkinter.PhotoImage(file="Voltea2.png")

# Imagenes vidas (gasolina)
gasolina1 = tkinter.PhotoImage(file="Corazao1.png")
gasolina2 = tkinter.PhotoImage(file="Corazao2.png")
gasolina3 = tkinter.PhotoImage(file="Corazao3.png")
gasolina4 = tkinter.PhotoImage(file="Corazao4.png")
gasolina5 = tkinter.PhotoImage(file="Corazao5.png")
gasolina6 = tkinter.PhotoImage(file="Corazao6.png")

gasolina11 = tkinter.PhotoImage(file="Corazao11.png")
gasolina22 = tkinter.PhotoImage(file="Corazao22.png")
gasolina33 = tkinter.PhotoImage(file="Corazao33.png")
gasolina44 = tkinter.PhotoImage(file="Corazao44.png")
gasolina55 = tkinter.PhotoImage(file="Corazao55.png")
gasolina66 = tkinter.PhotoImage(file="Corazao66.png")

# Imagen Gasolina
gasol = tkinter.PhotoImage(file="Gasolina.png")
gasol2 = tkinter.PhotoImage(file="Gasolina2.png")

# Imagenes win y lose
win = tkinter.PhotoImage(file="Youwin.png")
lose = tkinter.PhotoImage(file="Youlose.png")

# Imagen aceite
aceite = tkinter.PhotoImage(file="Aceitee.png")
aceite2 = tkinter.PhotoImage(file="Aceite.png")

def Level1():
    """
    Nivel 1 de Traffic Road Racing
    """
    global level1,canvas,nivel1,w,x,y,m,k,f,r,contador,m2,w2,r2,f2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,gas,equis,ac,gas2,ac2,ply1,ply2,puntoss,puntoss2
    level1 = tkinter.Toplevel(vt)
    vt.iconify()
    level1.geometry("1200x1000")
    canvas = tkinter.Canvas(level1, width=1500, height=780,bg="black")
    w = canvas.create_image(250,400,image=nivel1)
    w2 = canvas.create_image(850,400,image=nivel11)
    canvas.lower(w)
    canvas.lower(w2)
    canvas.bind("<Key>", key)
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()
    carretera()
    key()
    # Estados de los jugadores
    p1 = tkinter.Label(canvas,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=50)
    km1 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=130)
    fuel1 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=210)
    p2 = tkinter.Label(canvas,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=580,y=350)
    km2 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=600,y=430)
    fuel2 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=616,y=510)
    # Cargar imagenes de carros
    x = canvas.create_image(200,620,image=player01)
    y = canvas.create_image(795,620,image=player02)
    f = canvas.create_image(200,0,image=fighter)
    f2 = canvas.create_image(820,0,image=fighter2)
    m = canvas.create_image(257,0,image=minivan)
    m2 = canvas.create_image(845,0,image=minivan2)
    r = canvas.create_image(200,0,image=runner)
    r2 = canvas.create_image(800,0,image=runner2)
    # Cargar imagen vidas(gasolina)
    g1 = canvas.create_image(460,245,image=gasolina1)
    g2 = canvas.create_image(470,245,image=gasolina2)
    g3 = canvas.create_image(480,245,image=gasolina3)
    g4 = canvas.create_image(490,245,image=gasolina4)
    g5 = canvas.create_image(500,245,image=gasolina5)
    g6 = canvas.create_image(510,245,image=gasolina6)

    g11 = canvas.create_image(606,545,image=gasolina11)
    g22 = canvas.create_image(616,545,image=gasolina22)
    g33 = canvas.create_image(626,545,image=gasolina33)
    g44 = canvas.create_image(636,545,image=gasolina44)
    g55 = canvas.create_image(646,545,image=gasolina55)
    g66 = canvas.create_image(656,545,image=gasolina66)

    # Cargar Imagen gasolina
    gas = canvas.create_image(230,0,image=gasol)
    gas2 = canvas.create_image(820,0,image=gasol2)

    # Cargar Imagen aceite
    ac = canvas.create_image(200+equis,0,image=aceite)
    ac2 = canvas.create_image(820+equis,0,image=aceite2)

    # Nombres de los jugadores en el juego
    jugador1 = tkinter.Label(canvas,textvariable=ply1,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=75)
    jugador2 = tkinter.Label(canvas,textvariable=ply2,font=("Minecraft",11), fg="white", bg="black").place(x=540,y=375)

    # kilometraje
    scorer = tkinter.Label(canvas,textvariable=score,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=155)
    scorer2 = tkinter.Label(canvas,textvariable=score2,font=("Minecraft",11), fg="white", bg="black").place(x=570,y=455)
    kilo = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=495,y=155)
    kilo2 = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=610,y=455)
    
    # Funciones
    Minivan1()
    Fighter1()
    Runner1()
    Gasolina()
    GasolinaBonus()
    Aceite()
    Puntos()
    

def Ayuda():
    """
    Función para mostrar la ayuda en el shell.
    """
    a = open("ReadMe.txt","r")
    for linea in a.readlines(): 
        print(linea)


    
# Funciones mover dos jugadores al tiempo
h = []
def keyup(e):
    global h
    if(e.keycode in h):
        h.pop(h.index(e.keycode))
def keydown(e):
    global h
    if not e.keycode in h:
        h.append(e.keycode)

# Funcion botones de los jugadores
def key():
    """
    Funcion para añadir el código ASCII de las teclas.
    """
    global x,y,i,j,k,t,w,h,w2,contadorg,contadorg2
    if 68 in h:
        if(i < 144):
            canvas.delete(x)
            i = i + 2
            x = canvas.create_image(200+i,620,image=player01)
        else:
            contadorg = 0
            canvas.delete(x)
            x = canvas.create_image(200+i,620,image=explosion)
            canvas.move(w,0,-canvas.coords(w)[1])
    if 65 in h: 
        if(i > -22):
            canvas.delete(x)
            i = i - 2
            x = canvas.create_image(200+i,620,image=player01)
        else:
            contadorg = 0
            canvas.delete(x)
            x = canvas.create_image(200+i,620,image=explosion)
            canvas.move(w,0,-canvas.coords(w)[1])
    
    if 76 in h:
        if(k < 136):
            canvas.delete(y)
            k = k + 2
            y = canvas.create_image(795+k,620,image=player02)
        else:
            contadorg2 = 0
            canvas.delete(y)
            y = canvas.create_image(795+k,620,image=explosion)
            canvas.move(w2,0,-canvas.coords(w2)[1])
    if 74 in h: 
        if(k > -25):
            canvas.delete(y)
            k = k - 2
            y = canvas.create_image(795+k,620,image=player02)
        else:
            contadorg2 = 0
            canvas.delete(y)
            y = canvas.create_image(795+k,620,image=explosion)
            canvas.move(w2,0,-canvas.coords(w2)[1])
    canvas.after(8,key)
    
# Funcion carretera
def carretera():
    """
    Función para hacer que la carretera se repita cada cierto número de pixeles
    """
    global w,w2,canvas,contador,i,k
    if(contador < 100):
        canvas.move(w,0,5)
        canvas.move(w2,0,5)
    if(canvas.coords(w)[1]>=2000):
        canvas.move(w,0,-canvas.coords(w)[1])
    if(canvas.coords(w2)[1]>=2000):
        canvas.move(w2,0,-canvas.coords(w2)[1])
    canvas.after(1,carretera)

    
# Funcion Runner
def Runner1():
    """
    Función para hacer que el carro runner cambie de carril siempre sin importar dónde esté el jugador
    """
    global x,y,i,j,k,canvas,r,r2,equis,level1,contadorr,contadorr2,w,w2,x,y,contadorg,contadorg2,puntoss,puntoss2
    
    if(contadorr < 48):
        contadorr = contadorr + 1
        canvas.move(r,3,5)
    if(contadorr2 < 48):
        canvas.move(r2,3,5)
        contadorr2 = contadorr2 + 1
    if(contadorr >= 48 and contadorr < 100):
        canvas.move(r,-3,5)
        contadorr = contadorr + 1
    if(contadorr2 >= 48 and contadorr2 < 100):
        canvas.move(r2,-3,5)
        contadorr2 = contadorr2 + 1
    if(contadorr >= 100 and contadorr < 150):
        canvas.move(r,3,5)
        contadorr = contadorr + 1
    if(contadorr2 >= 100 and contadorr2 < 150):
        canvas.move(r2,3,5)
        contadorr2 = contadorr2 + 1
    if(contadorr >= 150 and contadorr < 200):
        canvas.move(r,-3,5)
        contadorr = contadorr + 1
        if(contadorr >= 200):
            contadorr = 0
            r = canvas.create_image(200,0,image=runner)
            
    if(contadorr2 >= 150 and contadorr2 < 200):
        canvas.move(r2,-3,5)
        contadorr2 = contadorr2 + 1
        if(contadorr2 >= 200):
            contadorr2 = 0
            r2 = canvas.create_image(800,0,image=runner2)
            
    canvas.after(30,Runner1)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashrx2=canvas.coords(r)[0]
    crashry2=canvas.coords(r)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashrx22=canvas.coords(r2)[0]
    crashry22=canvas.coords(r2)[1]
    
    if(crashx1 >= crashrx2 and crashx1 <= crashrx2 + 25 and crashy1 >= crashry2 and crashy1 <= crashry2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(r)
        r = canvas.create_image(200,0,image=runner)
        contadorr = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashrx2 and crashx1 + 25 >= crashrx2 and crashy1 <= crashry2 and crashy1 + 55 >= crashry2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(r)
        r = canvas.create_image(200,0,image=runner)
        contadorm = 0
        contadorr = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashrx22 and crashx11 <= crashrx22 + 25 and crashy11 >= crashry22 and crashy11 <= crashry22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(r2)
        r2 = canvas.create_image(800,0,image=runner2)
        contadorr2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashrx22 and crashx11 + 25 >= crashrx22 and crashy11 <= crashry22 and crashy11 + 55 >= crashry22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(r2)
        r2 = canvas.create_image(800,0,image=runner2)
        contadorr2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])

# Funcion Minivan 
def Minivan1():
    """
    Función para hacer que el carro minivan siempre vaya en un carril.
    """
    global canvas,m,m2,i,k,x,j,y,equis,f,explosion,contadorg,contadorg2,contadorm,contadorm2,puntoss,puntoss2,w,w2,contador
    equis = random.uniform(0,100)
    if(contadorm < 180):
        canvas.move(m,0,5)
        contadorm = contadorm + 1
    if(contadorm2 < 180):
        canvas.move(m2,0,5)
        contadorm2 = contadorm2 + 1
    if(contadorm == 180):
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
    if(contadorm2 == 180):
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
    canvas.after(30,Minivan1)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashx2=canvas.coords(m)[0]
    crashy2=canvas.coords(m)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashx22=canvas.coords(m2)[0]
    crashy22=canvas.coords(m2)[1]
    
    if(crashx1 >= crashx2 and crashx1 <= crashx2 + 25 and crashy1 >= crashy2 and crashy1 <= crashy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashx2 and crashx1 + 25 >= crashx2 and crashy1 <= crashy2 and crashy1 + 55 >= crashy2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashx22 and crashx11 <= crashx22 + 25 and crashy11 >= crashy22 and crashy11 <= crashy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashx22 and crashx11 + 25 >= crashx22 and crashy11 <= crashy22 and crashy11 + 55 >= crashy22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    
        
# Funcion Fighter
def Fighter1():
    """
    Función para que el carro fighter persiga al jugador.
    """
    global i,j,k,canvas,equis,f,m,level1,contadorf,contadorf2,f2,l,contadorg,contadorg2,x,y,puntoss,puntoss2,w,w2
    equis = random.uniform(0,100)
    if(contadorf < 147):
        contadorf = contadorf + 1
        if(i < 144):
            canvas.delete(f)
            j = j + 2.5
            f = canvas.create_image(200+i/2.5,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.5
            f = canvas.create_image(200+i/2.5,0+j,image=fighter)
        if(i > -22):
            canvas.delete(f)
            j = j + 2.5
            f = canvas.create_image(200+i/2.5,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.5
            f = canvas.create_image(200+i/2.5,0+j,image=fighter)
        if(contadorf >= 147):
            canvas.delete(f)
            contadorf = 0
            j = 0
            f = canvas.create_image(200+i,0,image=fighter)

    if(contadorf2 < 147):
        contadorf2 = contadorf2 + 1
        if(k < 136):
            canvas.delete(f2)
            l = l + 2.5
            f2 = canvas.create_image(820+k/2.5,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.5
            f2 = canvas.create_image(820+k/2.5,0+j,image=fighter2)
        if(k > -25):
            canvas.delete(f2)
            l = l + 2.5
            f2 = canvas.create_image(820+k/2.5,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.5
            f2 = canvas.create_image(820+k/2.5,0+j,image=fighter2)
        if(contadorf >= 147):
            canvas.delete(f2)
            contadorf2 = 0
            l = 0
            f2 = canvas.create_image(820+k,0,image=fighter2)
    
    canvas.after(30,Fighter1)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashfx2=canvas.coords(f)[0]
    crashfy2=canvas.coords(f)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashfx22=canvas.coords(f2)[0]
    crashfy22=canvas.coords(f2)[1]
    
    if(crashx1 >= crashfx2 and crashx1 <= crashfx2 + 25 and crashy1 >= crashfy2 and crashy1 <= crashfy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashfx2 and crashx1 + 25 >= crashfx2 and crashy1 <= crashfy2 and crashy1 + 55 >= crashfy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashfx22 and crashx11 <= crashfx22 + 25 and crashy11 >= crashfy22 and crashy11 <= crashfy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(f2)
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        puntoss2 = 98
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashfx22 and crashx11 + 25 >= crashfx22 and crashy11 <= crashfy22 and crashy11 + 55 >= crashfy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(f2)
        puntoss2 = 98
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
        

# Funcion gasolinabonus
def GasolinaBonus():
    """
    Función para hacer que aparezca el tanque de gasolina.
    """
    global gas,canvas,contadorgaso,contadorgaso2,equis,gas2,gasol,gasol2,x,y,contadorg,contadorg2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66
    equis = random.uniform(0,100)
    if(contadorgaso < 1000):
        canvas.move(gas,0,4)
        contadorgaso = contadorgaso + 1
    if(contadorgaso2 < 1000):
        canvas.move(gas2,0,4)
        contadorgaso2 = contadorgaso2 + 1
    if(contadorgaso == 1000):
        contadorgaso = 0
        canvas.delete(gas)
        gas = canvas.create_image(200+equis,0,image=gasol)
    if(contadorgaso2 == 1000):
        contadorgaso2 = 0
        canvas.delete(gas2)
        gas2 = canvas.create_image(820+equis,0,image=gasol2)
    canvas.after(20,GasolinaBonus)
    
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashgx2=canvas.coords(gas)[0]
    crashgy2=canvas.coords(gas)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashgx22=canvas.coords(gas2)[0]
    crashgy22=canvas.coords(gas2)[1]
    
    if(crashx1 >= crashgx2 and crashx1 <= crashgx2 + 25 and crashy1 >= crashgy2 and crashy1 <= crashgy2 + 55):
        canvas.delete(gas)
        gas = canvas.create_image(200+equis,0,image=gasol)
        contadorgaso = 0
        contadorg = contadorg + 10
        if(contadorg >=41 and contadorg <= 60):
            g6 = canvas.create_image(510,245,image=gasolina6)
        
        if(contadorg >=31 and contadorg <= 50):
            g5 = canvas.create_image(500,245,image=gasolina5)
        
        if(contadorg >=21 and contadorg <= 40):
            g4 = canvas.create_image(490,245,image=gasolina4)
      
        if(contadorg >=11 and contadorg <= 30):
            g3 = canvas.create_image(480,245,image=gasolina3)
     
        if(contadorg >=1 and contadorg <= 20):
            g2 = canvas.create_image(470,245,image=gasolina2)
        


    if(crashx1 <= crashgx2 and crashx1 + 25 >= crashgx2 and crashy1 <= crashgy2 and crashy1 + 55 >= crashgy2):
        canvas.delete(gas)
        gas = canvas.create_image(200+equis,0,image=gasol)
        contadorgaso = 0
        contadorg = contadorg + 10
        if(contadorg >=41 and contadorg <= 60):
            g6 = canvas.create_image(510,245,image=gasolina6)
        
        if(contadorg >=31 and contadorg <= 50):
            g5 = canvas.create_image(500,245,image=gasolina5)
        
        if(contadorg >=21 and contadorg <= 40):
            g4 = canvas.create_image(490,245,image=gasolina4)
      
        if(contadorg >=11 and contadorg <= 30):
            g3 = canvas.create_image(480,245,image=gasolina3)
     
        if(contadorg >=1 and contadorg <= 20):
            g2 = canvas.create_image(470,245,image=gasolina2)

            
    if(crashx11 >= crashgx22 and crashx11 <= crashgx22 + 25 and crashy11 >= crashgy22 and crashy11 <= crashgy22 + 55):
        canvas.delete(gas2)
        gas2 = canvas.create_image(795+equis,0,image=gasol2)
        contadorgaso2 = 0
        contadorg2 = contadorg2 + 10
        if(contadorg2 >=41 and contadorg2 <= 60):
            g11 = canvas.create_image(606,545,image=gasolina11)
        
        if(contadorg2 >=31 and contadorg2 <= 50):
            g22 = canvas.create_image(616,545,image=gasolina22)
        
        if(contadorg2 >=21 and contadorg2 <= 40):
            g33 = canvas.create_image(626,545,image=gasolina33)
      
        if(contadorg2 >=11 and contadorg2 <= 30):
            g44 = canvas.create_image(636,545,image=gasolina44)
     
        if(contadorg2 >=1 and contadorg2 <= 20):
            g55 = canvas.create_image(646,545,image=gasolina55)

            
    if(crashx11 <= crashgx22 and crashx11 + 25 >= crashgx22 and crashy11 <= crashgy22 and crashy11 + 55 >= crashgy22):
        canvas.delete(gas2)
        gas2 = canvas.create_image(795+equis,0,image=gasol2)
        contadorgaso2 = 0
        contadorg2 = contadorg2 + 10
        if(contadorg2 >=41 and contadorg2 <= 60):
            g11 = canvas.create_image(606,545,image=gasolina11)
        
        if(contadorg2 >=31 and contadorg2 <= 50):
            g22 = canvas.create_image(616,545,image=gasolina22)
        
        if(contadorg2 >=21 and contadorg2 <= 40):
            g33 = canvas.create_image(626,545,image=gasolina33)
      
        if(contadorg2 >=11 and contadorg2 <= 30):
            g44 = canvas.create_image(636,545,image=gasolina44)
     
        if(contadorg2 >=1 and contadorg2 <= 20):
            g55 = canvas.create_image(646,545,image=gasolina55)

            
    
# Funcion aceite
def Aceite():
    """
    Función que hace que salga una mancha de aceite aleatoriamente.
    """
    global ac,canvas,contadoraceite,contadoraceite2,equis,ac2,x,y,contadorg,contadorg2,puntoss,puntoss2
    equis = random.uniform(0,100)
    if(contadoraceite < 800):
        canvas.move(ac,0,5)
        contadoraceite = contadoraceite + 1
    if(contadoraceite < 800):
        canvas.move(ac2,0,5)
        contadoraceite2 = contadoraceite2 + 1
    if(contadoraceite == 800):
        ac = canvas.create_image(200+equis,0,image=aceite)
        contadoraceite = 0
    if(contadoraceite == 800):
        contadoraceite2 = 0
        ac2 = canvas.create_image(820+equis,0,image=aceite2)
    canvas.after(5,Aceite)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashacx2=canvas.coords(ac)[0]
    crashacy2=canvas.coords(ac)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashacx22=canvas.coords(ac2)[0]
    crashacy22=canvas.coords(ac2)[1]
    
    if(crashx1 >= crashacx2 and crashx1 <= crashacx2 + 25 and crashy1 >= crashacy2 and crashy1 <= crashacy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(ac)
        ac = canvas.create_image(200+equis,0,image=aceite)
        contadoraceite = 0
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashacx2 and crashx1 + 25 >= crashacx2 and crashy1 <= crashacy2 and crashy1 + 55 >= crashacy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(ac)
        ac = canvas.create_image(200+equis,0,image=aceite)
        contadoraceite = 0
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashacx22 and crashx11 <= crashacx22 + 25 and crashy11 >= crashacy22 and crashy11 <= crashacy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(ac2)
        ac2 = canvas.create_image(795+equis,0,image=aceite2)
        contadoraceite2 = 0
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashacx22 and crashx11 + 25 >= crashacx22 and crashy11 <= crashacy22 and crashy11 + 55 >= crashacy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(ac2)
        ac2 = canvas.create_image(795+equis,0,image=aceite2)
        contadoraceite2 = 0
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])

    
puntoss = 0
puntoss2 = 0
# Funcion puntos
def Puntos():
    """
    Función para mostrar el kilometraje.
    """
    global canvas,puntoss,puntoss2,score,score2,scorer,scorer2
    if(puntoss >= 0):
        score.set(str(puntoss))
        puntoss = puntoss + 1
    if(puntoss >= 180):
        score.set(str(puntoss))
        puntoss = puntoss - 1
    if(puntoss2 >= 0):
        score2.set(str(puntoss2))
        puntoss2 = puntoss2 + 1
    if(puntoss2 >= 180):
        score2.set(str(puntoss2))
        puntoss2 = puntoss2 - 1
    canvas.after(30,Puntos)

# Funcion de la gasolina
def Gasolina():
    """
    Función para mostrar la gasolina del jugador.
    """
    global contadorg,contadorg2,canvas,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,win,lose,r,r2,m,m2,f,f2,ac,ac2,gas,gas2,x,y,contador,puntoss,puntoss2
    if(contadorg > 0):
        contadorg = contadorg - 1
    if(contadorg2 > 0):
        contadorg2 = contadorg2 - 1
    canvas.after(1000,Gasolina)
    if(contadorg <= 50):
        canvas.delete(g6)
    if(contadorg2 <= 50):
        canvas.delete(g11)
    if(contadorg <= 40):
        canvas.delete(g5)
    if(contadorg2 <= 40):
        canvas.delete(g22)
    if(contadorg <= 30):
        canvas.delete(g4)
    if(contadorg2 <= 30):
        canvas.delete(g33)
    if(contadorg <= 20):
        canvas.delete(g3)
    if(contadorg2 <= 20):
        canvas.delete(g44)
    if(contadorg <= 10):
        canvas.delete(g2)
    if(contadorg2 <= 10):
        canvas.delete(g55)
    if(contadorg <= 0):
        canvas.delete(g1)
        if(contadorg <= 0 and contadorg2 >= 1):
            wi = canvas.create_image(850,400,image=win)
            canvas.lift(wi)
            lo = canvas.create_image(250,400,image=lose)
            canvas.lift(lo)
           
            canvas.after(100,Gasolina)
            
    if(contadorg2 <= 0):
        canvas.delete(g66)
        if(contadorg2 <= 0 and contadorg >= 1):
            wi = canvas.create_image(250,400,image=win)
            canvas.lift(wi)
            lo = canvas.create_image(850,400,image=lose)
            canvas.lift(lo)
            
            canvas.after(100,Gasolina)
         



###################################################################################  LVL 2   #########################################################################
def Level2():
    """
    Nivel 2 de Traffic Road Racing
    """
    global level1,canvas,nivel2,nivel22,w,x,y,m,k,f,r,contador,m2,w2,r2,f2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,gas,equis,ac,gas2,ac2,ply1,ply2,puntoss,puntoss2
    level1 = tkinter.Toplevel(vt)
    vt.iconify()
    level1.geometry("1200x1000")
    canvas = tkinter.Canvas(level1, width=1500, height=780,bg="black")
    w = canvas.create_image(250,400,image=nivel2)
    w2 = canvas.create_image(850,400,image=nivel22)
    canvas.lower(w)
    canvas.lower(w2)
    canvas.bind("<Key>", key)
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()
    carretera()
    key()
    # Estados de los jugadores
    p1 = tkinter.Label(canvas,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=50)
    km1 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=130)
    fuel1 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=210)
    p2 = tkinter.Label(canvas,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=580,y=350)
    km2 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=600,y=430)
    fuel2 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=616,y=510)
    # Cargar imagenes de carros
    x = canvas.create_image(200,620,image=player01)
    y = canvas.create_image(795,620,image=player02)
    f = canvas.create_image(200,0,image=fighter)
    f2 = canvas.create_image(820,0,image=fighter2)
    m = canvas.create_image(257,0,image=minivan)
    m2 = canvas.create_image(845,0,image=minivan2)
    r = canvas.create_image(200,0,image=runner)
    r2 = canvas.create_image(800,0,image=runner2)
    # Cargar imagen vidas(gasolina)
    g1 = canvas.create_image(460,245,image=gasolina1)
    g2 = canvas.create_image(470,245,image=gasolina2)
    g3 = canvas.create_image(480,245,image=gasolina3)
    g4 = canvas.create_image(490,245,image=gasolina4)
    g5 = canvas.create_image(500,245,image=gasolina5)
    g6 = canvas.create_image(510,245,image=gasolina6)

    g11 = canvas.create_image(606,545,image=gasolina11)
    g22 = canvas.create_image(616,545,image=gasolina22)
    g33 = canvas.create_image(626,545,image=gasolina33)
    g44 = canvas.create_image(636,545,image=gasolina44)
    g55 = canvas.create_image(646,545,image=gasolina55)
    g66 = canvas.create_image(656,545,image=gasolina66)

    # Cargar Imagen gasolina
    gas = canvas.create_image(230,0,image=gasol)
    gas2 = canvas.create_image(820,0,image=gasol2)

    # Cargar Imagen aceite
    ac = canvas.create_image(200+equis,0,image=aceite)
    ac2 = canvas.create_image(820+equis,0,image=aceite2)

    # Nombres de los jugadores en el juego
    jugador1 = tkinter.Label(canvas,textvariable=ply1,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=75)
    jugador2 = tkinter.Label(canvas,textvariable=ply2,font=("Minecraft",11), fg="white", bg="black").place(x=540,y=375)

    # kilometraje
    scorer = tkinter.Label(canvas,textvariable=score,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=155)
    scorer2 = tkinter.Label(canvas,textvariable=score2,font=("Minecraft",11), fg="white", bg="black").place(x=570,y=455)
    kilo = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=495,y=155)
    kilo2 = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=610,y=455)
    
    # Funciones
    Minivan2()
    Fighter2()
    Runner1()
    Gasolina()
    GasolinaBonus()
    Aceite()
    Puntos()

    

# Funcion Minivan 
def Minivan2():
    """
    Función para hacer que el carro minivan siempre vaya en un carril.
    """
    global canvas,m,m2,i,k,x,j,y,equis,f,explosion,contadorg,contadorg2,contadorm,contadorm2,puntoss,puntoss2,w,w2,contador
    equis = random.uniform(0,100)
    if(contadorm < 170):
        canvas.move(m,0,5.5)
        contadorm = contadorm + 1
    if(contadorm2 < 170):
        canvas.move(m2,0,5.5)
        contadorm2 = contadorm2 + 1
    if(contadorm == 170):
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
    if(contadorm2 == 170):
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
    canvas.after(30,Minivan2)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashx2=canvas.coords(m)[0]
    crashy2=canvas.coords(m)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashx22=canvas.coords(m2)[0]
    crashy22=canvas.coords(m2)[1]
    
    if(crashx1 >= crashx2 and crashx1 <= crashx2 + 25 and crashy1 >= crashy2 and crashy1 <= crashy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashx2 and crashx1 + 25 >= crashx2 and crashy1 <= crashy2 and crashy1 + 55 >= crashy2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashx22 and crashx11 <= crashx22 + 25 and crashy11 >= crashy22 and crashy11 <= crashy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashx22 and crashx11 + 25 >= crashx22 and crashy11 <= crashy22 and crashy11 + 55 >= crashy22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    
        
# Funcion Fighter
def Fighter2():
    """
    Función para que el carro fighter persiga al jugador.
    """
    global i,j,k,canvas,equis,f,m,level1,contadorf,contadorf2,f2,l,contadorg,contadorg2,x,y,puntoss,puntoss2,w,w2
    equis = random.uniform(0,100)
    if(contadorf < 147):
        contadorf = contadorf + 1
        if(i < 144):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2.2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2.2,0+j,image=fighter)
        if(i > -22):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2.2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2.2,0+j,image=fighter)
        if(contadorf >= 147):
            canvas.delete(f)
            contadorf = 0
            j = 0
            f = canvas.create_image(200+i,0,image=fighter)

    if(contadorf2 < 147):
        contadorf2 = contadorf2 + 1
        if(k < 136):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2.2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2.2,0+j,image=fighter2)
        if(k > -25):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2.2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2.2,0+j,image=fighter2)
        if(contadorf >= 147):
            canvas.delete(f2)
            contadorf2 = 0
            l = 0
            f2 = canvas.create_image(820+k,0,image=fighter2)
    
    canvas.after(30,Fighter2)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashfx2=canvas.coords(f)[0]
    crashfy2=canvas.coords(f)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashfx22=canvas.coords(f2)[0]
    crashfy22=canvas.coords(f2)[1]
    
    if(crashx1 >= crashfx2 and crashx1 <= crashfx2 + 25 and crashy1 >= crashfy2 and crashy1 <= crashfy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashfx2 and crashx1 + 25 >= crashfx2 and crashy1 <= crashfy2 and crashy1 + 55 >= crashfy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashfx22 and crashx11 <= crashfx22 + 25 and crashy11 >= crashfy22 and crashy11 <= crashfy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(f2)
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        puntoss2 = 98
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashfx22 and crashx11 + 25 >= crashfx22 and crashy11 <= crashfy22 and crashy11 + 55 >= crashfy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(f2)
        puntoss2 = 98
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
        

#################################################################### LVL 3 ##########################################################################################


def Level3():
    """
    Nivel 3 de Traffic Road Racing
    """
    global level1,canvas,nivel3,nivel33,w,x,y,m,k,f,r,contador,m2,w2,r2,f2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,gas,equis,ac,gas2,ac2,ply1,ply2,puntoss,puntoss2
    level1 = tkinter.Toplevel(vt)
    vt.iconify()
    level1.geometry("1200x1000")
    canvas = tkinter.Canvas(level1, width=1500, height=780,bg="black")
    w = canvas.create_image(250,400,image=nivel3)
    w2 = canvas.create_image(850,400,image=nivel33)
    canvas.lower(w)
    canvas.lower(w2)
    canvas.bind("<Key>", key)
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()
    carretera()
    key()
    # Estados de los jugadores
    p1 = tkinter.Label(canvas,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=50)
    km1 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=130)
    fuel1 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=210)
    p2 = tkinter.Label(canvas,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=580,y=350)
    km2 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=600,y=430)
    fuel2 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=616,y=510)
    # Cargar imagenes de carros
    x = canvas.create_image(200,620,image=player01)
    y = canvas.create_image(795,620,image=player02)
    f = canvas.create_image(200,0,image=fighter)
    f2 = canvas.create_image(820,0,image=fighter2)
    m = canvas.create_image(257,0,image=minivan)
    m2 = canvas.create_image(845,0,image=minivan2)
    r = canvas.create_image(200,0,image=runner)
    r2 = canvas.create_image(800,0,image=runner2)
    # Cargar imagen vidas(gasolina)
    g1 = canvas.create_image(460,245,image=gasolina1)
    g2 = canvas.create_image(470,245,image=gasolina2)
    g3 = canvas.create_image(480,245,image=gasolina3)
    g4 = canvas.create_image(490,245,image=gasolina4)
    g5 = canvas.create_image(500,245,image=gasolina5)
    g6 = canvas.create_image(510,245,image=gasolina6)

    g11 = canvas.create_image(606,545,image=gasolina11)
    g22 = canvas.create_image(616,545,image=gasolina22)
    g33 = canvas.create_image(626,545,image=gasolina33)
    g44 = canvas.create_image(636,545,image=gasolina44)
    g55 = canvas.create_image(646,545,image=gasolina55)
    g66 = canvas.create_image(656,545,image=gasolina66)

    # Cargar Imagen gasolina
    gas = canvas.create_image(230,0,image=gasol)
    gas2 = canvas.create_image(820,0,image=gasol2)

    # Cargar Imagen aceite
    ac = canvas.create_image(200+equis,0,image=aceite)
    ac2 = canvas.create_image(820+equis,0,image=aceite2)

    # Nombres de los jugadores en el juego
    jugador1 = tkinter.Label(canvas,textvariable=ply1,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=75)
    jugador2 = tkinter.Label(canvas,textvariable=ply2,font=("Minecraft",11), fg="white", bg="black").place(x=540,y=375)

    # kilometraje
    scorer = tkinter.Label(canvas,textvariable=score,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=155)
    scorer2 = tkinter.Label(canvas,textvariable=score2,font=("Minecraft",11), fg="white", bg="black").place(x=570,y=455)
    kilo = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=495,y=155)
    kilo2 = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=610,y=455)
    
    # Funciones
    Minivan3()
    Fighter3()
    Runner1()
    Gasolina()
    GasolinaBonus()
    Aceite()
    Puntos()


# Funcion Minivan
def Minivan3():
    """
    Función para hacer que el carro minivan siempre vaya en un carril.
    """
    global canvas,m,m2,i,k,x,j,y,equis,f,explosion,contadorg,contadorg2,contadorm,contadorm2,puntoss,puntoss2,w,w2,contador
    equis = random.uniform(0,100)
    if(contadorm < 170):
        canvas.move(m,0,5.5)
        contadorm = contadorm + 1
    if(contadorm2 < 170):
        canvas.move(m2,0,5.5)
        contadorm2 = contadorm2 + 1
    if(contadorm == 170):
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
    if(contadorm2 == 170):
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
    canvas.after(25,Minivan3)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashx2=canvas.coords(m)[0]
    crashy2=canvas.coords(m)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashx22=canvas.coords(m2)[0]
    crashy22=canvas.coords(m2)[1]
    
    if(crashx1 >= crashx2 and crashx1 <= crashx2 + 25 and crashy1 >= crashy2 and crashy1 <= crashy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashx2 and crashx1 + 25 >= crashx2 and crashy1 <= crashy2 and crashy1 + 55 >= crashy2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashx22 and crashx11 <= crashx22 + 25 and crashy11 >= crashy22 and crashy11 <= crashy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashx22 and crashx11 + 25 >= crashx22 and crashy11 <= crashy22 and crashy11 + 55 >= crashy22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    
        
# Funcion Fighter
def Fighter3():
    """
    Función para que el carro fighter persiga al jugador.
    """
    global i,j,k,canvas,equis,f,m,level1,contadorf,contadorf2,f2,l,contadorg,contadorg2,x,y,puntoss,puntoss2,w,w2
    equis = random.uniform(0,100)
    if(contadorf < 147):
        contadorf = contadorf + 1
        if(i < 144):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2,0+j,image=fighter)
        if(i > -22):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/2,0+j,image=fighter)
        if(contadorf >= 147):
            canvas.delete(f)
            contadorf = 0
            j = 0
            f = canvas.create_image(200+i,0,image=fighter)

    if(contadorf2 < 147):
        contadorf2 = contadorf2 + 1
        if(k < 136):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2,0+j,image=fighter2)
        if(k > -25):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/2,0+j,image=fighter2)
        if(contadorf >= 147):
            canvas.delete(f2)
            contadorf2 = 0
            l = 0
            f2 = canvas.create_image(820+k,0,image=fighter2)
    
    canvas.after(25,Fighter3)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashfx2=canvas.coords(f)[0]
    crashfy2=canvas.coords(f)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashfx22=canvas.coords(f2)[0]
    crashfy22=canvas.coords(f2)[1]
    
    if(crashx1 >= crashfx2 and crashx1 <= crashfx2 + 25 and crashy1 >= crashfy2 and crashy1 <= crashfy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashfx2 and crashx1 + 25 >= crashfx2 and crashy1 <= crashfy2 and crashy1 + 55 >= crashfy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashfx22 and crashx11 <= crashfx22 + 25 and crashy11 >= crashfy22 and crashy11 <= crashfy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(f2)
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        puntoss2 = 98
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashfx22 and crashx11 + 25 >= crashfx22 and crashy11 <= crashfy22 and crashy11 + 55 >= crashfy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(f2)
        puntoss2 = 98
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])



################################################################ LVL 4 #################################################################################################


def Level4():
    """
    Nivel 4 de Traffic Road Racing
    """
    global level1,canvas,nivel4,nivel44,w,x,y,m,k,f,r,contador,m2,w2,r2,f2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,gas,equis,ac,gas2,ac2,ply1,ply2,puntoss,puntoss2
    level1 = tkinter.Toplevel(vt)
    vt.iconify()
    level1.geometry("1200x1000")
    canvas = tkinter.Canvas(level1, width=1500, height=780,bg="black")
    w = canvas.create_image(250,400,image=nivel4)
    w2 = canvas.create_image(850,400,image=nivel44)
    canvas.lower(w)
    canvas.lower(w2)
    canvas.bind("<Key>", key)
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()
    carretera()
    key()
    # Estados de los jugadores
    p1 = tkinter.Label(canvas,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=50)
    km1 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=130)
    fuel1 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=210)
    p2 = tkinter.Label(canvas,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=580,y=350)
    km2 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=600,y=430)
    fuel2 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=616,y=510)
    # Cargar imagenes de carros
    x = canvas.create_image(200,620,image=player01)
    y = canvas.create_image(795,620,image=player02)
    f = canvas.create_image(200,0,image=fighter)
    f2 = canvas.create_image(820,0,image=fighter2)
    m = canvas.create_image(257,0,image=minivan)
    m2 = canvas.create_image(845,0,image=minivan2)
    r = canvas.create_image(200,0,image=runner)
    r2 = canvas.create_image(800,0,image=runner2)
    # Cargar imagen vidas(gasolina)
    g1 = canvas.create_image(460,245,image=gasolina1)
    g2 = canvas.create_image(470,245,image=gasolina2)
    g3 = canvas.create_image(480,245,image=gasolina3)
    g4 = canvas.create_image(490,245,image=gasolina4)
    g5 = canvas.create_image(500,245,image=gasolina5)
    g6 = canvas.create_image(510,245,image=gasolina6)

    g11 = canvas.create_image(606,545,image=gasolina11)
    g22 = canvas.create_image(616,545,image=gasolina22)
    g33 = canvas.create_image(626,545,image=gasolina33)
    g44 = canvas.create_image(636,545,image=gasolina44)
    g55 = canvas.create_image(646,545,image=gasolina55)
    g66 = canvas.create_image(656,545,image=gasolina66)

    # Cargar Imagen gasolina
    gas = canvas.create_image(230,0,image=gasol)
    gas2 = canvas.create_image(820,0,image=gasol2)

    # Cargar Imagen aceite
    ac = canvas.create_image(200+equis,0,image=aceite)
    ac2 = canvas.create_image(820+equis,0,image=aceite2)

    # Nombres de los jugadores en el juego
    jugador1 = tkinter.Label(canvas,textvariable=ply1,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=75)
    jugador2 = tkinter.Label(canvas,textvariable=ply2,font=("Minecraft",11), fg="white", bg="black").place(x=540,y=375)

    # kilometraje
    scorer = tkinter.Label(canvas,textvariable=score,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=155)
    scorer2 = tkinter.Label(canvas,textvariable=score2,font=("Minecraft",11), fg="white", bg="black").place(x=570,y=455)
    kilo = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=495,y=155)
    kilo2 = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=610,y=455)
    
    # Funciones
    Minivan4()
    Fighter4()
    Runner1()
    Gasolina()
    GasolinaBonus()
    Aceite()
    Puntos()


# Funcion Minivan
def Minivan4():
    """
    Función para hacer que el carro minivan siempre vaya en un carril.
    """
    global canvas,m,m2,i,k,x,j,y,equis,f,explosion,contadorg,contadorg2,contadorm,contadorm2,puntoss,puntoss2,w,w2,contador
    equis = random.uniform(0,100)
    if(contadorm < 170):
        canvas.move(m,0,5.5)
        contadorm = contadorm + 1
    if(contadorm2 < 170):
        canvas.move(m2,0,5.5)
        contadorm2 = contadorm2 + 1
    if(contadorm == 170):
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
    if(contadorm2 == 170):
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
    canvas.after(20,Minivan4)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashx2=canvas.coords(m)[0]
    crashy2=canvas.coords(m)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashx22=canvas.coords(m2)[0]
    crashy22=canvas.coords(m2)[1]
    
    if(crashx1 >= crashx2 and crashx1 <= crashx2 + 25 and crashy1 >= crashy2 and crashy1 <= crashy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashx2 and crashx1 + 25 >= crashx2 and crashy1 <= crashy2 and crashy1 + 55 >= crashy2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashx22 and crashx11 <= crashx22 + 25 and crashy11 >= crashy22 and crashy11 <= crashy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashx22 and crashx11 + 25 >= crashx22 and crashy11 <= crashy22 and crashy11 + 55 >= crashy22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    
        
# Funcion Fighter
def Fighter4():
    """
    Función para que el carro fighter persiga al jugador.
    """
    global i,j,k,canvas,equis,f,m,level1,contadorf,contadorf2,f2,l,contadorg,contadorg2,x,y,puntoss,puntoss2,w,w2
    equis = random.uniform(0,100)
    if(contadorf < 147):
        contadorf = contadorf + 1
        if(i < 144):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.8,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.8,0+j,image=fighter)
        if(i > -22):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.8,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.8,0+j,image=fighter)
        if(contadorf >= 147):
            canvas.delete(f)
            contadorf = 0
            j = 0
            f = canvas.create_image(200+i,0,image=fighter)

    if(contadorf2 < 147):
        contadorf2 = contadorf2 + 1
        if(k < 136):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.8,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.8,0+j,image=fighter2)
        if(k > -25):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.8,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.8,0+j,image=fighter2)
        if(contadorf >= 147):
            canvas.delete(f2)
            contadorf2 = 0
            l = 0
            f2 = canvas.create_image(820+k,0,image=fighter2)
    
    canvas.after(20,Fighter4)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashfx2=canvas.coords(f)[0]
    crashfy2=canvas.coords(f)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashfx22=canvas.coords(f2)[0]
    crashfy22=canvas.coords(f2)[1]
    
    if(crashx1 >= crashfx2 and crashx1 <= crashfx2 + 25 and crashy1 >= crashfy2 and crashy1 <= crashfy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashfx2 and crashx1 + 25 >= crashfx2 and crashy1 <= crashfy2 and crashy1 + 55 >= crashfy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashfx22 and crashx11 <= crashfx22 + 25 and crashy11 >= crashfy22 and crashy11 <= crashfy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(f2)
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        puntoss2 = 98
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashfx22 and crashx11 + 25 >= crashfx22 and crashy11 <= crashfy22 and crashy11 + 55 >= crashfy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(f2)
        puntoss2 = 98
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])


############################################################################## LVL5 ###################################################################################

def Level5():
    """
    Nivel 5 de Traffic Road Racing
    """
    global level1,canvas,nivel5,nivel55,w,x,y,m,k,f,r,contador,m2,w2,r2,f2,g1,g11,g2,g22,g3,g33,g4,g44,g5,g55,g6,g66,gas,equis,ac,gas2,ac2,ply1,ply2,puntoss,puntoss2
    level1 = tkinter.Toplevel(vt)
    vt.iconify()
    level1.geometry("1200x1000")
    canvas = tkinter.Canvas(level1, width=1500, height=780,bg="black")
    w = canvas.create_image(250,400,image=nivel5)
    w2 = canvas.create_image(850,400,image=nivel55)
    canvas.lower(w)
    canvas.lower(w2)
    canvas.bind("<Key>", key)
    canvas.bind("<KeyPress>", keydown)
    canvas.bind("<KeyRelease>", keyup)
    canvas.pack()
    canvas.focus_set()
    carretera()
    key()
    # Estados de los jugadores
    p1 = tkinter.Label(canvas,text="Player 1",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=50)
    km1 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=130)
    fuel1 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=450,y=210)
    p2 = tkinter.Label(canvas,text="Player 2",font=("Minecraft",11), fg="white", bg="black").place(x=580,y=350)
    km2 = tkinter.Label(canvas,text="Score",font=("Minecraft",11), fg="white", bg="black").place(x=600,y=430)
    fuel2 = tkinter.Label(canvas,text="Fuel",font=("Minecraft",11), fg="white", bg="black").place(x=616,y=510)
    # Cargar imagenes de carros
    x = canvas.create_image(200,620,image=player01)
    y = canvas.create_image(795,620,image=player02)
    f = canvas.create_image(200,0,image=fighter)
    f2 = canvas.create_image(820,0,image=fighter2)
    m = canvas.create_image(257,0,image=minivan)
    m2 = canvas.create_image(845,0,image=minivan2)
    r = canvas.create_image(200,0,image=runner)
    r2 = canvas.create_image(800,0,image=runner2)
    # Cargar imagen vidas(gasolina)
    g1 = canvas.create_image(460,245,image=gasolina1)
    g2 = canvas.create_image(470,245,image=gasolina2)
    g3 = canvas.create_image(480,245,image=gasolina3)
    g4 = canvas.create_image(490,245,image=gasolina4)
    g5 = canvas.create_image(500,245,image=gasolina5)
    g6 = canvas.create_image(510,245,image=gasolina6)

    g11 = canvas.create_image(606,545,image=gasolina11)
    g22 = canvas.create_image(616,545,image=gasolina22)
    g33 = canvas.create_image(626,545,image=gasolina33)
    g44 = canvas.create_image(636,545,image=gasolina44)
    g55 = canvas.create_image(646,545,image=gasolina55)
    g66 = canvas.create_image(656,545,image=gasolina66)

    # Cargar Imagen gasolina
    gas = canvas.create_image(230,0,image=gasol)
    gas2 = canvas.create_image(820,0,image=gasol2)

    # Cargar Imagen aceite
    ac = canvas.create_image(200+equis,0,image=aceite)
    ac2 = canvas.create_image(820+equis,0,image=aceite2)

    # Nombres de los jugadores en el juego
    jugador1 = tkinter.Label(canvas,textvariable=ply1,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=75)
    jugador2 = tkinter.Label(canvas,textvariable=ply2,font=("Minecraft",11), fg="white", bg="black").place(x=540,y=375)

    # kilometraje
    scorer = tkinter.Label(canvas,textvariable=score,font=("Minecraft",11), fg="white", bg="black").place(x=450,y=155)
    scorer2 = tkinter.Label(canvas,textvariable=score2,font=("Minecraft",11), fg="white", bg="black").place(x=570,y=455)
    kilo = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=495,y=155)
    kilo2 = tkinter.Label(canvas,text="Km/h",font=("Minecraft",11), fg="white", bg="black").place(x=610,y=455)
    
    # Funciones
    Minivan4()
    Fighter4()
    Runner1()
    Gasolina()
    GasolinaBonus()
    Aceite()
    Puntos()

 
# Funcion Minivan
def Minivan5():
    """
    Función para hacer que el carro minivan siempre vaya en un carril.
    """
    global canvas,m,m2,i,k,x,j,y,equis,f,explosion,contadorg,contadorg2,contadorm,contadorm2,puntoss,puntoss2,w,w2,contador
    equis = random.uniform(0,100)
    if(contadorm < 170):
        canvas.move(m,0,7)
        contadorm = contadorm + 1
    if(contadorm2 < 170):
        canvas.move(m2,0,7)
        contadorm2 = contadorm2 + 1
    if(contadorm == 170):
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
    if(contadorm2 == 170):
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
    canvas.after(9,Minivan5)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashx2=canvas.coords(m)[0]
    crashy2=canvas.coords(m)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashx22=canvas.coords(m2)[0]
    crashy22=canvas.coords(m2)[1]
    
    if(crashx1 >= crashx2 and crashx1 <= crashx2 + 25 and crashy1 >= crashy2 and crashy1 <= crashy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashx2 and crashx1 + 25 >= crashx2 and crashy1 <= crashy2 and crashy1 + 55 >= crashy2):
        canvas.delete(x)
        x = canvas.create_image(200+i,620,image=vol1)
        canvas.delete(m)
        m = canvas.create_image(200+equis,0,image=minivan)
        contadorm = 0
        contadorg = contadorg - 10
        puntoss = 98
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashx22 and crashx11 <= crashx22 + 25 and crashy11 >= crashy22 and crashy11 <= crashy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashx22 and crashx11 + 25 >= crashx22 and crashy11 <= crashy22 and crashy11 + 55 >= crashy22):
        canvas.delete(y)
        y = canvas.create_image(795+k,620,image=vol2)
        canvas.delete(m2)
        m2 = canvas.create_image(770+equis,0,image=minivan2)
        contadorm2 = 0
        contadorg2 = contadorg2 - 10
        puntoss2 = 98
        canvas.move(w2,0,-canvas.coords(w2)[1])
    
        
# Funcion Fighter
def Fighter5():
    """
    Función para que el carro fighter persiga al jugador.
    """
    global i,j,k,canvas,equis,f,m,level1,contadorf,contadorf2,f2,l,contadorg,contadorg2,x,y,puntoss,puntoss2,w,w2
    equis = random.uniform(0,100)
    if(contadorf < 147):
        contadorf = contadorf + 1
        if(i < 144):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.2,0+j,image=fighter)
        if(i > -22):
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.2,0+j,image=fighter)
        else:
            canvas.delete(f)
            j = j + 2.8
            f = canvas.create_image(200+i/1.2,0+j,image=fighter)
        if(contadorf >= 147):
            canvas.delete(f)
            contadorf = 0
            j = 0
            f = canvas.create_image(200+i,0,image=fighter)

    if(contadorf2 < 147):
        contadorf2 = contadorf2 + 1
        if(k < 136):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.2,0+j,image=fighter2)
        if(k > -25):
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.2,0+j,image=fighter2)
        else:
            canvas.delete(f2)
            l = l + 2.8
            f2 = canvas.create_image(820+k/1.2,0+j,image=fighter2)
        if(contadorf >= 147):
            canvas.delete(f2)
            contadorf2 = 0
            l = 0
            f2 = canvas.create_image(820+k,0,image=fighter2)
    
    canvas.after(15,Fighter5)
    crashx1=canvas.coords(x)[0]
    crashy1=canvas.coords(x)[1]
    crashfx2=canvas.coords(f)[0]
    crashfy2=canvas.coords(f)[1]
    
    crashx11=canvas.coords(y)[0]
    crashy11=canvas.coords(y)[1]
    crashfx22=canvas.coords(f2)[0]
    crashfy22=canvas.coords(f2)[1]
    
    if(crashx1 >= crashfx2 and crashx1 <= crashfx2 + 25 and crashy1 >= crashfy2 and crashy1 <= crashfy2 + 55):
        canvas.delete(x)
        x = canvas.create_image(240+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx1 <= crashfx2 and crashx1 + 25 >= crashfx2 and crashy1 <= crashfy2 and crashy1 + 55 >= crashfy2):
        canvas.delete(x)
        x = canvas.create_image(160+i,620,image=vol1)
        canvas.delete(f)
        f = canvas.create_image(200+equis,0,image=fighter)
        contadorf = 0
        puntoss = 98
        contadorg = contadorg - 10
        canvas.move(w,0,-canvas.coords(w)[1])
    if(crashx11 >= crashfx22 and crashx11 <= crashfx22 + 25 and crashy11 >= crashfy22 and crashy11 <= crashfy22 + 55):
        canvas.delete(y)
        y = canvas.create_image(835+k,620,image=vol2)
        canvas.delete(f2)
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        puntoss2 = 98
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])
    if(crashx11 <= crashfx22 and crashx11 + 25 >= crashfx22 and crashy11 <= crashfy22 and crashy11 + 55 >= crashfy22):
        canvas.delete(y)
        y = canvas.create_image(755+k,620,image=vol2)
        canvas.delete(f2)
        puntoss2 = 98
        f2 = canvas.create_image(820+equis,0,image=fighter2)
        contadorf2 = 0
        contadorg2 = contadorg2 - 10
        canvas.move(w2,0,-canvas.coords(w2)[1])

# Botones niveles
lvl1 = tkinter.Button(vt,text="Lvl 1",command=Level1, font=("Minecraft",10), fg="white", bg="black").place(x=150,y=320)
lvl2 = tkinter.Button(vt,text="Lvl 2",command=Level2, font=("Minecraft",10), fg="white", bg="black").place(x=210,y=320)
lvl3 = tkinter.Button(vt,text="Lvl 3",command=Level3, font=("Minecraft",10), fg="white", bg="black").place(x=270,y=320)
lvl4 = tkinter.Button(vt,text="Lvl 4",command=Level4, font=("Minecraft",10), fg="white", bg="black").place(x=330,y=320)
lvl5 = tkinter.Button(vt,text="Lvl 5",command=Level5, font=("Minecraft",10), fg="white", bg="black").place(x=390,y=320)
cargar = tkinter.Button(vt,text="Cargar Partida",font=("Minecraft",10), fg="white", bg="black").place(x=230,y=350)
ayuda = tkinter.Button(vt,text="Ayuda",command=Ayuda, font=("Minecraft",10), fg="white", bg="black").place(x=520,y=375)
# Ciclo para escuchar los eventos
vt.mainloop()


