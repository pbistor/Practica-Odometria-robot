import math
import readchar
import matplotlib.pyplot as plt

separacionRuedas: float
diametroDerecha: float
diametroIzquierda: float
conversionIzq: float
encoderDer: float
encoderIzq: float
desplazamientoDer: float
desplazamientoIzq: float
desplazamientoFinal: float
giro: float
anguloGiro: float
global orientacion
global posicionX
global posicionY
radioGiro: float
incrementoX: float
incrementoY: float

posicionX = 0
posicionY = 0
orientacion = 0

#lista para almacenar las posiciones del robot
posiciones_x = []
posiciones_y = []
posiciones_x.append(0)
posiciones_y.append(0)

fig, ax = plt.subplots()

#límites de los ejes
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

#etiquetas y titulo
ax.set_xlabel('Posición X')
ax.set_ylabel('Posición Y')
ax.set_title('Trayectoria del Robot')

ax.grid(True)


def calcularPosicion(encoderDer, encoderIzq):
    global orientacion
    global posicionX
    global posicionY
    posiciones_x_o = []
    posiciones_y_o = []

    separacionRuedas = 220 # valor de ejemplo, por tomar una medida similar a la del robot Roomba de la otra práctica (235)

    resEncoderDerecha = 1000
    resEncoderIzquierda = 1000

    conversionIzq = (2 * math.pi * diametroIzquierda / 2) / resEncoderIzquierda
    conversionDer = (2 * math.pi * diametroDerecha / 2) / resEncoderDerecha

    desplazamientoDer = encoderDer * conversionDer
    desplazamientoIzq = encoderIzq * conversionIzq
    desplazamientoFinal = (desplazamientoIzq + desplazamientoDer) / 2

    giro = (desplazamientoDer - desplazamientoIzq) / separacionRuedas  # esto es en radianes
    anguloGiro = (giro * 360) / (2 * math.pi)

    if anguloGiro != 0:
        radioGiro = desplazamientoFinal / anguloGiro
        incrementoX = radioGiro * math.sin(anguloGiro)
        incrementoY = radioGiro * (1 - math.cos(anguloGiro))
        posicionX = posicionX + incrementoX * math.cos(orientacion) - incrementoY * math.sin(orientacion)
        posicionY = posicionY + incrementoX * math.sin(orientacion)+ incrementoY * math.cos(orientacion)
    else:
        posicionX += desplazamientoFinal * math.cos(orientacion)
        posicionY += desplazamientoFinal * math.sin(orientacion)

    orientacion += anguloGiro

    #Mostramos las coordenadas y la orientación
    print("X:")   
    print(posicionX)

    print("Y:")
    print(posicionY)
    print("Orientación:")
    print(orientacion)
    
    # Agregamos las posiciones actuales a las listas
    posiciones_x.append(posicionX)
    posiciones_y.append(posicionY)
    # Pintamos el indicador de la orientación.
    posiciones_y_o.append(posicionY)
    posiciones_y_o.append(posicionY + 0.5 * math.sin(orientacion))
    posiciones_x_o.append(posicionX)
    posiciones_x_o.append(posicionX + 0.5 * math.cos(orientacion))
    plt.plot(posiciones_x_o, posiciones_y_o, label = "Orientación")
    

    # Pintar el recorrido del robot.
    plt.plot(posiciones_x, posiciones_y, label = "Trayectoria")
    plt.legend()
    plt.autoscale(False)   
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    plt.xlabel('Posición X')
    plt.ylabel('Posición Y')
    plt.title('Trayectoria del Robot')
    plt.grid(True)
    plt.savefig("robot.png")
    ax.clear()

def cargarEjemplo():
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(10, 10)
    calcularPosicion(-10, 10)
   

print("Diametro de la rueda derecha:")
diametroDerecha = float(input())
print("Diametro de la rueda izquierda:")
diametroIzquierda = float(input())
print("Puede pulsar las teclas que desee, para generar el ejemplo del informe, pulse e:")

while True:
    #leemos el carácter de entrada
    key = readchar.readkey()

    if key == 'i':
        calcularPosicion(10, 10)
    elif key == 'l':
        calcularPosicion(-10, 10)
    elif key == 'j':
        calcularPosicion(10, -10)
    elif key == 'k':
        calcularPosicion(-10, -10)
    elif key == 'u':
        calcularPosicion(10, 3)
    elif key == 'o':
        calcularPosicion(3, 10)
    elif key == 'e':
        cargarEjemplo()
    elif key == 'q':
        break




