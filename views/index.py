from tkinter import *
from tkinter import ttk

#importamos las demas vistas
from views.login import *

class Index():
    def __init__(self,ventana):
        self.ventana=ventana
        #la vista por defecto deberá ser la de login
        login=Login(self.ventana)
        login.frame_principal.pack(fill=BOTH)