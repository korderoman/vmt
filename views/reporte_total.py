from tkinter import *
from tkinter import ttk
#controlador de base de datos
from controllers.controlador import *
class Reporte_Total:
    def __init__(self,ventana):
        self.ventana=ventana
        self.frame_principal=Frame(self.ventana)
        self.tabla=None
        self.crear_interfaz(self.frame_principal)
        #controlador
        self.controlador=Controlador()
        self.obtener_data_en_tabla()
    
    def crear_interfaz(self,frame):
        self.tabla=ttk.Treeview(frame, columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10"),show=["headings"])
        scroll_y=ttk.Scrollbar(frame,orient="vertical",command=self.tabla.yview)
        scroll_x=ttk.Scrollbar(frame,orient="horizontal",command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        #definimos las columnas recuerda que la #0 define el nombre del arbol
        
        self.tabla.column("#1",minwidth=60,width=60,stretch=False,anchor=CENTER)
        self.tabla.column("#2",width=250,stretch=False,anchor=CENTER)
        self.tabla.column("#3",minwidth=110,width=110,stretch=False,anchor=CENTER)
        self.tabla.column("#4",minwidth=60,width=60,stretch=False,anchor=CENTER)
        self.tabla.column("#5",width=70,stretch=False,anchor=CENTER)
        self.tabla.column("#6",width=250,stretch=False,anchor=CENTER)
        self.tabla.column("#7",width=70,stretch=False,anchor=CENTER)
        self.tabla.column("#8",width=250,stretch=False,anchor=CENTER)
        self.tabla.column("#9",width=250,stretch=False,anchor=CENTER)
        self.tabla.column("#10",width=250,stretch=False,anchor=CENTER)
        #definimos los encabezados
        self.tabla.heading("#1",text="COD",anchor=CENTER)
        self.tabla.heading("#2",text="ADMIN",anchor=CENTER)
        self.tabla.heading("#3",text="FECHA",anchor=CENTER)
        self.tabla.heading("#4",text="PUESTO",anchor=CENTER)
        self.tabla.heading("#5",text="TURNO",anchor=CENTER)
        self.tabla.heading("#6",text="OPERADOR",anchor=CENTER)
        self.tabla.heading("#7",text="CÁMARA",anchor=CENTER)
        self.tabla.heading("#8",text="ÁREA",anchor=CENTER)
        self.tabla.heading("#9",text="TIPO DE INCIDENCIA",anchor=CENTER)
        self.tabla.heading("#10",text="DESCRIPCIÓN",anchor=CENTER)
        #colocamos la tabla en el frame
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.tabla.pack(side=LEFT,fill=BOTH,expand=False)
    
    def obtener_data_en_tabla(self):
        resultados=self.controlador.mostrar_incidencias_totales()
        #print(datos) # observar lo que se esta recibiendo, una lista de tuplas
        
        for index,dato in enumerate(resultados):
            self.tabla.insert("",0,text="datos",values=(dato[0],dato[3],dato[4],dato[2],dato[6],dato[1],dato[5],dato[9],dato[7],dato[8]))
