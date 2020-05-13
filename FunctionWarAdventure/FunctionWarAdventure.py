import arcade
import math
import random
from arcade.gui import *

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_BOX = 0.5
COIN_COUNT = 25


SIZE_WALL = 64 # ESTE ES EL TAMAÑO DE MI BLOQUE . 128*0.5 (OJO)

SCREEN_WIDTH = 20*SIZE_WALL # PARA QUE ENCAJE UN NUMEOR ENTERO DE PAREDES , IMPORTANTE
SCREEN_HEIGHT =  13*SIZE_WALL # PARA QUE ENCAJE UN NUMEOR ENTERO DE PAREDES , IMPORTANTE

BULLET_SPEED_X = 4
BULLET_SPEED_Y = 4

CHANGE_TIME = 0.024

MOVEMENT_SPEED = 5  # la velocidad de movimiento de mi personaje

# Vamos a crear dos nuevas constantes. No queremos que el jugador llegue al borde de la pantalla
# antes de comenzar a desplazarnos. Porque entonces el jugador no tendría idea de a dónde va
# . En nuestro ejemplo estableceremos un "margen" de 40 píxeles. Cuando el jugador esté a 40 píxeles del
# borde de la pantalla, moveremos el puerto de visualización para que pueda ver al menos 40 píxeles a su alrededor.
# osea para que vea 40 pixeles a su borde antes de que se mueva mas a ese borde .
VIEWPORT_MARGIN = 40  # El margen

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

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
        angulo_radians = math.atan(self.division)
        self.angle = math.degrees(angulo_radians)


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

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
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

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
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

        self.center_x += self.change_x
        self.center_y = math.sin((self.center_x - self.inicio_x) / 100) * 100 + self.inicio_y

        # Este angulo debo usar la dervada . Puedo con esto QUEDA PENDIENTE . USA atan2 (Ojo)
        self.division = (self.center_x - self.inicio_x) / (self.center_y - self.inicio_y)
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




    def update(self):
        pass



###################### ENEMIGO 1 ###########################

class Enemy1(arcade.Sprite):
    # enemigo principal , habra mas de esto pero por ahora solo sera un enemigo simple
    pass


###################### JEFE FINAL ###########################

class FinalBoss(arcade.Sprite):
    # La inteligencia de este enemigo sera dificil de programar pero con fe puedo programarlo
    pass

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
        arcade.draw_text("PRESIONA START PARA COMENZAR", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
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

        # Draw all the sprites.
        # dibujamos los sprites como lo deseamos
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.wall_list.draw()

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
            COMENZAR_JUEGO = Juego() # creamos un nuevo objeto
            # y nos vamos a la pantalla de INICIO DE JUEGO , LLEVANDOME LAS LISTAS A LOS JUGADORES , MONEDAS
            # BALAS . DEBO LIMPIARLAS DE ALGUN MODO PARA NO TENER PROBLEMAS LUEGO CON LA MEMORAIA .
            self.window.show_view(COMENZAR_JUEGO)  # nose como este metodo puede funcionar



        self.time += delta_time

        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.player_list.update()
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
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()




###################### PANTALLA DE JUEGO ###########################


class Juego(arcade.View):
    # El juego principal que es un escenario gigante
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    # dibuja el mensaje
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")


###################### PANTALLA DE BATALLA FINAL ###########################

class FinalBattle(arcade.View):
    # escenario final donde el jefe se encuentra y te quiere matar . Tiene mecanicas especificas
    pass












# ----------------------------------------------- COMANDO PARA INICIAR JUEGO ------------------------------------------------------



def main():
    # en que pantalla comienza
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "FunctionWarAdventure")
    window.total_score = 0 # cuantas monedas va a recolectar el jugador durante toda la partida para mostrarlas al final
    pantalla_inicio = Inicio()
    window.show_view(pantalla_inicio)
    arcade.run()


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


