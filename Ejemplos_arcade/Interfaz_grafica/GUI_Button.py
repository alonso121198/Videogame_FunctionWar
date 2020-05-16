from arcade.gui import *

import os

# esto es el boton de TextButton
class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Play", theme=None):
        # fijate lo que hereda .
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):

        if self.pressed:
            self.game.pause = False
            self.pressed = False


class PauseButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Pause", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.game.pause = True
            self.pressed = False


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "GUI Text Buton Example")

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.AMAZON)
        self.pause = False
        self.text = "Graphical User Interface"
        self.text_x = 0
        self.text_y = 300
        self.text_font_size = 40
        self.speed = 1
        self.theme = None

    def set_button_textures(self):
        normal = ":resources:gui_themes/Fantasy/Buttons/Normal.png"
        hover = ":resources:gui_themes/Fantasy/Buttons/Hover.png"
        clicked = ":resources:gui_themes/Fantasy/Buttons/Clicked.png"
        locked = ":resources:gui_themes/Fantasy/Buttons/Locked.png"
        # fijate , self theme es un objeto , pero que tipo de objeto ?
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        # donde se definio la funcion theme ?
        # # esto viene de from arcade.gui import * (OJO)
        self.theme = Theme() # y para ser exacto en la documentacion viene de arcade.Theme
        self.theme.set_font(24, arcade.color.WHITE) # establecer la fuente de los textos
        self.set_button_textures() # metodo anterior

    def set_buttons(self):

        self.button_list.append(PlayButton(self, 60, 570, 110, 50, theme=self.theme))
        self.button_list.append(PauseButton(self, 60, 515, 110, 50, theme=self.theme))

    def setup(self):
        # para estableces los temas y los botones de los metodos antes definidos
        print("hola usuario")
        self.setup_theme()
        self.set_buttons()

    def on_draw(self):
        arcade.start_render()
        # dibuja todo lo heredado
        super().on_draw() # con esto traes todas las opciones de botones , osea el dibujado
        # dibuja self.text con los detalles
        arcade.draw_text(self.text, self.text_x, self.text_y, arcade.color.ALICE_BLUE, self.text_font_size)

    def update(self, delta_time):
        # retorna nulo
        if self.pause:
            return
        # para que rebote el texto
        if self.text_x < 0 or self.text_x > self.width:
            self.speed = -self.speed
        self.text_x += self.speed


def main():
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()