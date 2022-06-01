import sys
import math
from time import sleep
from tkinter import Text

import pyglet
import threading
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL._bytes import as_8_bit

#Iluminacion
class iluminacion(object):
    encendida = True
    colores = [(2.55, 2.55, 2.55, 0), (1., 0.5, 0.5, 1.),
               (0.5,1.,0.5,1.), (0.5,0.5,1.,1.)]
    def __init__(self, luz_id, posicion):
        self.luz_id = luz_id
        self.posicion = posicion
        self.color_actual = 2

    def dibujar(self):
        light_id = self.luz_id
        color = iluminacion.colores[self.color_actual]
        glLightfv(light_id, GL_POSITION, self.posicion)
        glLightfv(light_id, GL_DIFFUSE, (2.55,2.55,2.55,2.55))
        glLightfv(light_id, GL_CONSTANT_ATTENUATION, 0.10)
        glLightfv(light_id, GL_LINEAR_ATTENUATION, 0.01)

    def cambiar_color(self):
        self.color_actual += 0
        self.color_actual %= len(iluminacion.colores)


    def enable(self):
        if not iluminacion.encendida:
            glEnable(GL_LIGHTING)
            iluminacion.encendida = False
        glEnable(self.luz_id)




class Mundo(object):
    def __init__(self, radio, posicion, color):
        self.radio = 35
        self.posicion = posicion
        self.color = color

    def dibujar(self):
        glTranslatef(*self.posicion)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.color)
        glPolygonMode(GL_FRONT, GL_FILL)
        glutSolidCube(100)

class islaa (object):
    meridianos = 40
    paralelos = 40

    def __init__(self, radio, posicion, color):
        self.radio = radio
        self.posicion = posicion
        self.color = color

    def dibujar(self):
        glTranslatef(*self.posicion)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1.61,1.30,.98,1))
        self.esfera()

    def esfera(self):
        glTranslatef(0,.25,.25)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,(0.933 , 0.513 , 0.098))
        glutSolidSphere(2.8,40,40)



class algas (object):
    meridianos = 40
    paralelos = 40

    def __init__(self, radio, posicion, color):
        self.radio = radio
        self.posicion = posicion
        self.color = color

    def dibujar(self):
        glTranslatef(*self.posicion)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1.61,1.30,.98,1))
        self.algas()

    def algas(self):
        glTranslatef(0,.25,.25)
        glMaterialfv(GL_FRONT, GL_DIFFUSE,( 0.258 , 0.686 , 0.317))
        glutSolidSphere(2,5,40)


class poste(object):
    meridianos = 40
    paralelos = 40

    def __init__(self, radio, posicion, color):
        self.radio = radio
        self.posicion = posicion
        self.color = color

    def dibujar(self):
        glTranslatef(*self.posicion)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1.61,1.30,.98,1))
        self.poste()

    def poste(self):
        glTranslatef(-0.19,0.0,3.3)
        #glRotatef(120,120,0,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.258 , 0.686 , 0.317))
        glutSolidCylinder( 0.5,7.3,20,100)




class Barco(object):

    def __init__(self, radio, posicion, color,vectores,angulo):
        self.radio = radio
        self.posicion = posicion
        self.color = color
        self.vectores=vectores
        self.angulo=angulo


    def dibujar(self):
        glTranslatef(*self.posicion)
        glRotatef(self.angulo,*self.vectores)
        self.base()
        self.base_2()

        self.punta_barco()
        #self.piso_1()
        self.base_alta()
        self.base_alta2()
        self.base_alta3()
        self.base_alta4()

        self.ventana()
        self.ventana2()
        self.ventana3()
        self.ventana4()

        self.piso1()
        self.piso2()

        self.caja1()
        self.caja2()

        self.cabina()

        self.puerta()
        self.puerta2()

        self.marco_ventana()
        self.marco_ventana1()
        self.marco_ventana2()
        self.marco_ventana3()

        self.super_ventana()
        self.super_ventana1()
        self.super_ventana2()
        self.super_ventana3()

        self.marco_ventana4()
        self.super_ventana4()

        self.techo_cabina()
        self.techo_cabina1()
        self.techo_cabina2()
        self.techo_cabina3()
        self.techo_cabina4()
        self.techo_cabina5()
        self.techo_cabina6()
        self.techo_cabina7()
        self.techo_cabina8()
        self.techo_cabina9()
        self.techo_cabina10()
        self.techo_cabina11()
        self.techo_cabina12()
        self.techo_cabina13()

        self.base_3()
        self.base_alta_1()
        self.base_alta_2()
        self.base_alta_3()
        self.piso3()
        self.ventana_black()
        self.ventana_black2()
        self.tubo()
        self.tubo2()

        self.texto()
        self.humo_1()
        self.humo_2()
        self.humo_3()
        self.humo_4()
        self.humo_5()
        self.humo_6()
        





  #punta principla
    def base(self):
            glTranslatef(0,.25,.25)
            #color rojo =1.0 ,0.0,0.0

            glMaterialfv(GL_FRONT, GL_DIFFUSE,(1.0,0.0,0.0))
            glutSolidCube(4)
    #cola del barco
    def base_2(self):
        glTranslatef(-0,-0.0,-4)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(1.0,0.0,0.0))
        glutSolidCube(4)
    def punta_barco(self):
        glTranslatef(0,0.5,6)
       # glRotated(1,1,0)
        #glRotatef(1,2,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(1.0,0.0,0.0))
       # glutSolidCone(2.0,2,20,30)
        glutSolidCone(2.0,2,20,5)









    def base_alta(self):
        glTranslatef(-1.9,1.7,-8)
       # glRotated(1,1,0)
        #glRotatef(1,2,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,8,20,100)
    def base_alta2(self):
        glTranslatef(3.7,0.0,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,8,20,100)
    def base_alta3(self):
        glTranslatef(-3.8,0.0,0.0)
        glRotatef(90,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,3.9,20,100)
        
    def base_alta4(self):
        glTranslatef(-7.9,0.0,4)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,3.9,20,100)


    def ventana(self):
        glTranslatef(-2,-1,-0.1)
        #glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0  , 0.498 , 0.933))
        glutSolidTorus( 0.10, 0.50, 35, 35)

    def ventana2(self):
        glTranslatef(-4,-0.0,0.0)
        #glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0  , 0.498 , 0.933))
        glutSolidTorus( 0.10, 0.50, 35, 35)

    def ventana3(self):
        glTranslatef(4,-0.0,4.2)
        #glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0  , 0.498 , 0.933))
        glutSolidTorus( 0.10, 0.50, 35, 35)
    def ventana4(self):
        glTranslatef(-4,-0.0,-0.1)
        #glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0  , 0.498 , 0.933))
        glutSolidTorus( 0.10, 0.50, 35, 35)

    def piso1(self):
        glTranslatef(4.3,-0.89,-2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.505 , 0.294 , 0.047 ))
        glutSolidCube(3.5)

    def piso2(self):
        glTranslatef(-3.5,-0.0,0.0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.505 , 0.294 , 0.047 ))
        glutSolidCube(3.5)

    def caja1(self):
        glTranslatef(-1.7,1.5,0.8)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.572 , 0.552 , 0.552))
        glutSolidCube(1.5)

    def caja2(self):
        glTranslatef(-0.0,-0.0,-1.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.572 , 0.552 , 0.552))
        glutSolidCube(1.5)

    def cabina(self):
        glTranslatef(5.5,1.0,0.7)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidCube(2.5)

    def puerta(self):
        glTranslatef(-1.05,-0.5,0.0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.5)

    def puerta2(self):
        glTranslatef(-0.02,0.5,0.0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.5)

    def marco_ventana(self):
        glTranslatef(1.99,0.7,0.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.8)

    def marco_ventana1(self):
        glTranslatef(0.0,-0.0,-0.8)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.8)

    def marco_ventana2(self):
        glTranslatef(0.0,-0.0,-0.2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.8)

    def marco_ventana3(self):
        glTranslatef(-0.9,0.0,1.39)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.8)

    def super_ventana(self):
        glTranslatef(-0.0,0.0,0.13)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(  0.321 , 0.690 , 0.901))
        glutSolidCube(0.6)


    def super_ventana1(self):
        glTranslatef(1.01,0.0,-1.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(  0.321 , 0.690 , 0.901))
        glutSolidCube(0.6)

    def super_ventana2(self):
        glTranslatef(0.01,0.0,1)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(  0.321 , 0.690 , 0.901))
        glutSolidCube(0.6)

    def super_ventana3(self):
        glTranslatef(0.00,0.0,-0.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(  0.321 , 0.690 , 0.901))
        glutSolidCube(0.6)

    def marco_ventana4(self):
        glTranslatef(-0.99,0.00,-0.9)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 0.807 , 0.474 , 0.039))
        glutSolidCube(0.8)

    def super_ventana4(self):
        glTranslatef(0.00,0.0,-0.11)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(  0.321 , 0.690 , 0.901))
        glutSolidCube(0.6)

    def techo_cabina(self):
        glTranslatef(-2.0,0.5,2.2)
        glRotatef(90,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina1(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina2(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)

    def techo_cabina3(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina4(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina5(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina6(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina7(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina8(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)

    def techo_cabina9(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)

    def techo_cabina10(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina11(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina12(self):
        glTranslatef(-0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
    def techo_cabina13(self):
        glTranslatef(0.19,0.0,3.3)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.807 , 0.474 , 0.039))
        glutSolidCylinder( 0.1,3.3,20,100)
        #agregados

    def base_3(self):
        glTranslatef(1.29,-4,9.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(1.0,0.0,0.0))
        glutSolidCube(4)

    def base_alta_1(self):
        glTranslatef(-1.9,2.2,2)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,3.9,20,100)

    def base_alta_2(self):
        glTranslatef(-3.8,0,4)
        glRotatef(180,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,3.9,20,100)

    def base_alta_3(self):
        glTranslatef(-3.9,0,4)
        glRotatef(90,0,90,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.831 , 0.776 ,  0.0))
        glutSolidCylinder( 0.2,3.9,20,100)

    def piso3(self):
        glTranslatef(1.8,-1.8,2.0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.505 , 0.294 , 0.047 ))
        glutSolidCube(3.5)

    def ventana_black(self):
        glTranslatef(0.5,0.6,1.1)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0 , 0.0 , 0.0 ))
        glutSolidCube(2)

    def ventana_black2(self):
        glTranslatef(-0.5,0,-2.2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.0 , 0.0 , 0.0 ))
        glutSolidCube(2)

    def tubo(self):
        glTranslatef(-1,1,2)
        glRotatef(180,0,120,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.541 , 0.541 , 0.541))
        glutSolidCylinder( .5,3.9,70,200)

    def tubo2(self):
        glTranslatef(-1,-1,-2)
        glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,(0.541 , 0.541 , 0.541))
        glutSolidCylinder( .7,3.9,70,200)

    def draw_text(self,text, font):
        for c in text:
            glutBitmapCharacter(font, ord(c))


    def texto(self):
        glTranslatef(3,5,6)
        glColor3f( 0.062 , 0.062 , 0.831)
        glRasterPos3f(-0.8, 2.5,1.0)
        #!ERROR DE VS CODE
        self.draw_text("chu chuuuuuuu", GLUT_BITMAP_TIMES_ROMAN_24)

    def humo_1 (self):
        glTranslatef(-4,-6,0)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(1,10,10)
    
    def humo_2 (self):
        glTranslatef(-1,0,0.3)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(1,10,10)
    def humo_3 (self):
        glTranslatef(-1,0,0.3)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(0.7,10,10)
    def humo_4 (self):
        glTranslatef(-1,0,0.3)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(0.7,10,10)
    def humo_5 (self):
        glTranslatef(-1,0,0.3)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(0.5,10,10)
    def humo_6 (self):
        glTranslatef(-1,0,0.3)
        #glRotatef(180,0,0,120)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,( 1.0  ,  1.0  ,  1.0))
        glutSolidSphere(0.3,10,10)












class App(object):
    def __init__(self, largo=1200, ancho=800):

        self.titulo = 'Barco'
        self.largo = largo
        self.ancho = ancho
        self.angulo = 0
        self.angulo2=0
        self.distancia = 8
        #self.movimientosuperior =-4.5
        self.movimiento2 = -10
        self.movimientolateral2 = 10
        self.iluminacion = iluminacion(GL_LIGHT0, (150, 100, 150, 1))
        self.iluminacion2 = iluminacion(GL_LIGHT1, (-150,-100, -150, 1))

        self.oceano()





    def oceano(self):


        self.pisoMundo2=Mundo(20,(0,-15,0),( 0.086 , 0.294 , 0.870))
        self.barcoA = Barco(20, (self.movimientolateral2,0.5,self.movimiento2), (),(5,1.0,0.0),0)

        self._isla=islaa(.20,(-20,68,-15),( 0.086 , 0.294 , 0.870))

        self._algas=algas(.20,(-15,-30,20),( 0.086 , 0.294 , 0.870))

        self._poste=poste(.20,(15,11.5,20),( 0.086 , 0.294 , 0.870))

        









    def iniciar(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowPosition(50, 50)
        glutInitWindowSize(self.largo, self.ancho)
        glutCreateWindow(self.titulo)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
       #

        self.iluminacion.enable()
        self.iluminacion2.enable()

        glClearColor(0.34,1.13,1.79,1)
        #glColor3f( 0.086 , 0.294 , 0.870)


        glMatrixMode(GL_PROJECTION)
        aspect = self.largo / self.ancho
        gluPerspective(115., aspect, 0.9, 50.)
        glMatrixMode(GL_MODELVIEW)
        glutDisplayFunc(self.dibujarplano)

        glutSpecialFunc(self.keyboard)
        glutKeyboardFunc(self.normalKeyboard)
        glutKeyboardFunc(self.normalKeyboard)
        glutMotionFunc(self.Motion)
        glutMainLoop()

    def Motion(self, x,y):
        self.angulo2 = y / 500
        self.angulo = x / 500
        glutPostRedisplay()






    def dibujarplano(self):
        self.distancia=40
        x = math.sin(self.angulo) * self.distancia
        z = math.cos(self.angulo) * self.distancia

        z2 = math.cos(self.angulo2) * self.distancia

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(x, z2, z,
                  0, 0, 0,
                  0, 1, 0)

        self.iluminacion.dibujar()
        self.iluminacion2.dibujar()
        self.mundo()
        glutSwapBuffers()

    def mundo(self):


        self.pisoMundo2.dibujar()
        self._isla.dibujar()
        self._algas.dibujar()
        self._poste.dibujar()
        

        glPushMatrix()

        glPopMatrix()
        self.barcoA.dibujar()


    def keyboard(self, tecla, x, y):
        if tecla == GLUT_KEY_INSERT:
            sys.exit()
        if tecla == GLUT_KEY_UP:
            self.angulo2-=0.15
        if tecla == GLUT_KEY_DOWN:
            self.angulo2+=0.15
        if tecla == GLUT_KEY_LEFT:
            self.angulo -= 0.15
        if tecla == GLUT_KEY_RIGHT:
            self.angulo += 0.15

        self.distancia = max(2, min(self.distancia, 10))
        self.angulo %= math.pi * 2
        self.angulo2 %= math.pi * 2
        glutPostRedisplay()


    def normalKeyboard(self, tecla,x,y):

        if tecla == as_8_bit('W') or tecla == as_8_bit('w'):
                posicion = ((self.movimientolateral2),0.5, (self.movimiento2))
                self.movimiento2 -= 0.10
                self.barcoA = Barco(20, (posicion), (0,1,0),(0.0,1.0,0.0),180)




        if tecla == as_8_bit('S') or tecla == as_8_bit('s'):
                posicion = ((self.movimientolateral2),0.5, (self.movimiento2))
                self.movimiento2 += 0.10
                self.barcoA=Barco(20,(posicion),(0,1,0),(0.0,0.0,0.0),0)



        if tecla == as_8_bit('D') or tecla == as_8_bit('d'):
                posicion = ((self.movimientolateral2),0.5, (self.movimiento2))
                self.movimientolateral2 += 0.10
                posicion=((self.movimientolateral2),0.5,(self.movimiento2))
                self.barcoA=Barco(20,(posicion),(0,1,0),(0.0,1.0,0.0),90)

#a
        if tecla == as_8_bit('A') or tecla == as_8_bit('a'):
                posicion = ((self.movimientolateral2),0.5, (self.movimiento2))
                self.movimientolateral2 -= 0.10
                posicion=((self.movimientolateral2),0.5,(self.movimiento2))
                self.barcoA=Barco(20,(posicion),(0,1,0),(0.0,-1.0,0.0),90)
#a
        self.distancia = max(1, min(self.distancia, 10))
        self.angulo %= math.pi * 2
        self.angulo2 %= math.pi * 2
        glutPostRedisplay()
def music():
    musica = pyglet.resource.media('barco.wav', streaming=True)
    musica.play()
    pyglet.app.run()


if __name__ == '__main__':
    t1 = threading.Thread(name="t_Musica", target=music)
    t1.start()
    app = App()
    app.iniciar()

#final
