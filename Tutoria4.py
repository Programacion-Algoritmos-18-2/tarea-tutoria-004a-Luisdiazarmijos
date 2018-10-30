#Definir la clase Materia
class Materia(object):
    
# Definimos atributos

    def  __init__ ( self ):
        self.codigo =  " "
        self.nombre =  " "

#Construimos los agregar y presentar de codigo y nombre
    def presentar_datos(self):
        return "%s-%s-%s" % (self.obtener_codigo(), self.nombre)

    def agregar_codigo(self, n):  
        self.codigo = n

    def obtener_codigo(self):
        return self.codigo

    def agregar_nombre(self, n):  
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def presentar_datos (self):
        return "%s-%s" % (self.codigo, self.nombre)
# Hacemos la clase y heredamos de la clase materia
class  MateriaPresencial (Materia):

   def __init__(self):
         
        self.num_creditos = " "
#Declaros los agregar y obteter respectivam,ente
   def agregar_num_creditos(self, n):  
        self.num_creditos = n

   def obtener_num_creditos(self):
        return self.num_creditos
        #Creamos el metodo presentar_datos
   def presentar_datos(self):
        return "%s-%s" % (super(MateriaPresencial, self).presentar_datos(), self.num_creditos)
