"""
Show how to do enemies in a platformer

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_enemies_in_platformer
"""

import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING) # # el tamaño de la pared o suelo

SCREEN_WIDTH = 800 # amcho de pantalla
SCREEN_HEIGHT = 600 # largo de pantalla
SCREEN_TITLE = "Sprite Enemies in a Platformer Example" # titulo del juego

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40 # el margen (tengo que ver donde lo usa)
RIGHT_MARGIN = 150

# Physics
MOVEMENT_SPEED = 5 # velocidad de movimiento de izquierda y derecha
JUMP_SPEED = 14 # velocidad de salto , esto aun no lo entiendo
GRAVITY = 0.5 # la gravedad en que unidades esta ?


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.


        # esto sirve para que se pueda ejecutar programas con python -m arcade.(ruta) de manera facil
        # puedes dejar esto fuera de tu codigo , no altera en nada excepto que no puedes hacer lo que te indique
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.wall_list = None # lista de paredes
        self.enemy_list = None # lista de los enemigos
        self.player_list = None # lista de los jugadores

        # Set up the player
        self.player_sprite = None # sprite del jugador
        self.physics_engine = None # sprite de la fisica
        self.view_left = 0 # coordenada x del incio de pantalla
        self.view_bottom = 0  # coordenada y del inicio de la pantalla
        self.game_over = False # estatus de mi juego

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        # inicialmos las listas de stprites
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Draw the walls on the bottom

        # dibujamos el suelo
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # Draw the platform
        # dibujamos la plataforma que flota de las paredes
        for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # Draw the crates
        # dibujamos las paredes o obstaculos (las cajas )
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 5):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE
            wall.left = x
            self.wall_list.append(wall)

        # -- Draw an enemy on the ground
        # establece el enmigo
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        # la ubicacion de ese enemigo debe justo encima del suelo
        enemy.bottom = SPRITE_SIZE
        enemy.left = SPRITE_SIZE * 2

        # Set enemy initial speed
        # velocidad del enemigo
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Draw a enemy on the platform
        # dibuja el enemigo en la plataforma
        enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

        # ubica el segundo enemigo justo encima de la plataforma
        enemy.bottom = SPRITE_SIZE * 4
        enemy.left = SPRITE_SIZE * 4

        # Set boundaries on the left/right the enemy can't cross
        # Establece los limites por donde el enmigo caminara , despues de eso no podra pasar
        enemy.boundary_right = SPRITE_SIZE * 8
        enemy.boundary_left = SPRITE_SIZE * 3
        # velociad del enemigo en el eje x
        enemy.change_x = 2
        self.enemy_list.append(enemy)

        # -- Set up the player
        # establece el player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        # Starting position of the player
        # comienzo del jugador
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270

        # engine physics usado para saltar cuando halla una plataforma debajo del sprite . con la gravedad
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the background color
        # El fondo
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        # dibuja los players , paredes , cajas , platafomaas y enemigos
        self.player_list.draw()
        self.wall_list.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            # regresa True si hay una plataforma debajo del personaje
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED # sale con una velocidad hacia arriba
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        # fijate que no se pone para y .
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # les similar con update pero para mas consistencia usa on_update always

        # Update the player based on the physics engine
        # si el el player no choco con algun enemigo , sigue el juego
        # si esto es falso no se actualiza nada y el juego se detiene visualmente pero sigue corriendo el juego .
        if not self.game_over:
            # Move the enemies
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                # If the enemy hit a wall, reverse
                # si un enemigo golpio una pared hazlo cambiar de direccion
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                # If the enemy hit the left boundary, reverse
                # si el enmigo esta en los limites y el limite izquierdo no es nulo hazlo retroceder
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

            # Update the player using the physics engine
            # actualiza su salto de caida
            self.physics_engine.update()

            # See if the player hit a worm. If so, game over.
            # si el player choco con un enemigo el juego termina
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()