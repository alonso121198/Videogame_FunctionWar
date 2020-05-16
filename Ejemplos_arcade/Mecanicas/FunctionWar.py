import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED_X = 5
BULLET_SPEED_Y = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        # con esto creo la pantalla
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists

        self.player_list = None  # mi jugador
        self.coin_list = None  # las monedas del juego
        self.bullet_list = None  # las monedas

        # Set up the player info
        self.player_sprite = None # el sprite
        self.score = 0 # contador de puntos

        # Don't show the mouse cursor
        # para que no se vea el mouse
        self.set_mouse_visible(False)

        # el color del fondo
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """
        # inicializamos el juego

        # Sprite lists
        self.player_list = arcade.SpriteList() # sera lista de personajes
        self.coin_list = arcade.SpriteList() # sera lista de monedas
        self.bullet_list = arcade.SpriteList() # lista de disparos

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        # cargamos el sprite del jugador
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        # establecemos el inicio de posicion de nuestro jugador
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        # lo agregamos a la lista de nuestros jugadores
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            # cargamos las monedas
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            # lo agregamos a la lista
            self.coin_list.append(coin)

        # Set the background color
        # esto aun nose para que sirve
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

        # Render the text
        # dibujamos el puntaje en la parte superior derecha
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    # define el movimiento del personaje
    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        # hazlo aparecer donde este mi jugador en el mouse
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    # accion cuando se presiona el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        # carga el disparo
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        # The image points to the right, and we want it to point up. So


        # rotate it.
        # rotas la imagen
        # como parte rotado la imagen
        bullet.angle = 45

        # Position the bullet
        # comienza de la ubicacion del jugador
        bullet.center_x = self.player_sprite.center_x


        # pero desde la base de la cabeza de mi sprite jugador sale
        bullet.bottom = self.player_sprite.top
        # la velocidad con que cambia mi disparo automaticamente
        bullet.change_y = BULLET_SPEED_Y
        bullet.change_x = BULLET_SPEED_X

        # Add the bullet to the appropriate lists
        # añade un disparo a la lista
        self.bullet_list.append(bullet)

    # la actualizacion en cada frame
    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        # actualiza tanto las monedas como las balas
        self.coin_list.update()
        self.bullet_list.update()



        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            # si disparo(s) choca con moneda(s)
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            # si choco eliminalo de la lista
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1 # agrega a la puntuacion

            # If the bullet flies off-screen, remove it.
            # si un disparo se escapo de la pantalla eliminalo
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


# inicio
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
