#Crédits:
# Software Engineer : @GaelHF
# https://www.geeksforgeeks.org/
# ~800 lignes de code

#Bibliothèque
import turtle
import tkinter
from sketchpy import canvas
import requests
from PIL import Image
global square
import customtkinter

#Variables
image = open('img.jpg', 'w')
image.close()

t = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
screen.setup(500, 500)
fenetre = tkinter.Tk()

current_Lang = "fr"
current_Color = "black"
current_FillColor = "black"
current_Longeur = 100
current_Cote = 0
current_Toollangages = 0
isFilling = False
current_Text = ""
current_URL = ""
nbr1=0
nbr2=0
answer=0

pos_x = 0
pos_y = 0

t.speed(-1)

#UTILITAIRES
class CalculDeMath():
   def addition(number1, number2):
      return(int(number1) + int(number2))
   def soustraction(number1, number2):
      return(int(number1) - int(number2))
   def multiplication(number1, number2):
      return(int(number1) * int(number2))
   def division(number1, number2):
      return(int(number1) / int(number2))
#FONCTIONS


def nb1():
  #Fait des calculs (1er chiffre)
  nbr = tkinter.Toplevel(fenetre)
  nbr.title("1er chiffre")
  nbr.geometry("300x100")
  canvas1 = tkinter.Canvas(nbr, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(nbr)
  canvas1.create_window(0, 10, window=entry1)

  def change_nbr():
    global nbr1
    if(entry1.get() == "ANS"):
      nbr1 = result
    else:
      nbr1 = int(entry1.get())
    nbr.destroy()
    nb2()

  ChangeButton = tkinter.Button(nbr, text="Entrer", command=change_nbr)
  ChangeButton.pack()


def nb2():
  #Fait des calculs (2e chiffre)
  nbr = tkinter.Toplevel(fenetre)
  nbr.title("2e chiffre")
  nbr.geometry("300x100")
  canvas1 = tkinter.Canvas(nbr, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(nbr)
  canvas1.create_window(0, 10, window=entry1)

  def change_nbr():
    global nbr2
    if(entry1.get() == "ANS"):
      nbr2 = result
    else:
      nbr2 = int(entry1.get())
    nbr.destroy()
    method()

  ChangeButton = tkinter.Button(nbr, text="Entrer", command=change_nbr)
  ChangeButton.pack()


def method():
  #Fait des calculs (method)
  nbr = tkinter.Toplevel(fenetre)
  nbr.title("Méthode")
  nbr.geometry("300x100")
  canvas1 = tkinter.Canvas(nbr, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(nbr)
  canvas1.create_window(0, 10, window=entry1)

  def change_nbr():
    global nbr1
    global nbr2
    global result
    metod = entry1.get()
    if metod == "+":
      result = CalculDeMath.addition(nbr1, nbr2)
    elif metod == "-":
      result = CalculDeMath.soustraction(nbr1, nbr2)
    elif metod == "*":
      result = CalculDeMath.multiplication(nbr1, nbr2)
    elif metod == "/":
      result = CalculDeMath.division(nbr1, nbr2)
    answer = tkinter.Button(nbr, text=result)
    answer.pack()
    entry1.delete(0, 'end')

  ChangeButton = tkinter.Button(nbr, text="Entrer", command=change_nbr)
  ChangeButton.pack()

def grid():
  hauteur = -250
  for i in range(10):
    t.penup()
    t.goto(-250, hauteur)
    t.pendown()
    for i in range(10):
      for i in range(4):
        t.forward(50)
        t.left(90)
      t.forward(50)
    hauteur += 50
  t.goto(0, 0)

def forw():
  #Change la couleur
  forw = tkinter.Toplevel(fenetre)
  forw.title("Forward")
  forw.geometry("300x100")
  canvas1 = tkinter.Canvas(forw, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(forw)
  canvas1.create_window(0, 10, window=entry1)

  def change_forw():
    t.forward(int(entry1.get()))
    forw.destroy()

  ChangeButton = tkinter.Button(forw, text="Changer", command=change_forw)
  ChangeButton.pack()

def backw():
  #Change la couleur
  backw = tkinter.Toplevel(fenetre)
  backw.title("Backward")
  backw.geometry("300x100")
  canvas1 = tkinter.Canvas(backw, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(backw)
  canvas1.create_window(0, 10, window=entry1)

  def change_backw():
    t.backward(int(entry1.get()))
    backw.destroy()

  ChangeButton = tkinter.Button(backw, text="Changer", command=change_backw)
  ChangeButton.pack()

def triangle():
  global isFilling
  #Fait un triangle
  if isFilling == True:
    t.fillcolor(current_FillColor)
    t.begin_fill()
  for i in range(3):
    t.forward(current_Longeur)
    t.left(360 / 3)
  if isFilling == True:
    t.end_fill()

def carre():
  global isFilling
  #Fait un triangle
  if isFilling == True:
    t.fillcolor(current_FillColor)
    t.begin_fill()
  for i in range(4):
    t.forward(current_Longeur)
    t.left(360 / 4)
  if isFilling == True:
    t.end_fill()

def left():
  #Tourne de 45 degrés a gauche
  t.left(45)

def right():
  #Tourne de 45 degrés a droite
  t.right(45)

def reset():
  #Efface tous
  global current_Text
  global current_Color
  global current_FillColor
  global current_Longeur
  global current_Cote
  global current_Toollangages
  global isFilling
  global pos_x
  global pos_y
  global current_Lang
  current_Lang = "fr"
  current_Text = ""
  current_Color = ""
  current_FillColor = ""
  current_Longeur = 100
  current_Cote = 0
  current_Toollangages = 0
  isFilling = False
  pos_x = 0
  pos_y = 0
  t.clear()
  t.reset()

def dot():
  #Fait un point
  t.dot(current_Toollangages)

def circle():
  #Fait un cercle
  t.circle(current_Longeur)

def toggleFill():
  #Changer le mode remplissage
  global isFilling
  if isFilling == True:
    isFilling = False
  elif isFilling == False:
    isFilling = True

def goto():
  #Va sans déssiner
  t.penup()
  t.goto(pos_x, pos_y)
  t.pendown()

def gotoanddraw():
  #Va et déssine
  t.goto(pos_x, pos_y)
  t.pendown()

def color():
  #Change la couleur
  color = tkinter.Toplevel(fenetre)
  color.title("Couleur")
  color.geometry("300x100")
  canvas1 = tkinter.Canvas(color, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(color)
  canvas1.create_window(0, 10, window=entry1)

  def change_color():
    global current_Color
    current_Color = str(entry1.get())
    t.color(current_Color)
    color.destroy()

  ChangeButton = tkinter.Button(color, text="Changer", command=change_color)
  ChangeButton.pack()

def fill_color():
  #Change la couleur
  fill_color = tkinter.Toplevel(fenetre)
  fill_color.title("Couleur de Remplissage")
  fill_color.geometry("300x100")
  canvas1 = tkinter.Canvas(fill_color, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(fill_color)
  canvas1.create_window(0, 10, window=entry1)

  def fill_color_change():
    global current_FillColor
    current_FillColor = str(entry1.get())
    fill_color.destroy()

  ChangeButton = tkinter.Button(fill_color, text="Changer",command=fill_color_change)
  ChangeButton.pack()

def length():
  #Change le longeur
  length = tkinter.Toplevel(fenetre)
  length.title("Longeur")
  length.geometry("300x100")
  canvas1 = tkinter.Canvas(length, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(length)
  canvas1.create_window(0, 10, window=entry1)

  def change_length():
    global current_Longeur
    current_Longeur = int(entry1.get())
    length.destroy()

  ChangeButton = tkinter.Button(length, text="Changer", command=change_length)
  ChangeButton.pack()

def shape():
  #Dessine un forme selon le nombre de cote
  shape = tkinter.Toplevel(fenetre)
  shape.title("Forme")
  shape.geometry("300x100")
  canvas1 = tkinter.Canvas(shape, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(shape)
  canvas1.create_window(0, 10, window=entry1)

  def change_color():
    global current_Cote
    current_Cote = int(entry1.get())
    shape.destroy()
    global current_Longeur
    if isFilling == True:
      t.fillcolor(current_FillColor)
      t.begin_fill()
    for i in range(current_Cote):
      t.forward(current_Longeur)
      t.left(360 / current_Cote)
    if isFilling == True:
      t.end_fill()

  ChangeButton = tkinter.Button(shape, text="Enregistrer", command=change_color)
  ChangeButton.pack()

def rotation():
  #Change la rotation
  t.setheading(0)

def write():
  #Écrit du texte
  write = tkinter.Toplevel(fenetre)
  write.title("Forme")
  write.geometry("300x100")
  canvas1 = tkinter.Canvas(write, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(write)
  canvas1.create_window(0, 10, window=entry1)

  def change_color():
    global current_Text
    current_Text = str(entry1.get())
    write.destroy()
    turtle.write(current_Text, font=("Verdana", 15, "normal"))

  ChangeButton = tkinter.Button(write, text="Écrire", command=change_color)
  ChangeButton.pack()

def dragging(x, y):
  #dessiner en glissant turtle
  t.ondrag(None)
  t.setheading(t.towards(x, y))
  t.goto(x, y)
  t.ondrag(dragging)

def minecraft():
    #fait un dessin de minecraft
    sol = -250
    #Ciel
    def resetPos():
        #Change la positon
        t.penup()
        t.goto(-250, sol)
        t.pendown()
    resetPos()
    t.fillcolor('skyblue')
    t.begin_fill()
    for i in range(4):
        t.forward(500)
        t.left(90)
    t.end_fill()
    
    #Cube de terre
    for i in range(10):
        t.fillcolor((int(160), int(82), int(45)))
        t.begin_fill()
        for i in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.forward(50)
    sol += 50
    
    
    #Cube de Gazon
    resetPos()
    for i in range(10):
        t.fillcolor('green')
        t.begin_fill()
        for i in range(2):
            t.forward(50)
            t.left(90)
            t.forward(12.5)
            t.left(90)
        t.end_fill()
        t.forward(50)
    sol += 12.5
    
    #Tron d'arbre
    for i in range(3):
        resetPos()
        t.penup()
        t.forward(100)
        t.pendown()
        for i in range(3):
            t.fillcolor((200, 173, 127))
            t.begin_fill()
            for i in range(4):
                t.forward(50)
                t.left(90)
            t.end_fill()
            t.penup()
            t.forward(100+50)
            t.pendown()
        sol += 50
    #Feuille d'arbre
    resetPos()
    t.penup()
    t.forward(50)
    t.pendown()
    for i in range(3):
        for i in range(3):
            t.fillcolor('darkgreen')
            t.begin_fill()
            for i in range(4):
                t.forward(50)
                t.left(90)
            t.end_fill()
            t.forward(50)
    sol+=50
    resetPos()
    t.penup()
    t.forward(100)
    t.pendown()
    for i in range(3):
        t.fillcolor('darkgreen')
        t.begin_fill()
        for i in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
        t.forward(150)
    sol+=100
    
    #Nuage et soleil
    resetPos()
    t.penup()
    t.forward(150)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    sol+=50
    resetPos()
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(200)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

    def resetPos():
      #reset la position
      global hauteur
      t.penup()
      t.goto(float(-250.00), float(hauteur))
      t.pendown()
      
    def update_hauteur(haut):
      global hauteur
      #change la hauteur
      hauteur = hauteur+haut

    #Ciel
    resetPos()
    t.fillcolor("skyblue")
    t.begin_fill()
    for i in range(4):
        t.forward(500)
        t.left(90)
    t.end_fill()

    #Sol
    t.width(2.5)
    t.color("#4d2500")
    t.fillcolor("#9e5410")
    for i in range(10):
        t.begin_fill()
        for i in range(2):
            t.forward(50)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()
        t.forward(50)

    #Gazon
    update_hauteur(40)
    resetPos()
    t.width(1.5)
    t.color("#125400")
    t.fillcolor("#27b300")
    for i in range(10):
        t.begin_fill()
        for i in range(2):
            t.forward(50)
            t.left(90)
            t.forward(10)
            t.left(90)
        t.end_fill()
        t.forward(50)

def langages():
  #Change la langue des bouttons
  langages = tkinter.Toplevel(fenetre)
  langages.title("Langages")
  langages.geometry("300x100")
  canvas1 = tkinter.Canvas(langages, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(langages)
  label1 = tkinter.Label(langages, text="FR: Français / EN: English")
  label1.pack()
  canvas1.create_window(0, 10, window=entry1)

  def change_lang():
    global current_Lang
    current_Lang = str(entry1.get())
    if(current_Lang == "FR" or current_Lang == "fr"):
       generate_button_fr()
       main_loop()
    elif(current_Lang == "EN" or current_Lang == "en"):
       generate_button_en()
       main_loop()
  
    langages.destroy()

  ChangeButton = tkinter.Button(langages, text="Changer", command=change_lang)
  ChangeButton.pack()

def draw():
  #Change la couleur
  draw = tkinter.Toplevel(fenetre)
  draw.title("Image")
  draw.geometry("300x100")
  canvas1 = tkinter.Canvas(draw, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(draw)
  canvas1.create_window(0, 10, window=entry1)

  def change_draw():
    global current_URL
    current_URL = entry1.get()
    data = requests.get(current_URL).content
    f = open('img.jpg', 'wb')
    f.write(data)
    f.close()
    draw.destroy()
    img = canvas.sketch_from_image('img.jpg')
    img.draw(threshold = 127, pen = t)

  drawButton = tkinter.Button(draw, text="Dessiner", command=change_draw)
  drawButton.pack()


#Titres
screen.title('Paint.wish')

def generate_button_fr():
  clearCommands()
  fenetre.title("Commandes")
  customtkinter.set_appearance_mode('Dark')
  #Créer les buttons

  credits =customtkinter.CTkLabel(fenetre, text="Créé: Gaël Hébert-Furoy", text_color='black')
  credits.pack(pady=5)

  bdraw = customtkinter.CTkButton(text="Dessiner depuis URL",master=fenetre, corner_radius=10, command=draw)
  bdraw.pack(pady=5, anchor=tkinter.CENTER)

  blang = customtkinter.CTkButton(text="Langage",master=fenetre, corner_radius=10, command=langages)
  blang.pack(pady=5, anchor=tkinter.CENTER)

  bcalc = customtkinter.CTkButton(text="Calculer",master=fenetre, corner_radius=10, command=nb1)
  bcalc.pack(pady=5, anchor=tkinter.CENTER)

  btriangle = customtkinter.CTkButton(text="Triangle",master=fenetre, corner_radius=10, command=triangle)
  btriangle.pack(pady=5, anchor=tkinter.CENTER)

  bsquare = customtkinter.CTkButton(text="Carré",master=fenetre, corner_radius=10, command=carre)
  bsquare.pack(pady=5, anchor=tkinter.CENTER)

  bforw = customtkinter.CTkButton(text="Avancer",master=fenetre, corner_radius=10, command=forw)
  bforw.pack(pady=5, anchor=tkinter.CENTER)

  bbackw = customtkinter.CTkButton(text="Reculer",master=fenetre, corner_radius=10, command=backw)
  bbackw.pack(pady=5, anchor=tkinter.CENTER)

  bleft = customtkinter.CTkButton(text="<--",master=fenetre, corner_radius=10, command=left)
  bleft.pack(pady=5, anchor=tkinter.CENTER)

  bright = customtkinter.CTkButton(text="-->",master=fenetre, corner_radius=10, command=right)
  bright.pack(pady=5, anchor=tkinter.CENTER)

  brot = customtkinter.CTkButton(text="Angle par défaut",master=fenetre, corner_radius=10, command=rotation)
  brot.pack(pady=5, anchor=tkinter.CENTER)

  bgoto = customtkinter.CTkButton(text="Aller à",master=fenetre, corner_radius=10, command=goto)
  bgoto.pack(pady=5, anchor=tkinter.CENTER)

  bgotod = customtkinter.CTkButton(text="Aller à et dessiner",master=fenetre, corner_radius=10, command=gotoanddraw)
  bgotod.pack(pady=5, anchor=tkinter.CENTER)

  bcolor = customtkinter.CTkButton(text="Couleur",master=fenetre, corner_radius=10, command=color)
  bcolor.pack(pady=5, anchor=tkinter.CENTER)

  btoolsize = customtkinter.CTkButton(text="Taille de l'outil",master=fenetre, corner_radius=10, command=length)
  btoolsize.pack(pady=5, anchor=tkinter.CENTER)

  btogglefill = customtkinter.CTkButton(text="Activer/Désactiver Mode Remplissage",master=fenetre, corner_radius=10, command=toggleFill)
  btogglefill.pack(pady=5, anchor=tkinter.CENTER)

  bfillcolor = customtkinter.CTkButton(text="Couleur de remplissage",master=fenetre, corner_radius=10, command=fill_color)
  bfillcolor.pack(pady=5, anchor=tkinter.CENTER)

  bdot = customtkinter.CTkButton(text="Point",master=fenetre, corner_radius=10, command=dot)
  bdot.pack(pady=5, anchor=tkinter.CENTER)

  bcircle = customtkinter.CTkButton(text="Cercle",master=fenetre, corner_radius=10, command=circle)
  bcircle.pack(pady=5, anchor=tkinter.CENTER)

  bwrite = customtkinter.CTkButton(text="Écrire",master=fenetre, corner_radius=10, command=write)
  bwrite.pack(pady=5, anchor=tkinter.CENTER)

  bshape = customtkinter.CTkButton(text="Forme",master=fenetre, corner_radius=10, command=shape)
  bshape.pack(pady=5, anchor=tkinter.CENTER)

  breset = customtkinter.CTkButton(text="Effacer tout",master=fenetre, corner_radius=10, command=reset)
  breset.pack(pady=5, anchor=tkinter.CENTER)

  bminecraft = customtkinter.CTkButton(text="Minecraft",master=fenetre, corner_radius=10, command=minecraft)
  bminecraft.pack(pady=5, anchor=tkinter.CENTER)

  credits =customtkinter.CTkLabel(fenetre, text="Créé par: Gaël Hébert-Furoy", text_color='black')
  credits.pack(pady=5)

def generate_button_en():
  clearCommands()
  fenetre.title("Commands")
  customtkinter.set_appearance_mode('Dark')
  #Créer les buttons

  credits =customtkinter.CTkLabel(fenetre, text="Made by: Gaël Hébert-Furoy", text_color='black')
  credits.pack(pady=5)

  bdraw = customtkinter.CTkButton(text="Draw from URL",master=fenetre, corner_radius=10, command=draw)
  bdraw.pack(pady=5, anchor=tkinter.CENTER)

  blang = customtkinter.CTkButton(text="Language",master=fenetre, corner_radius=10, command=langages)
  blang.pack(pady=5, anchor=tkinter.CENTER)

  bcalc = customtkinter.CTkButton(text="Calculate",master=fenetre, corner_radius=10, command=nb1)
  bcalc.pack(pady=5, anchor=tkinter.CENTER)

  btriangle = customtkinter.CTkButton(text="Triangle",master=fenetre, corner_radius=10, command=triangle)
  btriangle.pack(pady=5, anchor=tkinter.CENTER)

  bsquare = customtkinter.CTkButton(text="Square",master=fenetre, corner_radius=10, command=carre)
  bsquare.pack(pady=5, anchor=tkinter.CENTER)

  bforw = customtkinter.CTkButton(text="Forward",master=fenetre, corner_radius=10, command=forw)
  bforw.pack(pady=5, anchor=tkinter.CENTER)

  bbackw = customtkinter.CTkButton(text="Backward",master=fenetre, corner_radius=10, command=backw)
  bbackw.pack(pady=5, anchor=tkinter.CENTER)

  bleft = customtkinter.CTkButton(text="<--",master=fenetre, corner_radius=10, command=left)
  bleft.pack(pady=5, anchor=tkinter.CENTER)

  bright = customtkinter.CTkButton(text="-->",master=fenetre, corner_radius=10, command=right)
  bright.pack(pady=5, anchor=tkinter.CENTER)

  brot = customtkinter.CTkButton(text="Reset Angle",master=fenetre, corner_radius=10, command=rotation)
  brot.pack(pady=5, anchor=tkinter.CENTER)

  bgoto = customtkinter.CTkButton(text="Move",master=fenetre, corner_radius=10, command=goto)
  bgoto.pack(pady=5, anchor=tkinter.CENTER)

  bgotod = customtkinter.CTkButton(text="Move and Draw",master=fenetre, corner_radius=10, command=gotoanddraw)
  bgotod.pack(pady=5, anchor=tkinter.CENTER)

  bcolor = customtkinter.CTkButton(text="Color",master=fenetre, corner_radius=10, command=color)
  bcolor.pack(pady=5, anchor=tkinter.CENTER)

  btoolsize = customtkinter.CTkButton(text="Tool Size",master=fenetre, corner_radius=10, command=length)
  btoolsize.pack(pady=5, anchor=tkinter.CENTER)

  btogglefill = customtkinter.CTkButton(text="Toggle Fill Mode",master=fenetre, corner_radius=10, command=toggleFill)
  btogglefill.pack(pady=5, anchor=tkinter.CENTER)

  bfillcolor = customtkinter.CTkButton(text="Fill Color",master=fenetre, corner_radius=10, command=fill_color)
  bfillcolor.pack(pady=5, anchor=tkinter.CENTER)

  bdot = customtkinter.CTkButton(text="Dot",master=fenetre, corner_radius=10, command=dot)
  bdot.pack(pady=5, anchor=tkinter.CENTER)

  bcircle = customtkinter.CTkButton(text="Circle",master=fenetre, corner_radius=10, command=circle)
  bcircle.pack(pady=5, anchor=tkinter.CENTER)

  bwrite = customtkinter.CTkButton(text="Write",master=fenetre, corner_radius=10, command=write)
  bwrite.pack(pady=5, anchor=tkinter.CENTER)

  bshape = customtkinter.CTkButton(text="Shape",master=fenetre, corner_radius=10, command=shape)
  bshape.pack(pady=5, anchor=tkinter.CENTER)

  breset = customtkinter.CTkButton(text="Clear All",master=fenetre, corner_radius=10, command=reset)
  breset.pack(pady=5, anchor=tkinter.CENTER)

  bminecraft = customtkinter.CTkButton(text="Minecraft",master=fenetre, corner_radius=10, command=minecraft)
  bminecraft.pack(pady=5, anchor=tkinter.CENTER)

  credits =customtkinter.CTkLabel(fenetre, text="Made by: Gaël Hébert-Furoy", text_color='black')
  credits.pack(pady=5)

def clearCommands():
   global fenetre
   #Efface la fenetre de tkinter et en fait une nouvelle.
   fenetre.destroy()
   fenetre = tkinter.Tk()

#Goto
def ClickLeft(x, y):
  global pos_x
  global pos_y
  pos_x = x
  pos_y = y


#Évenement
turtle.listen()
t.ondrag(dragging)
turtle.onscreenclick(ClickLeft, 1)


def main_loop():
  #Sert a garder l'écran ouvert
  screen.mainloop()
  fenetre.mainloop()


generate_button_fr()
main_loop()
