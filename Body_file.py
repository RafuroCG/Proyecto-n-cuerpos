import numpy as np
from numpy.linalg import norm

# Constante gravitacional en Unidades astronómicas, masas solares y años.
G = 4 * np.pi**2 

class Body:
    '''
    Clase para cada partícula. Contiene todos los parámetros de cada partícula: masa, posición, velocidad,
    color y nombre. También contiene las funciones a ejecutar en cada iteración, responsables de actualizar
    la posición y velocidad inicial usando el método "leapfrog" (que se explica en la función "animate") 
    con la fórmula de la fuerza gravitacional.

    Atributos:
        m (float): Masa de la partícula.
        pos (arreglo de numpy de R2): Posición de la partícula.
        vel (arreglo de numpy de R2): Velocidad de la partícula.
        color (string): Representación hexadecimal del color de la partícula.
        r_accel (arreglo de numpy de R2): Aceleración resultante sobre la partícula.

    Métodos:
        comp_accel (bodies): Computa la aceleración resultante de la partícula en el tiempo actual 
        sumando la fuerza causada por cada partícula distinta a la misma con la fórmula de la fuerza
        gravitacional: F = (-GMm/(r^3))r.
        update_vel (bodies, dt): Actualiza la velocidad a la mitad del intervalo actual ejecutando 
        "comp_accel" para hallar la aceleración.
        update_pos (dt): Actualiza la posición al final del intervalo actual con la velocidad en la 
        mitad.
    '''
    def __init__(self, masa, pos0, vel0, color, name="body"):
        self.m = float(masa)
        self.pos = np.array(pos0, dtype="float64")
        self.vel = np.array(vel0, dtype="float64")
        self.color = color
        self.name = str(name)
        

    def comp_accel(self, particles):
        '''
        Computa la aceleración resultante de la partícula en el tiempo actual 
        sumando la fuerza causada por cada partícula distinta a la misma con la fórmula de la fuerza
        gravitacional: F = (-GMm/(r^3))r.

        :particles: Lista de objetos de las partículas en la simulación.
        :return: Aceleración resultante. Arreglo de numpy de R2.
        '''
        self.r_accel = np.array([0.0, 0.0])
        for body in particles:
            # Para cada partícula distinta a la misma...
            if body is not self:
                # se halla el vector posición de dicha partícula desde la misma...
                relative_pos = body.pos - self.pos
                # y se halla la fuerza ejercida por dicha partícula a la misma, sumándose a la resultante.
                self.r_accel += (G * body.m / norm(relative_pos)**3) * relative_pos
        return self.r_accel
    

    def update_vel(self, particles, dt):
        '''
        Actualiza la velocidad a la mitad del intervalo actual ejecutando "comp_accel" para hallar 
        la aceleración.

        :particles: Lista de partículas en la simulación.
        :dt: Longitud del intervalo (step size).
        :return: Velocidad en la mitad del intervalo. Arreglo de numpy de R2.
        '''
        self.comp_accel(particles)
        # Se divide entre 2 para representar que sea la velocidad en la mitad del intervalo.
        self.vel += self.r_accel * dt / 2.0 
        return self.vel
    

    def update_pos(self, dt):
        '''
        Actualiza la posición al final del intervalo actual con la velocidad en la mitad.

        :dt: Longitud del intervalo (step size).
        :return: Posición al final del intervalo. Arreglo de numpy de R2.
        '''
        self.pos += self.vel * dt
        return self.pos