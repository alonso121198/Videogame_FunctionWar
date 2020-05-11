"""
Load a map stored in csv format, as exported by the program 'Tiled.'

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/
"""
import arcade

SPRITE_SCALING = 0.5 # escala de jugador

# Escala de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
# el borde de las pantallas
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

TILE_SIZE = 128 # tamaño de mi imagen , recuerda ( mis imagenes son de 128x128 pixeles)
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING # el tamaño que va a ir de mi imagen : tamaño en pixeles * escala
MAP_HEIGHT = 7 # el cuantas filas de tamaño (SCALE_TILE_SIZE) tendra de alto mi mapa

# Physics
# velocidades de mi juego
MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5


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


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        # Call the parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Sprite lists
        self.player_list = None # lista de jugadores
        self.wall_list = None # lista de paredes

        # Set up the player
        self.player_sprite = None # jugador

        # Physics engine
        self.physics_engine = None # la fisica . Como interaccionaran nuestras listas

        # Used for scrolling map
        self.view_left = 0 # coordenada x de inicio de pantalla
        self.view_bottom = 0 # cooredenada y de inicio de pantalla

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList() # define la lista
        self.wall_list = arcade.SpriteList() # define las paredes

        # Set up the player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING) # carga el sprite

        # Starting position of the player
        # ubicacion de mi sprite
        self.player_sprite.center_x = 90
        self.player_sprite.center_y = 270
        # agregalo a la lista
        self.player_list.append(self.player_sprite)

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
                    wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING)
                elif item == 1:
                    wall = arcade.Sprite("grassLeft.png", SPRITE_SCALING)
                elif item == 2:
                    wall = arcade.Sprite("grassMid.png", SPRITE_SCALING)
                elif item == 3:
                    wall = arcade.Sprite("grassRight.png", SPRITE_SCALING)

                if item >= 0:
                    # Calculate where the sprite goes
                    # calcula donde el sprite va
                    wall.left = column_index * SCALED_TILE_SIZE # calacula donde estara la parte izquierda
                    wall.top = (MAP_HEIGHT - row_index) * SCALED_TILE_SIZE # calcula la parte superior . MAP_HEIGHT es 7 , fijalte por que es asi . NO es dificil

                    # Add the sprite
                    self.wall_list.append(wall) # agrega a a la lista

        # Create out platformer physics engine with gravity

        # la fisica entre mi Sprite y las paredes
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the background color
        # el fondo
        arcade.set_background_color(arcade.color.AMAZON)

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
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        # movimientos de mi jugador
        if key == arcade.key.UP:
            # This line below is new. It checks to make sure there is a platform underneath
            # the player. Because you can't jump if there isn't ground beneath your feet.
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # fijate que no altera como en eje y por que eso ya lo hace el salto
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        # actualiza la fisica del asunto . Que tan relacionados estan
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the view port

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
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


def main():
    window = MyWindow()
    window.setup()

    arcade.run()


main()