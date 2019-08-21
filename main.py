from tkinter import *
from tkinter import messagebox 
#importamos la vista principal
from views.index import *

if __name__ == "__main__":
    principal=Tk()
    w_p=816 #el ancho de la ventana de nuestro programa
    h_p=490 #el alto de la ventana de nuestro programa
    w_d=principal.winfo_screenwidth() #el ancho del dispositivo donde se despliega el programa
    h_d=principal.winfo_screenheight()#al alto del dispositivo donde se despliega  el programa
    p_x=(w_d/2)-(w_p/2) #posición relativa en x de nuestro programa en el dispositivo
    p_y=(h_d/2)-(h_p/2) #posicion relativa en y de nuestro programa en el dispositivo

    principal.geometry("%dx%d+%d+%d"%(w_p,h_p,p_x,p_y)) #dimensión y posicion del programa
    principal.resizable(False,False) #denegamos que el usuario pueda redimensionar la ventana
    principal.title("Formulario de Incidentes - CCTV ") #generamos un título
    index=Index(principal)
    principal.config(menu=index.menu_principal)

    def salir():
        if messagebox.askokcancel("Salir de Aplicación","¿Está seguro que desea salir?"):
            principal.quit()
            principal.destroy()  
    principal.protocol("WM_DELETE_WINDOW",salir)
    principal.mainloop()