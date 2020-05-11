import arcade
import math
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_BOX = 0.5
COIN_COUNT = 25

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

BULLET_SPEED_X =4
BULLET_SPEED_Y = 4

CHANGE_TIME = 0.024

MOVEMENT_SPEED = 5 # la velocidad de movimiento de mi personaje


# Vamos a crear dos nuevas constantes. No queremos que el jugador llegue al borde de la pantalla
# antes de comenzar a desplazarnos. Porque entonces el jugador no tendría idea de a dónde va
# . En nuestro ejemplo estableceremos un "margen" de 40 píxeles. Cuando el jugador esté a 40 píxeles del
# borde de la pantalla, moveremos el puerto de visualización para que pueda ver al menos 40 píxeles a su alrededor.
# osea para que vea 40 pixeles a su borde antes de que se mueva mas a ese borde .
VIEWPORT_MARGIN = 40 # El margen

class Player(arcade.Sprite):

    def update(self):
        pass




class Gun(arcade.Sprite):

    pass



class Bullet(arcade.Sprite):

    # es necesario ponerlo de esa forma , ya que llamamos al padre de esa forma , con esos dos argumentos (podriamos poner mas) habra que probar todos los resultados
    def __init__(self,filename,scale):
        super().__init__(filename,scale)


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

        self.time +=  CHANGE_TIME


        self.center_x += self.change_x
        self.center_y =  math.sin( (self.center_x - self.inicio_x)/100 )*100  + self.inicio_y


        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = ( self.center_x - self.inicio_x ) / (self.center_y - self.inicio_y )
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(  angulo_radians  )










class Coin(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        self.change_x = random.uniform(-1, 1)
        self.change_y = random.uniform(-1, 1)

        if self.change_x == 0  or self.change_y == 0 :
            self.change_x = 0.5
            self.change_y = 0.5

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1





class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Function War")


        self.player_list = None
        self.coin_list = None # por el momento como nose crear sprites debo poner las monedas como enemigos
        self.bullet_list = None # mis balas
        self.wall_list = None # mi lista para las paredes


        self.player_sprite = None # el sprite
        self.score = None # la puntuacion es lo mas importante

        self.set_mouse_visible(False) # el mouse no debe verse

        self.time = 0 # este va  a ser mi contador para el tiempo de trabajo

        # This variable holds our simple "physics engine"
        # esta variaable se usara para poder simular una interaccion entre sprites
        self.physics_engine = None

        # Manage the view port
        # Este es para manejar la esquina inferior izquierda de nuestra vista de pantalla .
        self.view_left = 0   # coordenada x
        self.view_bottom = 0 # coordenada y



    def setup(self):

        # Establecemos como comenzara el juego
        self.player_list = arcade.SpriteList() # sera lista de personajes
        self.coin_list = arcade.SpriteList() # Sera una lista de monedas(enemigos)
        self.bullet_list = arcade.SpriteList() # Sera una lista de balas
        self.wall_list = arcade.SpriteList() # Sera una lista de paredes





        self.score = 0 # comenzamos con la anotacion

        self.player_sprite = Player("character.png",SPRITE_SCALING_PLAYER) # cargamos el personaje

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
        # Mis bloques son cuadrados de lado 64 pixeles . Aun nose por que pero creo que 0.5 de la medida de "SCALING BOX "
        coordinate_list = [[470, 500],
                    [400, 570],
                    [470, 570],
                    [100,70],
                    [100,140],
                    [100, 210],
                    [100, 280],
                    [100, 350],
                    [100, 420],
                    [100, 490],
                    [100, 560],
                    [100, 490],
                    [100, 560],
                    [100, 630],
                    [100, 700],
                    [100, 770],
                    [100, 840],
                    [100, 910]
        ]

        # Loop through coordinates
        # Dibuja todos mis paredes
        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[1]
            wall.center_y = coordinate[0]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        # Crea un physics engine (interaccion entre mi jugador y la lista de paredes)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)





        # Set the background color
        # esto aun nose para que sirve
        arcade.set_background_color(arcade.color.AMAZON)


    # dibujamos
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        # dibujamos los sprites como lo deseamos
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()

        # Render the text
        # dibujamos el puntaje en la parte superior derecha
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)


    # define el movimiento del personaje
    def on_mouse_motion(self, x, y, dx, dy):
        pass
    '''
          """
        Called whenever the mouse moves.
        """
        # hazlo aparecer donde este mi jugador en el mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    
    '''




    # accion cuando se presiona el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """



        # Create a bullet
        # carga el disparo
        bullet = Bullet("laserBlue01.png", SPRITE_SCALING_LASER)



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

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    # Cuando se deja de presionar . Para que mi jugador no siga avanzando
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

   # la actualizacion en cada frame
    def update(self, delta_time):

        self.time += CHANGE_TIME

        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.player_list.update()
        self.coin_list.update()
        self.bullet_list.update()
        self.physics_engine.update() # tenemos que actualizar en cada momento como mi personaje interacciona con la lista de paredes



        # Loop through each bullet
        # conviene tener presente todo en una lista ya que podemos tener varias balaar
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            # si disparo(s) choca con moneda(s)
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            # si choco elimina la bala  de la lista
            if len(hit_list) > 0  :
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1 # agrega a la puntuacion

            # If the bullet flies off-screen, remove it.
            # si un disparo se escapo de la pantalla eliminalo
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()



        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left

        left_boundary = self.view_left + VIEWPORT_MARGIN # borde izquierdo + margen
        if self.player_sprite.left < left_boundary:
            # se resta cuanto avanzo a la izquierda : el lado derecho analizalo . Es una diferencia pequeña (ojo)
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN # borde derecho
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN # borde superior
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN # borde inferior
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.

        # Asegúrese de que nuestros límites sean valores enteros. Si bien el puerto de vista
        # admite números de punto flotante, para esta aplicación queremos que cada píxel en el puerto de vista se
        # asigne directamente a un píxel en la pantalla. No queremos ningún error de redondeo.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        # se llama de nuevo a .set_viewport solo si el personaje se encuentra en los bordes
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)


# inicio
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":

    main()

'''

def main () :

    jugador1 = my_jugador()

    mapa = my_map() # mi mapa debe ser creado con cuadriculas separadas 5pixels . 5pixeles sera mi escala

    arma = gun() # esta arma debe disparar diferentes funciones para tener mas preciso

    enemigo = enemy() # este se debe mover por el mapa de una manera aleatoria

    bala = bull() # mi bala debe describir diferentes acciones
    
    - configurar el tiempo para las mecanicas ya lo tengo por hecho en temporizador.py .  
    - Crear el mapa grande para jugador (eso si se me hace dificultoso por ahora ) Usa tiled . Tienes que ver en la pagina de arcade como hacerlo .
    - Crearle la gravedad al jugador .
    - Crear los Sprites que voy a usar para el juego . 
    - crear el efecto de bomba cuando la moneda es alcanzada por una bala .
    - Darle animacion a mi player . para que se vea mas realista . Pero para eso debo crear sprites . 
    - Crearle el multijugador (Este es el reto mas grande que tengo ) .  
    - Crea la pantallla del tutorial .

'''


