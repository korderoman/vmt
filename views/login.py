from tkinter import *
from PIL import ImageTk, Image

class Login():
    def __init__(self,ventana):
        #constantes de diseño
        self.mx=5
        self.my=2
        self.frame_principal=Frame(ventana)
        #creamos los subframes del login
        self.frame_izquierda=Frame(self.frame_principal)
        self.frame_derecha=Frame(self.frame_principal)
        #posicionamos los subframes
        self.frame_izquierda.pack(fill="x",expand=True,side="left")
        self.frame_derecha.pack(fill="x",expand=True,side="right")        
        #variables del formulario de logeo
        self.usuario=StringVar()
        self.clave=StringVar()
        
        #inicializamos el método
        self.crear_interfaz(self.frame_izquierda,self.frame_derecha)
        
        

    def crear_interfaz(self,frame_iz,frame_der):
        #imagen de logo
        canvas=Canvas(frame_iz,bg="black",width=250,height=450)
        canvas.pack(fill=BOTH,expand=True)
        img=Image.open("resources\images\logo_vmt.png")
        canvas.image=ImageTk.PhotoImage(img)
        canvas.create_image(0,0,image=canvas.image,anchor="nw")
        """ Formulario de Logeo """
        #Usuario
        Label(frame_der,text="Usuario:").grid(row=0,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_der,textvariable=self.usuario).grid(row=1,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        #contraseña
        Label(frame_der,text="Contraseña:").grid(row=2,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_der,textvariable=self.clave,show="*").grid(row=3,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        #logearse
        Button(frame_der,text="Entrar",command=self.logearse).grid(row=4,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        #mensaje 
        Label(frame_der,text="En caso no poder ingresar al sistema comunicarse con el Administrador").grid(row=5,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        """ Fin de Formulario de logeo"""
    def logearse(self):
        print(self.usuario.get(),self.clave.get())
