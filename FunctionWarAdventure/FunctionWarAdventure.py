'''
Estoy usando arcade version 2.3.15
'''
import arcade
import math
import random
from arcade.gui import *

SPRITE_SCALING_PLAYER = 0.5
BOSS_SCALLING = 3
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_BOX = 0.5
COIN_COUNT = 25
LIFE = 100 # esto se usara para determinar la vida del personaje

SIZE_WALL = 64 # ESTE ES EL TAMAÑO DE MI BLOQUE . 128*0.5 (OJO)
# ojo estas medidas son de pantalla en pixeles . Las demas medidas se acomodaran a estas medidas primarias
SCREEN_WIDTH = 20*SIZE_WALL # PARA QUE ENCAJE UN NUMEOR ENTERO DE PAREDES , IMPORTANTE (el numero 20 si es arbitrario)
SCREEN_HEIGHT =  13*SIZE_WALL # PARA QUE ENCAJE UN NUMEOR ENTERO DE PAREDES , IMPORTANTE (el 13 si es arbitrario)

MAP_HEIGHT = 13 # el cuantas filas de tamaño (SCALE_TILE_SIZE) tendra de alto mi mapa

BULLET_SPEED_X = 3
BULLET_SPEED_Y = 4

CHANGE_TIME = 0.024

MOVEMENT_SPEED = 7  # la velocidad de movimiento de mi personaje
JUMP_SPEED = 14
GRAVITY = 0.5


# Vamos a crear dos nuevas constantes. No queremos que el jugador llegue al borde de la pantalla
# antes de comenzar a desplazarnos. Porque entonces el jugador no tendría idea de a dónde va
# . En nuestro ejemplo estableceremos un "margen" de 40 píxeles. Cuando el jugador esté a 40 píxeles del
# borde de la pantalla, moveremos el puerto de visualización para que pueda ver al menos 40 píxeles a su alrededor.
# osea para que vea 40 pixeles a su borde antes de que se mueva mas a ese borde .

VIEWPORT_MARGIN = 64
RIGHT_MARGIN = 500

# ----------------------------------------------- ARMAS -------------------------------------------------------


# disparo lineal
class Shoot_lineal(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        # trayectoria de la bala
        self.center_x += self.change_x
        self.center_y = self.inicio_y
        '''
        # Angulo de la bala
        self.division = 0
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)
        
        '''


# Disparo sinoidal
class Shoot_sinoidal(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        # trayectoria de la bala
        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Angulo de la bala
        self.division = math.cos((self.center_x - self.inicio_x) / 100)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)

# Disapro polinomial
class Shoot_polinomial(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        # trayectoria de la bala
        self.center_x += self.change_x
        self.center_y = ((self.center_x - self.inicio_x) / 100)**2 * 100 + self.inicio_y

        # Angulo de la bala
        self.division = 2*((self.center_x - self.inicio_x) / 100)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)


# disparo_logaritmico
class Shoot_log(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        # trayectoria de la bala
        self.center_x += self.change_x
        self.center_y = math.log((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Angulo de la bala
        self.division = 1/( (self.center_x - self.inicio_x) / 100)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)



# diparo_logaritmico
class Shoot_exp(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        # hacemos esto para que se vea que la bala viene de atras del personaje
        '''
        Prueba esto y veras que no cambia las cosas y nose por que no es permitido hacer esto
        debo leer mas la documentacion
        '''

        self.inicio_x = self.center_x   # el new_center_x es el nuevo centro de centro de mi bala
        self.inicio_y = self.center_y

        self.center_x = self.center_x - 200 #  Este sera el lugar donde parte la bala



    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        # trayectoria de la bala
        self.center_x = self.change_x + (self.center_x) # eje x no se suma nada mas
        self.center_y = math.exp((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Angulo de la bala
        self.division = math.exp((self.center_x - self.inicio_x) / 100)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)


# disparo superpoderoso
class Shoot_tan(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)


# barrera_campana
class Shoot_campana(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # su propio tiempo inicia

        self.time = 0
        # conviene ponerlos alli , esto se hara una vez .
        self.inicio_x = 0
        self.inicio_y = 0

        # sera la division , me servira para sacar el angulo
        self.division = 0

    def setup(self):
        self.inicio_x = self.center_x
        self.inicio_y = self.center_y

    def update(self):
        # con esto ya se actualiza con su propio tiempo

        self.time += CHANGE_TIME

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)


# Esta parte es para invocar la explosion en el momento de la colision . Es tambien un objeto
class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, texture_list):
        # hereda todo
        super().__init__()

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list # es una lista de texturas

        self.update() # es necesario esto . indica el inicio de todo

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.

        # actualiza la lista de sprites a mas 1 en cada actualizacion
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists() # cuando termine la lista se borra



# ----------------------------------------------- FUNCIONES IMPORTANTES -------------------------------------------------------

# para convertir el archivo CSV en un mapa
def get_map(filename):
    """
    This function loads an array based on a map stored as a list of
    numbers separated by commas.
    """

    # Open the file
    map_file = open(filename) # leer el mapa

    # Create an empty list of rows that will hold our map
    # crea una lista vacia de filas que mantendra nuestro mapa
    map_array = []

    # Read in a line from the file
    # lee una linea de -1,0,1,2,3
    for line in map_file:

        # Strip the whitespace, and \n at the end
        # eliminar los espacios en blanco y el \n al final de la linea
        line = line.strip()

        # This creates a list by splitting line everywhere there is a comma.
        # crea una lista de elementos separaddos por coma
        map_row = line.split(",")

        # The list currently has all the numbers stored as text, and we want it
        # as a number. (e.g. We want 1 not "1"). So loop through and convert
        # to an integer.

        # esa lista tiene elementos como caracteres , tenemos que transformarlo a entero
        for index, item in enumerate(map_row):
            map_row[index] = int(item)

        # Now that we've completed processing the row, add it to our map array.
        # Ahora que esta completa la lectura . Almacenamos en la lista
        # hemos agregado una lista es decir [ [-1][0] ,..... ]
        map_array.append(map_row)

    # Done, return the map.
    return map_array # retorna la lista de listas

# vamos a dibujar las barras de vida de los jugadores
def barra_de_vida1(nombre,left,right, top, bottom , colorEdge, color , fillporcent ):
    # el texto abajo de la barra de vida
    # el -30 es necesario
    arcade.draw_text(nombre, left, bottom-30 , arcade.color.BLACK, 20)

    # dibujamos la barra de vida , fijate en el tercer argumento
    arcade.draw_lrtb_rectangle_filled(left,left + (right-left)*fillporcent , top, bottom, color)

    # dibujamos el borde de la barra de vida
    arcade.draw_lrtb_rectangle_outline(left,right, top, bottom, colorEdge, 2)

# vamos a dibujar las barras de vida del boss_final
def barra_de_vida2(nombre,left,right, top, bottom , colorEdge, color , fillporcent ):
    # el texto abajo de la barra de vida
    # el -30 es necesario
    arcade.draw_text(nombre, left, bottom-30 , arcade.color.BLACK, 20)

    # dibujamos la barra de vida , fijate en el tercer argumento
    arcade.draw_lrtb_rectangle_filled(left,right , bottom + (top-bottom)*fillporcent, bottom, color)

    # dibujamos el borde de la barra de vida
    arcade.draw_lrtb_rectangle_outline(left,right, top, bottom, colorEdge, 2)

# ----------------------------------------------- OBJETOS-------------------------------------------------------



###################### JUGADOR ###########################

class Player(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma ,
    # con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        # .tipo_de_arma es un numero que va del 1 al 7 .
        # para indicar que arma(function) se esta disparando .
        self.tipo_de_arma = 1 # por defecto es 1 pero podria cambiar depende
        # esto lo usare para el dibujado de trayectoria de puntos
        self.inicio_x = 0
        self.inicio_y = 0
        self.time = 0 # su tiempo del jugador

        self.life = LIFE

        '''
        1 : Personaje viendo hacia la dercha
        0 : Personaje viendo hacia la izquierda 
        '''
        # Lista de texturas (solo habra dos texturas)
        self.textures = []
        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture(filename, mirrored=True)
        self.textures.append(texture)
        # con el segundo argumento hacemos que vea hacia la izquierda, ya que la imagen esta hacia la derecha
        texture = arcade.load_texture(filename)
        self.textures.append(texture)

        # By default, face right.
        self.set_texture(1) #


    def on_update(self,delta_time):

        '''
        # esto si lo pones el objeto en vez de que se mueva +7 se va a mover en cada update +7*(#_de_updates)
        self.center_x += self.change_x
        self.center_y += self.change_y
        '''

        self.time += delta_time

        # Figure out if we should face left or right
        # para establecer cuando deberia cambiar de vista
        if self.change_x < 0:
            self.texture = self.textures[0]
        elif self.change_x > 0:
            self.texture = self.textures[1]


    # Esto sera opcional, es para que encima del personaje se vea el nombre de quien lo este jugando ,
    # sus direcciones hacia a donde apunta .
    # # esta funcion debe llamarse dentro de la funcion on_draw() (OJO) debido al start render
    def draw(self):

        # dibujo del nombre del personaje
        arcade.draw_text("alonso",self.center_x-20,self.center_y+30,arcade.color.BLACK,10)

        # dibujando la trayectorias de donde el jugador puede disparar

        # --------lineal------------
        if self.tipo_de_arma == 1  :
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(30, 180, 30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = 0 + self.inicio_y + 33
                arcade.draw_point(X, Y, (235, 167, 167), 10)

        # -------sinoidal------------
        elif self.tipo_de_arma == 2:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            #dibujamos los puntos
            for change in range(30,180,30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = math.sin((X - self.inicio_x) / 100) * 100 + self.inicio_y +33
                arcade.draw_point(X, Y, (235, 167, 167), 10)
        # -----------polinomial----------
        elif self.tipo_de_arma == 3:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(30, 180, 30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = ((X - self.inicio_x) / 100)**2 * 100 + self.inicio_y + 33
                arcade.draw_point(X, Y, (235, 167, 167), 10)
        # ---------logaritmico------
        elif self.tipo_de_arma == 4:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(30, 180, 30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = math.log((X - self.inicio_x) / 100) * 100 + self.inicio_y + 33
                arcade.draw_point(X, Y, (235, 167, 167), 10)
        # ----------exponencial---------
        elif self.tipo_de_arma == 5:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(-80, 50, 30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = math.exp((X - self.inicio_x) / 100) * 100 + self.inicio_y + 33
                arcade.draw_point(X, Y, (235, 167, 167), 10)
        # ---------tangencial-----------
        elif self.tipo_de_arma == 6:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(30, 180, 30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = math.sin((X - self.inicio_x) / 100) * 100 + self.inicio_y + 33
                arcade.draw_point(X, Y, (235, 167, 167), 10)
        # ----------campana--------------
        elif self.tipo_de_arma == 7:
            self.inicio_x = self.center_x
            self.inicio_y = self.center_y

            # dibujamos los puntos
            for change in range(30,180,30):
                X = change + self.inicio_x
                # ese 33 es debido a que la bala sale de la parte superior de mi personaje (recuerda)
                Y = math.sin((X - self.inicio_x) / 100) * 100 + self.inicio_y +33
                arcade.draw_point(X, Y, (235, 167, 167), 10)




###################### ENEMIGO 1 ###########################

class EnemyWorm(arcade.Sprite):
    # enemigo principal , habra mas de esto pero por ahora solo sera un enemigo simple
    def __init__(self, filename1,filename2, scale):
        super().__init__()

        self.textures = []  # es una lista de texturas para mi sprite
        texture = arcade.load_texture(filename1)
        self.textures.append(texture)
        # para que vea hacia la izquierda .
        texture = arcade.load_texture(filename2)
        self.textures.append(texture)
        # se carga la imagen mirando hacia la derecha , se hace espejo
        texture = arcade.load_texture(filename2, mirrored=True)
        self.textures.append(texture)

        self.scale = scale # la escala de mi personaje

        '''
        0 = lombiz muerta
        1 = izquierda 
        2 = derecha 
        '''
        self.set_texture(2) # la textura inicial
        self.change_x = 3


    def setup(self):

        # Set boundaries on the left/right the enemy can't cross
        # establece los limites de los personajes en el mapa . Fijate que su referencia es relativa al mapa no a el mismo
        self.boundary_right = self.right + SIZE_WALL
        self.boundary_left = self.left - SIZE_WALL

    def on_update(self,delta_time):

        self.center_x += self.change_x

        # If we are out-of-bounds, then 'bounce'
        # haz las correcciones con las paredes , esto eventualmente cambiara cuadno hagas el juego principal
        if  self.left < self.boundary_left:
            self.change_x *= -1
            self.set_texture(2)
        # If the enemy hit the right boundary, reverse
        elif  self.right > self.boundary_right:
            self.change_x *= -1
            self.set_texture(1)


###################### ENEMIGO 2 ###########################

class EnemyRock(arcade.Sprite):
    # enemigo principal , habra mas de esto pero por ahora solo sera un enemigo simple
    def __init__(self, filename1, scale):
        super().__init__(filename1, scale)

        self.change_y = 0

    # no lo elimines o sino tendras errores de codigo
    def setup(self):
        pass

    def on_update(self,delta_time):


        self.center_y += self.change_y

    def activacion_caida(self):
        self.change_y = -20

###################### ENEMIGO 3 ###########################

class EnemyCircularSaw(arcade.Sprite):
    # enemigo principal , habra mas de esto pero por ahora solo sera un enemigo simple
    def __init__(self, filename1, scale):
        super().__init__(filename1, scale)

        self.change_y = 3


    def setup(self):

        # Set boundaries on the left/right the enemy can't cross
        # establece los limites de los personajes en el mapa . Fijate que su referencia es relativa al mapa no a el mismo
        self.boundary_top = self.top + 2*SIZE_WALL
        self.boundary_bottom = self.bottom - 2*SIZE_WALL

    def on_update(self,delta_time):

        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        # haz las correcciones con las paredes , esto eventualmente cambiara cuadno hagas el juego principal
        if  self.bottom < self.boundary_bottom:
            self.change_y *= -1
        # If the enemy hit the right boundary, reverse
        elif  self.top > self.boundary_top:
            self.change_y *= -1




###################### JEFE FINAL ###########################

class FinalBoss(arcade.Sprite):
    # La inteligencia de este enemigo sera dificil de programar pero con fe puedo programarlo
    # con esos tres argumentos (podriamos poner mas) se cargara el estado movil y en movimiento
    def __init__(self, filename1,filename2, scale):
        super().__init__()

        self.textures = []  # es una lista de texturas para mi sprite

        texture = arcade.load_texture(filename1)
        self.textures.append(texture)
        # se carga la imagen normal
        texture = arcade.load_texture(filename2)
        self.textures.append(texture)
        # para que vea hacia la derecha . Se hace espejo
        texture = arcade.load_texture(filename2, mirrored=True)
        self.textures.append(texture)

        self.scale = scale # la escala de mi personaje

        '''
        0 = sin movimiento
        1 = izquierda saltando
        2 = derecha saltando
        '''
        self.set_texture(0) # la textura inicial


        self.time1 = 0 # hace cuenta del tiempo . Esto lo usare para controlar los disparos por segundo
        self.time2 = 0 # lo usare para contar el tiempo entre saltos
        self.bullet = 0 # para los disparos
        # .tipo_de_arma es un numero que va del 1 al 7 .
        # para indicar que arma(function) se esta disparando .
        self.bullet_list = arcade.SpriteList()

        # esctenramnete pasare usare esta variable asi que no te confundas
        self.wall_list = None # le pasare por valor esta lista . Las paredes sera necesario para el control de mi pared
        self.lista_disparos_ajenos = None # disparos dej jugador que afectaran al enemigo
        self.life = LIFE # vida de mi personaje que se reducira
        self.physics_engine = None # Lo usare para que salte


        self.change_x = 7 # para que se mueva el enemigo


        # seria logico establecerlo aca pero te daras cuenta que resulta en errores . mejor haz este comando afuera
        # lo dejo aca para que veas que no va aca este comando . (cuidado)
        self.setup() # tiene que hacese manualmente en esta clase


    def setup(self):
        self.physics_engine = arcade.PhysicsEnginePlatformer(self,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY*2)

    def on_update(self, delta_time):

        # para avanzar el tiempo
        self.time1 += delta_time # para contar el tiempo entre disparos
        self.time2 += delta_time # para contar el tiempo entre salto

        '''
        Mi jefe tendra tres estados ,
        - cuando su vida este en mas del 50% disparara balas hacia arriba , pero estara sobre el suelo
        - cuando su vida este entre 25% y 50%  saltara de lado a lado intentando atacarte en la altura y por debajo
        - cuando su vida este menos de 25% volara y metera emitira bolas que bajan mucha vida . 
        '''

        '''Estado 1'''
        if 0.5*LIFE < self.life <= LIFE:
            if 0.25 * LIFE < self.life <= 0.5 * LIFE:
                # con esto aseguro que se da un disparo cada 1 segundos
                if self.time1 >= 1:
                    self.disparar()



            if self.left <= SIZE_WALL + 2 or self.right >= SCREEN_WIDTH - (SIZE_WALL + 2):
                self.change_x *= -1  # si esta en los limites cambia de posicion

            self.bullet_list.update()
            self.physics_engine.update()  # Se tiene que actualizar


        '''Estado 2'''

        if 0.25*LIFE < self.life <= 0.5*LIFE :
            # con esto aseguro que se da un disparo cada 1 segundos
            if self.time1 >= 1:
                self.disparar()

            self.bullet_list.update()

            # para que salte , ccon esto aseguramos que dara un salto cada 3 segundos
            if self.physics_engine.can_jump() and self.time2 >= 1.5 :
                self.change_y = JUMP_SPEED*2
                self.time2 = 0 # para incializar de nuevo

            self.physics_engine.update() # Se tiene que actualizar

            # si puede saltar pero no salta es por que esta en el suelo por tanto hacemos acciones cuando esta en el suelo
            if self.physics_engine.can_jump():
                self.set_texture(0) # si se encuentra en el suelo cambia a estado de reposo
                if self.left <= SIZE_WALL + 2 or self.right >= SCREEN_WIDTH - (SIZE_WALL+2):
                    self.change_x *= -1 # si esta en los limites cambia de posicion
            elif self.right >= SCREEN_WIDTH - (SIZE_WALL+2) or self.left <= SIZE_WALL+2:
                # acciones cuando esta en el aire y toco los extremos
                if self.change_x > 0:
                    self.set_texture(1)
                else:
                    self.set_texture(2)

                self.change_x *= -1
            else:
                # este caso es el ultimo , es decir no esta en el suelo , en el aire y no este en los extremos
                if self.change_x > 0:
                    self.set_texture(2)
                else:
                    self.set_texture(1)


        '''estado 3'''
        if self.life <= 0.25*LIFE:
            # con esto aseguro que se da un disparo cada 1 segundos
            if self.time1 >= 1:
                self.disparar()

            self.bullet_list.update()


            if self.physics_engine.can_jump() :
                self.change_y = JUMP_SPEED * 2.2

            self.physics_engine.update()  # Se tiene que actualizar

            # si puede saltar pero no salta es por que esta en el suelo por tanto hacemos acciones cuando esta en el suelo


            if self.right >= SCREEN_WIDTH - (SIZE_WALL + 2) or self.left <= SIZE_WALL + 2:
                # acciones cuando esta en el aire o suelo ; y toco los extremos
                if self.change_x > 0:
                    self.set_texture(1)
                else:
                    self.set_texture(2)
                self.change_x *= -1

            if self.top >= SCREEN_HEIGHT-(SIZE_WALL+50):

                print("alonso")
                # en el caso que toque el techo
                if self.change_x > 0:
                    self.center_x += 30
                else:
                    self.center_x -= 30


        '''Acciones en general de los estados'''

        # Este servira para eliminar balas fura de lugar
        for bullet in self.bullet_list:
            # If the bullet flies off-screen, remove it.
            # si un disparo se escapo de la pantalla eliminalo
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            elif bullet.left < 0 +64:
                bullet.remove_from_sprite_lists()
            elif bullet.right > SCREEN_WIDTH :
                bullet.remove_from_sprite_lists()


    def disparar(self):
        bullet = Shoot_lineal("laserRed01.png", SPRITE_SCALING_LASER)

        # rotate it.
        # rotas la imagen
        # como parte rotado la image
        bullet.angle = 90  # lo mantendre en  por ahora

        # Position the bullet
        # comienza de la ubicacion del jugador
        bullet.center_x = self.center_x
        # pero desde la base de la cabeza de mi sprite jugador sale
        bullet.bottom = self.top

        # estableces el setup (inicio)
        bullet.setup()

        # la velocidad con que cambia mi disparo automaticamente
        bullet.change_y = -BULLET_SPEED_Y
        bullet.change_x = -BULLET_SPEED_X

        # Add the bullet to the appropriate lists
        # añade un disparo a la lista
        self.bullet_list.append(bullet)
        self.time1 = 0 # para que la velocidad de disparos se mantenga

    # acciones en caso muera mi personaje
    def death(self):

        # Vaciamos la lista de balas . si desaparece mi personaje tambien debe desaparecer sus balas
        for bullet in self.bullet_list:
            bullet.remove_from_sprite_lists()


###################### MONEDAS ###########################

class Coin(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        self.change_x = random.uniform(-1, 1)
        self.change_y = random.uniform(-1, 1)

        if self.change_x == 0 or self.change_y == 0:
            self.change_x = 0.8
            self.change_y = 0.8

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        # haz las correcciones con las paredes , esto eventualmente cambiara cuadno hagas el juego principal
        if self.left < SIZE_WALL :
            self.change_x *= -1

        if self.right > SCREEN_WIDTH - SIZE_WALL :
            self.change_x *= -1

        if self.bottom < SIZE_WALL:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT - SIZE_WALL:
            self.change_y *= -1

# estas monedas seran para el juego de aventura . No para el tutorial
class Coin2(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)




    def update(self):
        pass

# ----------------------------------------------- Botones de juego-------------------------------------------------------

class BeginButton(TextButton):
    # fijate que se trae el estado del Inicio()
    # fijate que ya esta el texto por predeterminado ,
    def __init__(self, estado, x=0, y=0, width=100, height=40, text="Start", theme=None):
        # fijate lo que hereda .
        super().__init__(x, y, width, height, text, theme=theme)
        self.inicio = estado


    def on_press(self):

        # self.pressed ya esta cuando lo traes cosas del padre
        self.pressed = True

    def on_release(self):
        if self.pressed:

            self.inicio.comenzar_tutorial = True
            self.pressed = False # para no tener problemas

# ----------------------------------------------- ESCENARIOS-------------------------------------------------------

###################### PANTALLA DE INICIO ###########################

class Inicio(arcade.View):
    # el incio de mi juego

    # esto no es parte de arcade.View pero es necesario para mis textos por si lo quiero modificar algun dia
    def __init__(self):
        super().__init__()
        self.theme = None
        self.comenzar_tutorial = False # la condicion que si presiona el boton Start
        self.setup()  # esto es para establecer las condiciones iniciales , lo pondria "on_show()" pero hay problemas si lo pongo alli



    # este es para establecer todos los temas a mi boton , son varias opciones  a analizar
    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        # fijate , self.them es un objeto para botones
        self.theme.add_button_textures(normal, hover, clicked, locked)



    # establecemos como sera el tema de mi boton
    def setup_theme(self):
        # se puede decir que self theme es la el objeto carcasa de mi boton . No el boton en si mismo
        self.theme = arcade.Theme() # revisa la documentacion , es para los botonoes
        self.theme.set_font(24, arcade.color.WHITE)  # establecer la fuente de los textos
        self.set_button_textures()  # metodo anterior

    # para agregar los distintos botones que se usara , aca ya entra que tipo de boton sera
    def set_buttons(self):

        # self.button_list ya esta definido al llamar al padre y se encarga de guardar los botones
        self.button_list.append(BeginButton(self, 60, 570, 110, 50, theme=self.theme)) # solo un boton agregare , fijate que el ultimo argumento se dibuja el tema


    # se llama cuando se llama a inicio , es como setup en arcade.setup()
    # on_show se llama dos veces y no se por que . Eso me causa conflictos asi que aca no pongas creaciones de botones
    def on_show(self):

        # fondo de pantalla
        arcade.set_background_color(arcade.color.WHITE)

    # voy a crear mi setup propio y lo voy a llamar en init para no tener problemas por que on_show se llama dos veces
    def setup(self):
        # la pantalla de incio
        # para estableces los temas y los botones de los metodos antes definidos
        self.setup_theme()
        self.set_buttons()

    
    # dibujare el boton inicio , para comenzar a jugar
    # es necesario que este metodo este para poder comenzar a colorear y dibujar
    def on_draw(self):


        arcade.start_render()
        # dibuja todo lo heredado
        super().on_draw() # con esto traes todas las opciones de botones , osea el dibujado
        arcade.draw_text("FunctionWar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2+200,
                         arcade.color.BLACK, font_size=100, anchor_x="center")
        arcade.draw_text("PRESIONA START PARA COMENZAR ", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

    def update(self, delta_time):


        if self.comenzar_tutorial:

            pantalla_de_tutorial = Tutorial() # creamos un nuevo objeto

            # y nos vamos a la pantalla de tutoriales

            self.window.show_view(pantalla_de_tutorial)  # nose como este metodo puede funcionar


###################### PANTALLA DE TURIAL  ###########################


class Tutorial(arcade.View):

    def __init__(self):
        super().__init__()

        self.player_list = None
        self.coin_list = None  # por el momento como nose crear sprites debo poner las monedas como enemigos
        self.bullet_list = None  # mis balas
        self.wall_list = None  # mi lista para las paredes

        self.player_sprite = None  # el sprite
        self.score = None  # la puntuacion es lo mas importante


        '''
        esto lo elimino ya que arcade.view no tiene esto por defecto 
        # self.set_mouse_visible(False)  # el mouse no debe verse
        '''

        self.time = 0  # este va  a ser mi contador para el tiempo de trabajo

        # This variable holds our simple "physics engine"
        # esta variaable se usara para poder simular una interaccion entre sprites
        self.physics_engine = None

        # Manage the view port
        # Este es para manejar la esquina inferior izquierda de nuestra vista de pantalla .
        self.view_left = 0  # coordenada x
        self.view_bottom = 0  # coordenada y

        self.START_GAME = False # este sera la condicion para pasar al juego principal

        self.setup() # es necesario hacer esto ya que el padre arcade.view no llama setup por defecto


    def setup(self):

        # Establecemos como comenzara el juego
        self.player_list = arcade.SpriteList()  # sera lista de personajes
        self.coin_list = arcade.SpriteList()  # Sera una lista de monedas(enemigos)
        self.bullet_list = arcade.SpriteList()  # Sera una lista de balas
        self.wall_list = arcade.SpriteList()  # Sera una lista de paredes

        self.score = 0  # comenzamos con la anotacion

        self.player_sprite = Player("character.png", SPRITE_SCALING_PLAYER)  # cargamos el personaje

        # lo ubicamos inicialmente
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100

        # lo agregamos a la lista
        self.player_list.append(self.player_sprite)

        ## HACEMOS LO MISMO CON LAS MONEDAS O ENEMIGOS()
        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            # cargamos las monedas
            coin = Coin("coin_01.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            # lo agregamos a la lista
            self.coin_list.append(coin)

        # lista de donde estara ubicado todos mis paredes
        # recuerda que mis imagenes son pixeles de paredes de 128 pixeles
        # Mis bloques son cuadrados de lado 128*0.5= 64 pixeles .
        # necesito dibujar paredes de una forma sencilla

        # Loop through coordinates
        # Dibuja todos mis paredes
        # Recuerda SIZE_WALL = 64
        for x in range(0, SCREEN_WIDTH, SIZE_WALL ):
            if x == 0 or x == SCREEN_WIDTH-SIZE_WALL:
                for y in range(0, SCREEN_HEIGHT , SIZE_WALL ):
                    wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                    # espero no te confundas con .left y .bottom del sprite . eS intuitivo eso
                    wall.left = x
                    wall.bottom = y
                    self.wall_list.append(wall)

            else :
                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.left = x
                wall.bottom = 0
                self.wall_list.append(wall)

                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.left = x
                wall.bottom = SCREEN_HEIGHT - SIZE_WALL
                self.wall_list.append(wall)


        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        # Crea un physics engine (interaccion entre mi jugador y la lista de paredes)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)



    # aca el jugador jugara disparando monedas , se indicara las instrucciones y cuando este listo ira a jugar en el escenario principal
    def on_show(self):

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
            Render the screen.
            """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_text("Tienes armas desde el 1 al 5 \n 1: recta \n 2: sinoidal \n 3 : exp .... hasta 5 \n w (arriba) d(derecha) a(izquierda) s(abajo) click_mouse(disparar)", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=10, anchor_x="center")

        # Draw all the sprites.
        # dibujamos los sprites como lo deseamos
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()
        self.player_sprite.draw() # para dibujar cosas adicionales propio de mi personaje

        # Render the text
        # dibujamos el puntaje en la parte superior derecha
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    # accion cuando se presiona el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        # Create a bullet
        # carga el arma entre tantos que hay
        if self.player_sprite.tipo_de_arma == 1 :
            bullet = Shoot_lineal("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 2 :
            bullet = Shoot_sinoidal("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 3 :
            bullet = Shoot_polinomial("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 4 :
            bullet = Shoot_log("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 5 :
            bullet = Shoot_exp("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 6 :
            bullet = Shoot_tan("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 7 :
            bullet = Shoot_campana("laserBlue01.png", SPRITE_SCALING_LASER)
        # The image points to the right, and we want it to point up. So

        # rotate it.
        # rotas la imagen
        # como parte rotado la image
        bullet.angle = 0

        # Position the bullet
        # comienza de la ubicacion del jugador
        bullet.center_x = self.player_sprite.center_x
        # pero desde la base de la cabeza de mi sprite jugador sale
        bullet.bottom = self.player_sprite.top

        # estableces el setup (inicio)
        bullet.setup()

        # la velocidad con que cambia mi disparo automaticamente
        bullet.change_y = BULLET_SPEED_Y
        bullet.change_x = BULLET_SPEED_X

        # Add the bullet to the appropriate lists
        # añade un disparo a la lista
        self.bullet_list.append(bullet)


    # Si se presiona el teclado (Esto lo usare para el movimiento de mi personaje)
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        '''
        W = UP
        S = DOWN
        A = LEFT
        D = RIGHT
        '''
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    # Cuando se deja de presionar . Para que mi jugador no siga avanzando
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.KEY_1 :
            print("presionaste uno ")
            self.player_sprite.tipo_de_arma = 1
        elif key == arcade.key.KEY_2 :
            print("presionaste dos ")
            self.player_sprite.tipo_de_arma = 2
        elif key == arcade.key.KEY_3 :
            print("presionaste tres ")
            self.player_sprite.tipo_de_arma = 3
        elif key == arcade.key.KEY_4 :
            print("presionaste 4 ")
            self.player_sprite.tipo_de_arma = 4
        elif key == arcade.key.KEY_5 :
            print("presionaste 5 ")
            self.player_sprite.tipo_de_arma = 5
        elif key == arcade.key.KEY_6 :
            print("presionaste 6 ")
            self.player_sprite.tipo_de_arma = 6
        elif key == arcade.key.KEY_7 :
            print("presionaste 7 ")
            self.player_sprite.tipo_de_arma = 7





        # para que el jugador no siga avanzando despues de dejar de presionar
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

        # condidicion final para ver si mi juego continua o no

        if key == arcade.key.ENTER :
            self.START_GAME = True

    # la actualizacion en cada frame
    def update(self, delta_time):

        if self.START_GAME:
            # vaciamos la lista de monedas
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            # Vaciamos la lista de balas
            for bullet in self.bullet_list:
                bullet.remove_from_sprite_lists()
            # vaciamos la lista de parede
            for wall in self.wall_list:
                wall.remove_from_sprite_lists()

            # me doy cuenta de que el ciclo for sigue se pone en segundo plano si no acaba su proceso
            # con este if aseguro de que he borrado todas las cosas de antes . Asi evito sobrecarga de memoria
            if len(self.wall_list) == 0 and len(self.coin_list)==0 and len(self.bullet_list)==0:
                COMENZAR_JUEGO = Juego(self.player_list,self.coin_list,self.bullet_list,self.wall_list) # creamos un nuevo objeto
                # y nos vamos a la pantalla de INICIO DE JUEGO , LLEVANDOME LAS LISTAS A LOS JUGADORES , MONEDAS
                # BALAS . DEBO LIMPIARLAS DE ALGUN MODO PARA NO TENER PROBLEMAS LUEGO CON LA MEMORAIA .

                self.window.show_view(COMENZAR_JUEGO)  # nose como este metodo puede funcionar



        self.time += delta_time

        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.player_list.on_update() # este uso para que mi jugador tenga su tiempo propio
        self.coin_list.update()
        self.bullet_list.update()
        self.physics_engine.update()  # tenemos que actualizar en cada momento como mi personaje interacciona con la lista de paredes

        # Loop through each bullet
        # conviene tener presente todo en una lista ya que podemos tener varias balaar
        for bullet in self.bullet_list:
            # Check this bullet to see if it hit a coin
            # si disparo(s) choca con moneda(s)
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            # If it did, get rid of the bullet
            # si choco elimina la bala  de la lista
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1  # agrega a la puntuacion
            # If the bullet flies off-screen, remove it.
            # si un disparo se escapo de la pantalla eliminalo
            if bullet.bottom > SCREEN_HEIGHT-SIZE_WALL or bullet.right >= SCREEN_WIDTH-SIZE_WALL:
                bullet.remove_from_sprite_lists()


###################### PANTALLA DE JUEGO ###########################


class Juego(arcade.View):
    # El juego principal que es un escenario gigante

    def __init__(self,lista_player,lista_monedas,lista_balas,lista_cajas):

        super().__init__()

        self.player_list = lista_player
        self.coin_list = lista_monedas  # por el momento como nose crear sprites debo poner las monedas como enemigos
        self.bullet_list = lista_balas  # mis balas
        self.wall_list = lista_cajas  # mi lista para las paredes
        self.enemy_list = None # mi lista de enemigos

        self.player_sprite = lista_player[0]  # el sprite
        self.score = None  # la puntuacion es lo mas importante

        '''
        esto lo elimino ya que arcade.view no tiene esto por defecto 
        # self.set_mouse_visible(False)  # el mouse no debe verse
        '''

        self.time = 0  # este va  a ser mi contador para el tiempo de trabajo

        # This variable holds our simple "physics engine"
        # esta variaable se usara para poder simular una interaccion entre sprites
        self.physics_engine = None

        # Manage the view port
        # Este es para manejar la esquina inferior izquierda de nuestra vista de pantalla .
        self.view_left = 0  # coordenada x
        self.view_bottom = 0  # coordenada y

        self.START_FINAL_BOSS = False  # este sera la condicion para pasar al la batalla final
        self.GameOver = False # es para ir a la pantalla de GameOver

        self.setup()  # es necesario hacer esto ya que el padre arcade.view no llama setup por defecto

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.enemy_list = arcade.SpriteList() # sera una lista de sprites

        # Get a 2D array made of numbers based on the map
        # carga tu mapa en formato csv que lo hiciste en Tiled
        # ojo se esta llamando a la funcion get_map() definida arriba
        map_array = get_map("map.csv")

        # Now that we've got the map, loop through and create the sprites
        # ahora que ya tenemos el mapa cargado , en cada ciclo creamos los sprites
        for row_index in range(len(map_array)):
            # espero se entienda como se esta haciendo el loop , (ANALIZA)
            for column_index in range(len(map_array[row_index])):
                # row_index = fila  , colum_index = columna
                item = map_array[row_index][column_index]

                # For this map, the numbers represent:
                # -1 = empty
                # 0  = box
                # 1  = grass left edge
                # 2  = grass middle
                # 3  = grass right edge
                if item == 0:
                    wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                elif item == 1:
                    wall = arcade.Sprite("grassLeft.png", SPRITE_SCALING_BOX)
                elif item == 2:
                    wall = arcade.Sprite("grassMid.png", SPRITE_SCALING_BOX)
                elif item == 3:
                    wall = arcade.Sprite("grassRight.png", SPRITE_SCALING_BOX)
                elif item == 4:
                    enemy = EnemyWorm("wormGreen_move.png","wormGreen_move.png",SPRITE_SCALING_BOX)
                elif item == 5:
                    coin = Coin2("coin_01.png",SPRITE_SCALING_COIN)
                elif item == 6:
                    enemy = EnemyCircularSaw("saw.png", SPRITE_SCALING_BOX)
                elif item == 7:
                    enemy = EnemyRock("meteorGrey_big4.png", SPRITE_SCALING_BOX)

                if 0 <=item < 4:
                    # Calculate where the sprite goes
                    # calcula donde el sprite va
                    wall.left = column_index * SIZE_WALL  # calacula donde estara la parte izquierda
                    wall.top = (MAP_HEIGHT - row_index) * SIZE_WALL  # calcula la parte superior . MAP_HEIGHT es 13 , fijalte por que es asi . NO es dificil
                    # Add the sprite
                    self.wall_list.append(wall)  # agrega a a la lista
                elif item == 4 or item==6 or item==7 :
                    enemy.left = column_index * SIZE_WALL  # calacula donde estara la parte izquierda
                    enemy.top = (MAP_HEIGHT - row_index) * SIZE_WALL # calcula la parte superior . MAP_HEIGHT es 13 , fijalte por que es asi . NO es dificil
                    enemy.setup()  # para definir los limites de movimiento de mi personaje
                    # add the sprite
                    self.enemy_list.append(enemy)
                elif item == 5:
                    # Calculate where the sprite goes
                    # calcula donde el sprite va
                    coin.center_x = (column_index+1/2) * SIZE_WALL  # calacula donde estara la parte izquierda
                    coin.center_y = ( MAP_HEIGHT - row_index-1/2) * SIZE_WALL  # calcula la parte superior . MAP_HEIGHT es 13 , fijalte por que es asi . NO es dificil
                    # Add the sprite
                    self.coin_list.append(coin)  # agrega a a la lista

        # Create out platformer physics engine with gravity

        # la fisica entre mi Sprite y las paredes
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the view port boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        
        # Draw all the sprites.
        # dibuja paredes y el jugador
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        # movimientos de mi jugador
        if key == arcade.key.W:
            # This line below is new. It checks to make sure there is a platform underneath
            # the player. Because you can't jump if there isn't ground beneath your feet.
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # fijate que no altera como en eje y por que eso ya lo hace el salto
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.player_list.on_update()  # este uso para que mi jugador tenga su tiempo propio
        self.coin_list.update()
        self.enemy_list.on_update() # el on_update uso . recuerda esto
        self.physics_engine.update()  # tenemos que actualizar en cada momento como mi personaje interacciona con la lista de paredes


        for enemy in self.enemy_list:

            # registra si eres un enemigo tipo roca y si el jugador esta adelantado a la posicion de ese enemigo
            # si es asi entonces activa lal caida de la roca
            if isinstance(enemy,EnemyRock) and (enemy.center_x < self.player_sprite.center_x):
                enemy.activacion_caida()

            # se acabo automaticamente si el jugador es tocado por alguien
            if  arcade.check_for_collision(enemy, self.player_sprite):
                self.GameOver = True
                break


        # --- Manage Scrolling ---
        # Track if we need to change the view port
        changed = False

        # Scroll left
        left_bndry = self.view_left + RIGHT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True
        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True
        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True
        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True
        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


        # te vas a la pantalla de GameOver
        if self.GameOver:
            # aca si tenemos que hacer una limpieza total
            for player in self.player_list:
                player.remove_from_sprite_lists()
            # vaciamos la lista de monedas
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            # Vaciamos la lista de balas
            for bullet in self.bullet_list:
                bullet.remove_from_sprite_lists()
            # vaciamos la lista de parede
            for wall in self.wall_list:
                wall.remove_from_sprite_lists()
            for enemy in self.enemy_list:
                enemy.remove_from_sprite_lists()



            # me doy cuenta de que el ciclo for sigue se pone en segundo plano si no acaba su proceso
            # con este if aseguro de que he borrado todas las cosas de antes . Asi evito sobrecarga de memoria
            if len(self.wall_list) == 0 and len(self.coin_list) == 0 and len(self.bullet_list) == 0 and \
                    len(self.player_list) == 0 and len(self.enemy_list) == 0:
                # no te olvides de regresar el enfoque de camara a la normalidad
                arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
                Gameover = GameOver()  # creamos un nuevo objeto
                # y nos vamos a la pantalla de INICIO DE JUEGO , sin llevarnos  LISTAS A LOS JUGADORES , MONEDAS
                # BALAS . DEBO LIMPIARLAS DE ALGUN MODO PARA NO TENER PROBLEMAS LUEGO CON LA MEMORAIA .

                self.window.show_view(Gameover)  # nose como este metodo puede funcionar



        # mi condicion si el jugador llega a conseguir llegar a la meta
        if  SIZE_WALL*10  < self.player_sprite.center_x:
            self.START_FINAL_BOSS = True

        # te vas a la pelea de la batalla final
        if self.START_FINAL_BOSS:
            # aca si tenemos que hacer una limpieza total
            for player in self.player_list:
                player.remove_from_sprite_lists()
            # vaciamos la lista de monedas
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            # Vaciamos la lista de balas
            for bullet in self.bullet_list:
                bullet.remove_from_sprite_lists()
            # vaciamos la lista de parede
            for wall in self.wall_list:
                wall.remove_from_sprite_lists()

            # no te olvides de regresar el enfoque de camara a la normalidad
            arcade.set_viewport(0,SCREEN_WIDTH ,0,SCREEN_HEIGHT )

            # me doy cuenta de que el ciclo for sigue se pone en segundo plano si no acaba su proceso
            # con este if aseguro de que he borrado todas las cosas de antes . Asi evito sobrecarga de memoria
            if len(self.wall_list) == 0 and len(self.coin_list) == 0 and len(self.bullet_list) == 0 and len(self.player_list)==0:
                Pantalla_de_carga = PantallaDeCarga()  # creamos un nuevo objeto
                # y nos vamos a la pantalla de INICIO DE JUEGO , sin llevarnos  LISTAS A LOS JUGADORES , MONEDAS
                # BALAS . DEBO LIMPIARLAS DE ALGUN MODO PARA NO TENER PROBLEMAS LUEGO CON LA MEMORAIA .

                self.window.show_view(Pantalla_de_carga)  # nose como este metodo puede funcionar



###################### PANTALLA DE BATALLA FINAL ###########################

class FinalBattle(arcade.View):
    # escenario final donde el jefe se encuentra y te quiere matar . Tiene mecanicas especificas
    def __init__(self,explosiones_list):

        super().__init__()



        self.player_list = None
        self.coin_list = None  # por el momento como nose crear sprites debo poner las monedas como enemigos
        self.bullet_list = None  # mis balas
        self.wall_list = None  # mi lista para las paredes
        self.enemy_list = None # mi lista de enemigos
        self.explosions_list = explosiones_list  # lista de explosiones

        self.player_sprite = None  # el sprite
        self.boss_final = None # jefe final
        self.score = None  # la puntuacion es lo mas importante

        '''
        esto lo elimino ya que arcade.view no tiene esto por defecto 
        # self.set_mouse_visible(False)  # el mouse no debe verse
        '''



        self.time = 0  # este va  a ser mi contador para el tiempo de trabajo

        # This variable holds our simple "physics engine"
        # esta variaable se usara para poder simular una interaccion entre sprites
        self.physics_engine = None

        # Manage the view port
        # Este es para manejar la esquina inferior izquierda de nuestra vista de pantalla .
        self.view_left = 0  # coordenada x
        self.view_bottom = 0  # coordenada y

        # Pre-load the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []  # sera la lista que almacene los frames de la animacion

        # establece las dimensiones de mi explosion
        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = "explosion.png"

        # los argumentos de load_spritesheet son ( filename , Posición X del área de recorte de la textura
        # ,Posición Y del área de recorte de la textura. , numero de mosaicos de ancho que es la imagen,
        # numero de mosacios en la imagen)
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        # el sonido de las explosiones
        self.hit_sound = arcade.sound.load_sound("explosion2.wav") # LO PONGO ACA Y NO EN SETUP() .



        self.FINAL_GAME = False  # este sera la condicion para pasar al juego principal


        self.setup()  # es necesario hacer esto ya que el padre arcade.view no llama setup por defecto


    def setup(self):




        # Establecemos como comenzara el juego
        self.player_list = arcade.SpriteList()  # sera lista de personajes
        self.coin_list = arcade.SpriteList()  # Sera una lista de monedas(enemigos)
        self.bullet_list = arcade.SpriteList()  # Sera una lista de balas
        self.wall_list = arcade.SpriteList()  # Sera una lista de paredes
        self.enemy_list = arcade.SpriteList() # sera una lista de enemigos (por ahora solo creare un enemigo)






        self.score = 0  # comenzamos con la anotacion

        self.player_sprite = Player("character.png", SPRITE_SCALING_PLAYER)  # cargamos el personaje

        # lo ubicamos inicialmente
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 100

        # lo agregamos a la lista
        self.player_list.append(self.player_sprite)

        # creare mi boss_final
        self.boss_final = FinalBoss("frog.png","frog_move.png", BOSS_SCALLING)  # cargamos el jefe final
        self.boss_final.wall_list = self.wall_list # ambas tendran la misma lista de paredes , lo cual es conveniente
        self.boss_final.setup() # para establecer la mecanica de salto
        self.boss_final.center_x = 800
        self.boss_final.center_y = 400

        # lo agregamos
        self.enemy_list.append(self.boss_final)

        # lista de donde estara ubicado todos mis paredes
        # recuerda que mis imagenes son pixeles de paredes de 128 pixeles
        # Mis bloques son cuadrados de lado 128*0.5= 64 pixeles .
        # necesito dibujar paredes de una forma sencilla

        # Loop through coordinates
        # Dibuja todos mis paredes
        # Recuerda SIZE_WALL = 64
        for x in range(0, SCREEN_WIDTH, SIZE_WALL ):
            if x == 0 or x == SCREEN_WIDTH-SIZE_WALL:
                for y in range(0, SCREEN_HEIGHT , SIZE_WALL ):
                    wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                    # espero no te confundas con .left y .bottom del sprite . eS intuitivo eso
                    wall.left = x
                    wall.bottom = y
                    self.wall_list.append(wall)

            else :
                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.left = x
                wall.bottom = 0
                self.wall_list.append(wall)

                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.left = x
                wall.bottom = SCREEN_HEIGHT - SIZE_WALL
                self.wall_list.append(wall)


        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        # Crea un physics engine (interaccion entre mi jugador y la lista de paredes)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)



    # aca el jugador jugara disparando monedas , se indicara las instrucciones y cuando este listo ira a jugar en el escenario principal
    def on_show(self):

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
            Render the screen.
        """


        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_text("Tienes armas desde el 1 al 5 \n 1: recta \n 2: sinoidal \n 3 : exp .... hasta 5 \n w (arriba) d(derecha) a(izquierda) s(abajo) click_mouse(disparar)", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=10, anchor_x="center")

        # Draw all the sprites.
        # dibujamos los sprites como lo deseamos
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()
        self.enemy_list.draw()
        self.boss_final.bullet_list.draw() # para que dibuje las balas que emite el enemigo
        self.explosions_list.draw() # DIBUJAR LA LISTA DE EXPLOSIONES

        # Render the text
        # dibujamos el puntaje en la parte superior derecha
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

        # dibujamos barra del vida del player
        # aunque la division no es entera no causa problemas en el dibujado
        porcentaje1 = self.player_sprite.life / LIFE
        barra_de_vida1("Alonso Alcala",SIZE_WALL,SIZE_WALL+300,SCREEN_HEIGHT-30,SCREEN_HEIGHT-SIZE_WALL,arcade.color.BLACK,
                      (0, 171, 102) , porcentaje1)

        # dibujamos barra del vida del player
        # aunque la division no es entera no causa problemas en el dibujado
        porcentaje2 = self.boss_final.life / LIFE
        barra_de_vida2("BOSS", SCREEN_WIDTH-SIZE_WALL, SCREEN_WIDTH-10 , SCREEN_HEIGHT - 2*SIZE_WALL ,
                       SCREEN_HEIGHT - 10*SIZE_WALL, arcade.color.BLACK, 	(65, 68, 224), porcentaje2)

    # accion cuando se presiona el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        # carga el arma entre tantos que hay



        if self.player_sprite.tipo_de_arma == 1 :
            bullet = Shoot_lineal("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 2 :
            bullet = Shoot_sinoidal("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 3 :
            bullet = Shoot_polinomial("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 4 :
            bullet = Shoot_log("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 5 :
            bullet = Shoot_exp("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 6 :
            bullet = Shoot_tan("laserBlue01.png", SPRITE_SCALING_LASER)
        elif self.player_sprite.tipo_de_arma == 7 :
            bullet = Shoot_campana("laserBlue01.png", SPRITE_SCALING_LASER)






        # The image points to the right, and we want it to point up. So

        # rotate it.
        # rotas la imagen
        # como parte rotado la image
        bullet.angle = 0

        # Position the bullet
        # comienza de la ubicacion del jugador
        bullet.center_x = self.player_sprite.center_x
        # pero desde la base de la cabeza de mi sprite jugador sale
        bullet.bottom = self.player_sprite.top

        # estableces el setup (inicio)
        bullet.setup()

        # la velocidad con que cambia mi disparo automaticamente
        bullet.change_y = BULLET_SPEED_Y
        bullet.change_x = BULLET_SPEED_X

        # Add the bullet to the appropriate lists
        # añade un disparo a la lista
        self.bullet_list.append(bullet)


    # Si se presiona el teclado (Esto lo usare para el movimiento de mi personaje)
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        '''
        W = UP
        S = DOWN
        A = LEFT
        D = RIGHT
        '''

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    # Cuando se deja de presionar . Para que mi jugador no siga avanzando
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.KEY_1 :
            print("presionaste uno ")
            self.player_sprite.tipo_de_arma = 1
        elif key == arcade.key.KEY_2 :
            print("presionaste dos ")
            self.player_sprite.tipo_de_arma = 2
        elif key == arcade.key.KEY_3 :
            print("presionaste tres ")
            self.player_sprite.tipo_de_arma = 3
        elif key == arcade.key.KEY_4 :
            print("presionaste 4 ")
            self.player_sprite.tipo_de_arma = 4
        elif key == arcade.key.KEY_5 :
            print("presionaste 5 ")
            self.player_sprite.tipo_de_arma = 5
        elif key == arcade.key.KEY_6 :
            print("presionaste 6 ")
            self.player_sprite.tipo_de_arma = 6
        elif key == arcade.key.KEY_7 :
            print("presionaste 7 ")
            self.player_sprite.tipo_de_arma = 7





        # para que el jugador no siga avanzando despues de dejar de presionar
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

        # condidicion final para ver si mi juego continua o no

        if key == arcade.key.ENTER :
            self.START_GAME = True

    # la actualizacion en cada frame
    def update(self, delta_time):


        # por si que pasa si mi jugador muere o consigue derrotar al enemigo
        if self.FINAL_GAME:


            # vaciamos la lista de monedas
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()

            # Vaciamos la lista de balas
            for bullet in self.bullet_list:
                bullet.remove_from_sprite_lists()

            # vaciamos la lista de parede
            for wall in self.wall_list:
                wall.remove_from_sprite_lists()

            print("JUEGO TERMINADO")

        self.time += delta_time

        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.player_list.on_update() # el on_update es para que mi personaje tenga tiempo propio
        self.coin_list.update()
        self.bullet_list.update()
        self.enemy_list.on_update() # on update uso por que el tiempo tiene interes para mi con el enemigo
        self.physics_engine.update()  # tenemos que actualizar en cada momento como mi personaje interacciona con la lista de paredes
        self.explosions_list.update() # se actualiza las explosiones

        # Loop through each bullet
        # conviene tener presente todo en una lista ya que podemos tener varias balaar
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit el boss final with a bullet
            # If it did, get rid of the bullet
            # si choco elimina la bala  de la lista
            # aca estara los comandos que hara que le baje vida al enemigo
            # El enemigo aunque si lo eliminamos y no se dibuje sigue existiendo asi que con la segunda condicion
            # aseguramos que su existencia no lo tomaremos en cuenta con las balas .
            if arcade.check_for_collision(self.boss_final, bullet) and self.boss_final in self.enemy_list:


                self.boss_final.life -= 10 # restamos 10 de vida

                # Make an explosiona
                # se carga la explosion
                explosion = Explosion(self.explosion_texture_list)

                # Move it to the location of the coin
                # la explosion comienza en el origen de la moneda
                explosion.center_x = bullet.center_x
                explosion.center_y = bullet.center_y


                # Add to a list of sprites that are explosions
                # agrega a la lista
                self.explosions_list.append(explosion) # hay un problema aca que hace lento cuando se inicia las explosiones

                # el sonido no debes olvidar
                arcade.sound.play_sound(self.hit_sound)

                # Get rid of the bullet
                # se borra la bala
                bullet.remove_from_sprite_lists()


            # If the bullet flies off-screen, remove it.
            # si un disparo se escapo de la pantalla, eliminalo
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
            elif bullet.left < 0 +64:
                bullet.remove_from_sprite_lists()
            elif bullet.right > SCREEN_WIDTH :
                bullet.remove_from_sprite_lists()

        # Por si el juego termina
        if  arcade.check_for_collision_with_list( self.player_sprite, self.enemy_list):
            self.player_sprite.life -= 0.5
            # si su vida se acaba muere mi personaje
            if self.player_sprite.life <= 0 :
                self.FINAL_GAME = True


        # Por si es derrotado
        if self.boss_final.life <= 0 :
            self.boss_final.remove_from_sprite_lists() # muere mi personaje
            self.boss_final.death() # y muere todo lo que le pertenecia al boss


        # Ese atributo indica si los disparos que lanzo el enemigo lo toco a mi compañero
        # se tiene un tiempo de retardo de cuando la maquina se entere de que ya no estan los dos sprites superpuestos
        # por tanto se tiene que hacer una forma de corregir eso .
        # la unica manera que se me ocurre es bajarle como la vida disminuye
        if arcade.check_for_collision_with_list( self.player_sprite , self.boss_final.bullet_list ):
            self.player_sprite.life -= 0.4
            # si su vida se acaba muere mi personaje
            if self.player_sprite.life <= 0:
                self.FINAL_GAME = True

########################################### Pantallas opcionales ################################


# ------------------------------------- DESEAS CONTINUAR o GAME_OVER -------------------------
class GameOver(arcade.View):
    # el incio de mi juego

    # esto no es parte de arcade.View pero es necesario para mis textos por si lo quiero modificar algun dia
    def __init__(self):
        super().__init__()
        self.theme = None
        self.comenzar_tutorial = False  # la condicion que si presiona el boton Start
        self.setup()  # esto es para establecer las condiciones iniciales , lo pondria "on_show()" pero hay problemas si lo pongo alli

    # este es para establecer todos los temas a mi boton , son varias opciones  a analizar
    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        # fijate , self.them es un objeto para botones
        self.theme.add_button_textures(normal, hover, clicked, locked)

    # establecemos como sera el tema de mi boton
    def setup_theme(self):
        # se puede decir que self theme es la el objeto carcasa de mi boton . No el boton en si mismo
        self.theme = arcade.Theme()  # revisa la documentacion , es para los botonoes
        self.theme.set_font(24, arcade.color.WHITE)  # establecer la fuente de los textos
        self.set_button_textures()  # metodo anterior

    # para agregar los distintos botones que se usara , aca ya entra que tipo de boton sera
    def set_buttons(self):
        # self.button_list ya esta definido al llamar al padre y se encarga de guardar los botones
        self.button_list.append(BeginButton(self, 60, 570, 110, 50,
                                            theme=self.theme))  # solo un boton agregare , fijate que el ultimo argumento se dibuja el tema

    # se llama cuando se llama a inicio , es como setup en arcade.setup()
    # on_show se llama dos veces y no se por que . Eso me causa conflictos asi que aca no pongas creaciones de botones
    def on_show(self):
        # fondo de pantalla
        arcade.set_background_color(arcade.color.WHITE)

    # voy a crear mi setup propio y lo voy a llamar en init para no tener problemas por que on_show se llama dos veces
    def setup(self):
        # la pantalla de incio
        # para estableces los temas y los botones de los metodos antes definidos
        self.setup_theme()
        self.set_buttons()

    # dibujare el boton inicio , para comenzar a jugar
    # es necesario que este metodo este para poder comenzar a colorear y dibujar
    def on_draw(self):

        arcade.start_render()
        # dibuja todo lo heredado
        super().on_draw()  # con esto traes todas las opciones de botones , osea el dibujado
        arcade.draw_text("FunctionWar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.BLACK, font_size=100, anchor_x="center")
        arcade.draw_text("PRESIONA START PARA COMENZAR ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

    def update(self, delta_time):

        if self.comenzar_tutorial:
            print("hola")
            JuegoNuevo = Tutorial()  # creamos un nuevo objeto
            # y nos vamos a la pantalla de tutoriales
            self.window.show_view(JuegoNuevo)  # nose como este metodo puede funcionar

# ------------------------------------- VICTORIA ----------------------------------
class Victoria(arcade.View):
    # el incio de mi juego

    # esto no es parte de arcade.View pero es necesario para mis textos por si lo quiero modificar algun dia
    def __init__(self):
        super().__init__()
        self.theme = None
        self.comenzar_tutorial = False  # la condicion que si presiona el boton Start
        self.setup()  # esto es para establecer las condiciones iniciales , lo pondria "on_show()" pero hay problemas si lo pongo alli

    # este es para establecer todos los temas a mi boton , son varias opciones  a analizar
    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        # fijate , self.them es un objeto para botones
        self.theme.add_button_textures(normal, hover, clicked, locked)

    # establecemos como sera el tema de mi boton
    def setup_theme(self):
        # se puede decir que self theme es la el objeto carcasa de mi boton . No el boton en si mismo
        self.theme = arcade.Theme()  # revisa la documentacion , es para los botonoes
        self.theme.set_font(24, arcade.color.WHITE)  # establecer la fuente de los textos
        self.set_button_textures()  # metodo anterior

    # para agregar los distintos botones que se usara , aca ya entra que tipo de boton sera
    def set_buttons(self):
        # self.button_list ya esta definido al llamar al padre y se encarga de guardar los botones
        self.button_list.append(BeginButton(self, 60, 570, 110, 50,
                                            theme=self.theme))  # solo un boton agregare , fijate que el ultimo argumento se dibuja el tema

    # se llama cuando se llama a inicio , es como setup en arcade.setup()
    # on_show se llama dos veces y no se por que . Eso me causa conflictos asi que aca no pongas creaciones de botones
    def on_show(self):
        # fondo de pantalla
        arcade.set_background_color(arcade.color.WHITE)

    # voy a crear mi setup propio y lo voy a llamar en init para no tener problemas por que on_show se llama dos veces
    def setup(self):
        # la pantalla de incio
        # para estableces los temas y los botones de los metodos antes definidos
        self.setup_theme()
        self.set_buttons()

    # dibujare el boton inicio , para comenzar a jugar
    # es necesario que este metodo este para poder comenzar a colorear y dibujar
    def on_draw(self):
        arcade.start_render()
        # dibuja todo lo heredado
        super().on_draw()  # con esto traes todas las opciones de botones , osea el dibujado
        arcade.draw_text("FunctionWar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.BLACK, font_size=100, anchor_x="center")
        arcade.draw_text("PRESIONA START PARA COMENZAR ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

    def update(self, delta_time):
        if self.comenzar_tutorial:
            pantalla_de_tutorial = Tutorial()  # creamos un nuevo objeto

            # y nos vamos a la pantalla de tutoriales

            self.window.show_view(pantalla_de_tutorial)  # nose como este metodo puede funcionar


class PantallaDeCarga(arcade.View):
    # el incio de mi juego

    # esto no es parte de arcade.View pero es necesario para mis textos por si lo quiero modificar algun dia
    def __init__(self):
        super().__init__()
        self.theme = None
        self.comenzar_tutorial = False  # la condicion que si presiona el boton Start
        self.no = True
        self.setup()  # esto es para establecer las condiciones iniciales , lo pondria "on_show()" pero hay problemas si lo pongo alli
        self.explosions_list = arcade.SpriteList()

        # Pre-load the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []  # sera la lista que almacene los frames de la animacion

        # establece las dimensiones de mi explosion
        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = "explosion.png"

        # los argumentos de load_spritesheet son ( filename , Posición X del área de recorte de la textura
        # ,Posición Y del área de recorte de la textura. , numero de mosaicos de ancho que es la imagen,
        # numero de mosacios en la imagen)
        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

    # este es para establecer todos los temas a mi boton , son varias opciones  a analizar
    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        # fijate , self.them es un objeto para botones
        self.theme.add_button_textures(normal, hover, clicked, locked)

    # establecemos como sera el tema de mi boton
    def setup_theme(self):
        # se puede decir que self theme es la el objeto carcasa de mi boton . No el boton en si mismo
        self.theme = arcade.Theme()  # revisa la documentacion , es para los botonoes
        self.theme.set_font(24, arcade.color.WHITE)  # establecer la fuente de los textos
        self.set_button_textures()  # metodo anterior

    # para agregar los distintos botones que se usara , aca ya entra que tipo de boton sera
    def set_buttons(self):
        # self.button_list ya esta definido al llamar al padre y se encarga de guardar los botones
        self.button_list.append(BeginButton(self, 60, 570, 110, 50,
                                            theme=self.theme))  # solo un boton agregare , fijate que el ultimo argumento se dibuja el tema

    # se llama cuando se llama a inicio , es como setup en arcade.setup()
    # on_show se llama dos veces y no se por que . Eso me causa conflictos asi que aca no pongas creaciones de botones
    def on_show(self):
        # fondo de pantalla
        arcade.set_background_color(arcade.color.WHITE)

    # voy a crear mi setup propio y lo voy a llamar en init para no tener problemas por que on_show se llama dos veces
    def setup(self):
        # la pantalla de incio
        # para estableces los temas y los botones de los metodos antes definidos
        self.setup_theme()
        self.set_buttons()

    # dibujare el boton inicio , para comenzar a jugar
    # es necesario que este metodo este para poder comenzar a colorear y dibujar
    def on_draw(self):
        arcade.start_render()
        # dibuja todo lo heredado
        super().on_draw()  # con esto traes todas las opciones de botones , osea el dibujado
        arcade.draw_text("FunctionWar", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200,
                         arcade.color.BLACK, font_size=100, anchor_x="center")
        arcade.draw_text("PRESIONA START PARA COMENZAR ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        self.explosions_list.draw()


    def update(self, delta_time):
        self.explosions_list.update()  # se actualiza las explosiones
        if self.no:
            # Make an explosiona
            # se carga la explosion
            explosion = Explosion(self.explosion_texture_list)
            # Move it to the location of the coin
            # la explosion comienza en el origen de la moneda
            explosion.center_x = 100
            explosion.center_y = 100
            # Add to a list of sprites that are explosions
            # agrega a la lista
            self.explosions_list.append(explosion)  # hay un problema aca que hace lento cuando se inicia las explosiones
            self.no = False

        if self.comenzar_tutorial:
            BatallaFinal = FinalBattle(self.explosions_list)  # creamos un nuevo objeto
            # y nos vamos a la pantalla de tutoriales

            self.window.show_view(BatallaFinal)  # nose como este metodo puede funcionar




# ----------------------------------------------- COMANDO PARA INICIAR JUEGO ------------------------------------------------------



def main():
    # en que pantalla comienza
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "FunctionWarAdventure")
    window.total_score = 0 # cuantas monedas va a recolectar el jugador durante toda la partida para mostrarlas al final


    # Esto es el codigo oficial , lo omito para fines de crear el escenario final
    pantalla_inicio = Inicio()
    window.show_view(pantalla_inicio)
    arcade.run()



    '''
    # esto es para pasarme directo al jefe final . tiene fines de prueba esta parte
    
    final = FinalBattle()
    window.show_view(final)
    arcade.run()      
    '''








if __name__ == "__main__":
    main()







# ----------------------------------------------- ESTRUCTURA DE MI VIDEOJUEGO-------------------------------------------------------




'''

# Estructura de mi juego ...........

1 .- Definir todas las funciones que el jugador podra disponer , Averigua como escoger una funcion que devuelva funciones . Eso me vendra bine . lo hice con los propios metodos del player
2 .- Definir los objetos(sprites) de mi juego , osea que podran hacer , cuales seran sus actualizaciones 
3 .- Definir los las pantalla de inicio
4 .- Definir la pantalla de tutorial que a la vez son de instrucciones de juego , aca el jugador escogera 3 armas(funciones de 10) . 
5 .- Definir el juego  principal 
        - Crear el mapa en tiled 
        - Crear la logica del juego 
        - Como y que pasara cuando el jugador llegue a la escena final , tambien las monedas que se necesite 
6 .- Definir la moneda final . Es decir Cuando llegue al centro del escenario se pasara a otra plataforma
7 .- Esa plataforma estara el jefe final , este jefe final es un super_sprite que debes diseñar o buscar . Tiene que tener significado con lo que inventas ojo . 
8 .- Y la pantalla de victoria , que es lo que hara el jugador , y que es lo que conseguira . Que ganara como trofeo para presumirlo 

'''


