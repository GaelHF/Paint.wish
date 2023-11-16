#Crédits:
# Software Engineer: Gaël Hébert-Furoy
# ~500 lignes de code
# https://www.geeksforgeeks.org/

#Bibliothèque
import turtle
import tkinter

#Variables
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500, 500)
screen.colormode(255)
fenetre = tkinter.Tk()

current_Color = "black"
current_FillColor = "black"
current_Longeur = 100
current_Cote = 0
current_ToolSize = 0
isFilling = False
current_Text = ""

pos_x = 0
pos_y = 0

t.speed(-1)


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
  global current_ToolSize
  global isFilling
  global pos_x
  global pos_y
  current_Text = ""
  current_Color = ""
  current_FillColor = ""
  current_Longeur = 100
  current_Cote = 0
  current_ToolSize = 0
  isFilling = False
  pos_x = 0
  pos_y = 0
  t.clear()
  t.reset()
  t.speed(-1)


def dot():
  #Fait un point
  t.dot(current_ToolSize)


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

  ChangeButton = tkinter.Button(fill_color, text="Changer", command=fill_color_change)
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


def size():
  #Change la taille du pinceau
  size = tkinter.Toplevel(fenetre)
  size.title("Taille")
  size.geometry("300x100")
  canvas1 = tkinter.Canvas(size, width=50, height=50)
  canvas1.pack()
  entry1 = tkinter.Entry(size)
  canvas1.create_window(0, 10, window=entry1)

  def change_color():
    global current_ToolSize
    current_ToolSize = int(entry1.get())
    t.pensize(current_ToolSize)
    size.destroy()

  ChangeButton = tkinter.Button(size, text="Changer", command=change_color)
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
    t.write(current_Text, font=("Verdana", 15, "normal"))

  ChangeButton = tkinter.Button(write, text="Écrire", command=change_color)
  ChangeButton.pack()

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
    
def dragging(x, y):
  #dessiner en glissant turtle
  t.ondrag(None)
  t.setheading(t.towards(x, y))
  t.goto(x, y)
  t.ondrag(dragging)


#Titres
fenetre.title('Commandes')
screen.title('Paint.wish')


def generate_button():
  #Créer les buttons
  credits = tkinter.Label(fenetre, text="Créé par: Gaël Hébert-Furoy")
  credits.pack()
  triangleButton = tkinter.Button(fenetre, text="Triangle", command=triangle)
  triangleButton.pack()

  SquareButton = tkinter.Button(fenetre, text="Carré", command=carre)
  SquareButton.pack()

  LeftButton = tkinter.Button(fenetre, text="<--", command=left)
  LeftButton.pack()

  RightButton = tkinter.Button(fenetre, text="-->", command=right)
  RightButton.pack()
  rotButton = tkinter.Button(fenetre, text="Reset Rotation", command=rotation)
  rotButton.pack()

  GotoButton = tkinter.Button(fenetre, text="Aller à", command=goto)
  GotoButton.pack()

  GotodButton = tkinter.Button(fenetre, text="Aller à et dessiner", command=gotoanddraw)
  GotodButton.pack()

  ColorButton = tkinter.Button(fenetre, text="Couleur", command=color)
  ColorButton.pack()

  SizeButton = tkinter.Button(fenetre, text="Longeur", command=length)
  SizeButton.pack()

  ToggleFillButton = tkinter.Button(fenetre, text="Switch mode remplissage", command=toggleFill)
  ToggleFillButton.pack()

  FillColorButton = tkinter.Button(fenetre, text="Couleur de remplissage", command=fill_color)
  FillColorButton.pack()

  BrushSizeButton = tkinter.Button(fenetre, text="Taille du pinceau", command=size)
  BrushSizeButton.pack()

  dotButton = tkinter.Button(fenetre, text="Point", command=dot)
  dotButton.pack()
  
  circleButton = tkinter.Button(fenetre, text="Cerlce", command=circle)
  circleButton.pack()
  
  writeButton = tkinter.Button(fenetre, text="Texte", command=write)
  writeButton.pack()
  
  shapeButton = tkinter.Button(fenetre, text="Forme", command=shape)
  shapeButton.pack()
  
  resetButton = tkinter.Button(fenetre, text="Effacer tous", command=reset)
  resetButton.pack()
  
  MinecraftButton = tkinter.Button(fenetre, text="Minecraft", command=minecraft)
  MinecraftButton.pack()
  
  credits = tkinter.Label(fenetre, text="Créé par: Gaël Hébert-Furoy")
  credits.pack()


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


generate_button()
main_loop()
