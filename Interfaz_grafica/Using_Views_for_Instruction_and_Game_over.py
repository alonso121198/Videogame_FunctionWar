"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each view will need to have its own draw,
update and window event methods. To switch a view, simply create a view
with `view = MyView()` and then use the view.show() method.

This example shows how you can set data from one View on another View to pass data
around (see: time_taken), or you can store data on the Window object to share data between
all Views (see: total_score).

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_instructions_and_game_over.py
"""

import arcade
import random
import os

# estos comandos solo son para que alguien externo pueda ejecutarlo de manera facil desde la terminal
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# tamaño de la pantalla y escala de la imagen
WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class MenuView(arcade.View):

    # llamamlo cuando quieras cambiar el fondo de pantalla . llamalo para la vista
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    # comienza el dibujado de las palabras iniciales
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    # cuando se es presionado el boton
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # define el objeto insturcciones
        instructions_view = InstructionView()
        # fijate que self.windows es una variable de instancia (que es un objeto a su vez , una componente) y el .show_view() es su metodo
        # lo que hace es mostrar la vista actual
        self.window.show_view(instructions_view)

# munu de instrucciones
class InstructionView(arcade.View):


    # establece el color del juego
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    # dibuja el mensaje
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    # que pasa si se presiona
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # se llama a la funcion GameWiew
        game_view = GameView()
        # fijate que self.windows es una variable de instancia (que es un objeto a su vez , una componente) y el .show_view() es su metodo
        # lo que hace es mostrar la vista actual
        self.window.show_view(game_view)

    # Se inicializa el juego , Fijate que no se uso arcade.Windows lo cual es extraño , habra que aprender mas acerca de esto
class GameView(arcade.View):


    def __init__(self):
        super().__init__()
        # tiempo tomado para el juego
        self.time_taken = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # monedas
        for i in range(5):

            # Create the coin instance
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING / 3)

            # Position the coin
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    # color de
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

        # Don't show the mouse cursor
        # no se vea el cursor . Fijate como usa window aca
        self.window.set_mouse_visible(False)


    # dibujo
    def on_draw(self):
        arcade.start_render()
        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 30, arcade.color.WHITE, 14)
        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        # actualizas el tiempo cada vez que avanza la actualizacion
        self.time_taken += delta_time

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.player_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        for coin in hit_list:
            coin.kill()
            self.score += 1
            self.window.total_score += 1

        # If we've collected all the games, then move to a "GAME_OVER"
        # state.
        # si recupero todas las monedas entonces
        if len(self.coin_list) == 0:

            # llamas la funcion GameOverView()
            game_over_view = GameOverView()
            #  el tiempo final que transcurrio
            game_over_view.time_taken = self.time_taken
            # Para que se vea de nuevo el cursor
            self.window.set_mouse_visible(True)
            # LLama a la siguiente pantalla de game_over
            self.window.show_view(game_over_view)

    def on_mouse_motion(self, x, y, _dx, _dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        # el color de juego perdido
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        # dibuja cuanto tiempo duro el juego
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         WIDTH/2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        # para que el juego vuelva a verse de nuevo .
        self.window.show_view(game_view)


def main():
    # fijate que arcade.Window es la cabeza de todo es como alli se plazma todo lo que hacen otras clases hijos de arcade.View
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()