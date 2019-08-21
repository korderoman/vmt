from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import ttk

class Formulario():
    def __init__(self,ventana):
        self.ventana=ventana
        self.mx=5
        self.my=2
        self.frame_principal=Frame(ventana)
        #administradores
        self.check_admin1=IntVar()
        self.check_admin2=IntVar()
        self.check_admin3=IntVar()
        #puesto
        self.radio_puesto=IntVar()
        #turno
        self.radio_turno=IntVar()

    def crear_interfaz(self,frame):
        """Administradores"""
        administradores=LabelFrame(frame,text="Administrador",padx=self.mx,pady=self.my,sticky=W+E)
        Checkbutton(administradores,text="ENIT Nole",variable=self.check_admin1,onvalue=1,offvalue=0).grid(row=0,column=0, padx=self.mx,pady=self.my,sticky=W+E)
        Checkbutton(administradores,text="Pablo Chaupis",variable=self.check_admin2,onvalue=1,offvalue=0).grid(row=1,column=0, padx=self.mx,pady=self.my,sticky=W+E)
        Checkbutton(administradores,text="Jefe de Grupo",variable=self.check_admin3,onvalue=1,offvalue=0).grid(row=2,column=0, padx=self.mx,pady=self.my,sticky=W+E)
        administradores.pack(fill="x", expand=True,side="left")
        """Puesto"""
        puestos=LabelFrame(frame,text="Puestos",padx=self.mx,pady=self.my,sticky=W+E)
        Radiobutton(puestos,text="OP1",variable=self.radio_puesto,value=1).grid(row=0, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(puestos,text="OP2",variable=self.radio_puesto,value=2).grid(row=1, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(puestos,text="OP3",variable=self.radio_puesto,value=3).grid(row=2, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(puestos,text="OP4",variable=self.radio_puesto,value=4).grid(row=3, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(puestos,text="OP5",variable=self.radio_puesto,value=5).grid(row=4, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        puestos.pack(fill="x",expand=True,side="left")
        """Turno"""
        turnos=LabelFrame(frame,text="Puestos",padx=self.mx,pady=self.my,sticky=W+E)
        Radiobutton(turnos,text="Mañana",variable=self.radio_turno,value=1).grid(row=0, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(turnos,text="Tarde",variable=self.radio_turno,value=2).grid(row=1, padx=self.mx,pady=self.my,column=0,sticky=W+E)
        Radiobutton(turnos,text="Noche",variable=self.radio_turno,value=3).grid(row=2, padx=self.mx,pady=self.my,column=0,sticky=W+E)

        """Operador"""
        
