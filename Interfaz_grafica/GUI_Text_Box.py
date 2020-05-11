import arcade


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = ""
        self.center_x = self.width / 2 # fijate su propiedad width
        self.center_y = self.height / 2

    def setup(self):
        arcade.set_background_color(arcade.color.AMETHYST) # pinta el fondo

        # ese sel.text_list es una nueva propiedad para mi (no sale en la documentacion)
        # Revisa la documentacion . Solo es un elemento para que se dibujar texto que bien puede ser interactivo
        self.text_list.append(arcade.TextLabel("Name: ", self.center_x - 225, self.center_y))

        # Sprite de texto tambien agregado a la lista
        self.textbox_list.append(arcade.TextBox(self.center_x - 125, self.center_y))


        # Similar a text_list
        self.button_list.append(arcade.SubmitButton(self.textbox_list[0], self.on_submit,
                                                    self.center_x,
                                                    self.center_y))

    def on_draw(self):
        arcade.start_render()
        # se hereda todo lo que debe dibujar (esta es la primera vez que veo esto)

        super().on_draw()
        # si se presiona el botonn
        if self.text:
            arcade.draw_text(f"Hello {self.text}", 400, 100, arcade.color.BLACK, 24)

    def on_submit(self):
        self.text = self.textbox_list[0].text_storage.text


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()