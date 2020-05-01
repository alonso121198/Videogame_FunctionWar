import arcade

SPRITE_SCALING_PLAYER = 0.5 # esta es la escala de mi personaje
SPRITE_SCALING_COIN = 0.2 # de mi pelota en forma de moneda


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480



class Ball(arcade.Sprite):
    """ This class manages a ball bouncing on the screen. """

    def update(self):

        """ Code to control the ball's movement. """
        self.center_x += self.change_x
        self.center_y += self.change_y




'''
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

'''



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create a list for the balls
        self.ball_list = arcade.SpriteList() # sera lista de personajes

        # Add three balls to the list
        ball = Ball("coin_01.png", SPRITE_SCALING_COIN)
        ball.center_x = 50
        ball.center_y = 50
        ball.change_x = 2
        ball.change_y = 3
        self.ball_list.append(ball)




    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        # Use a "for" loop to pull each ball from the list, then call the draw
        # method on that ball.
        for ball in self.ball_list:
            ball.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""

        # Use a "for" loop to pull each ball from the list, then call the update
        # method on that ball.
        for ball in self.ball_list:
            ball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()