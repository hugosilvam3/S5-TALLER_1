from abc import ABC,abstractclassmethod,abstractmethod
from helpers import Helper
import os
class ADMINISTRACION:
  pass
      
class USUARIO():
  def __init__(self,nombre,direccion,cedula,email):
    self.nombre = nombre
    self.direccion = direccion
    self.cedula = cedula
    self.email = email
    
  @abstractmethod
  def mostrarCleinte(self):
    print(self.nombre,self.cedula,self.direccion,self.email)
        

    
class OPC_SISTEMA:
  def __init__(self,certi_usuario,verificar_datos,modificar_datos):
    self.certi_usuario = certi_usuario
    self.verificar_datos = verificar_datos
    self.modificar_datos = modificar_datos
    pass 
      
class MODIFICARDATOS(USUARIO):
  def __init__(self, nombre, direccion, cedula, email):
    super().__init__(nombre, direccion, cedula, email)
  def CertificarUsuario(self):
    print("*"*20,"Certificado Usuario","*"*20)
    print("Nombre"," "*10,"Cedula"," "*10,"Email"," "*10,"Direccion")
    print("{:15} {:13} {:23} {}".format(self.nombre,self.cedula,self.email,self.direccion) )
  
  def VerificarDatos(self):
    da = input("Ingrese el nombre")
    while da.isnumeric() == True :
      print("tiene que ingresar sólo letras")
      
  def ModificarDatos():
    
    pass
      
      
    
class VERIFICAR_DATOS(USUARIO):
  def __init__(self, nombre, direccion, cedula, email):
    super().__init__(nombre, direccion, cedula, email)
    def CantidadCaracteres(self):
      nombre=len(nombre)
      cedula=len(cedula)
      while len(cedula) < 10:
        print("ingrese 10 digitos") 
        cedula=int(input("ingrese cedula"))
      direccion=len(direccion)
      print("nombre tiene:{} caracteres".format(nombre))
      print("cedula tiene:{} caracteres".format(cedula))
      print("")

    pass
      
class CERTI_USUARIO(USUARIO):
  def __init__(self,nomb_usuario,celular,contraseña):
    self.nomb_usuario = nomb_usuario
    self.celular = celular
    self.contraseña = contraseña
    pass
      
helper = Helper()
lista=["1) Usuario","2) Administrador","3) Salir"]
opcion=""
while opcion != "3":
  os.system("clear")
  opcion = helper.menu(lista,"Menu Principal")
  if opcion == "1":
    opc1=""
    while opc1 != "2":
      os.system("clear")
      print("*"*20,"Mantenimento De Usuario","*"*20)
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"")