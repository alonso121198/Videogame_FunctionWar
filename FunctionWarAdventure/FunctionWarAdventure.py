import arcade
import math
import random
from arcade.gui import *

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_BOX = 0.5
COIN_COUNT = 25

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

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



# ----------------------------------------------- OBJETOS-------------------------------------------------------



###################### JUGADOR ###########################

class Player(arcade.Sprite):

    # funcion lineal
    def shoot_lineal(self,escala,argu):
        pass



    # disparo sinoidal o cosenoidal
    def shoot_sinoidal(self,escala,argu):
        pass

    # disparo_logaritmico
    def shoot_log(self,escala,argu):
        pass


    # diparo_logaritmico
    def shoot_exp(self,escala,argu):
        pass


    # disparo_algebraico
    def shoot_alge(self,escala,argu):
        pass

    # disparo superpoderoso
    def shoot_tan(self,escala,argu):
        pass


    # barrera_campana
    def shoot_campana(self,escala,argu):
        pass




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


###################### BALA ###########################

class Bullet(arcade.Sprite):

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


###################### MONEDAS ###########################

class Coin(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        self.change_x = random.uniform(-1, 1)
        self.change_y = random.uniform(-1, 1)

        if self.change_x == 0 or self.change_y == 0:
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
            print("liberado")
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
    # aca el jugador jugara disparando monedas , se indicara las instrucciones y cuando este listo ira a jugar en el escenario principal
    def on_show(self):

        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()


###################### PANTALLA DE JUEGO ###########################


class Juego(arcade.View):
    # El juego principal que es un escenario gigante
    pass


###################### PANTALLA DE BATALLA FINAL ###########################

class FinalBattle(arcade.View):
    # escenario final donde el jefe se encuentra y te quiere matar . Tiene mecanicas especificas
    pass









class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Function War")

        self.player_list = None
        self.coin_list = None  # por el momento como nose crear sprites debo poner las monedas como enemigos
        self.bullet_list = None  # mis balas
        self.wall_list = None  # mi lista para las paredes

        self.player_sprite = None  # el sprite
        self.score = None  # la puntuacion es lo mas importante

        self.set_mouse_visible(False)  # el mouse no debe verse

        self.time = 0  # este va  a ser mi contador para el tiempo de trabajo

        # This variable holds our simple "physics engine"
        # esta variaable se usara para poder simular una interaccion entre sprites
        self.physics_engine = None

        # Manage the view port
        # Este es para manejar la esquina inferior izquierda de nuestra vista de pantalla .
        self.view_left = 0  # coordenada x
        self.view_bottom = 0  # coordenada y

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
        # Mis bloques son cuadrados de lado 64 pixeles . Aun nose por que pero creo que 0.5 de la medida de "SCALING BOX "
        coordinate_list = [[470, 500],
                           [400, 570],
                           [470, 570],
                           [100, 70],
                           [100, 140],
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

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left

        left_boundary = self.view_left + VIEWPORT_MARGIN  # borde izquierdo + margen
        if self.player_sprite.left < left_boundary:
            # se resta cuanto avanzo a la izquierda : el lado derecho analizalo . Es una diferencia pequeña (ojo)
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN  # borde derecho
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN  # borde superior
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN  # borde inferior
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


