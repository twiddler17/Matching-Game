import arcade

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

class Square:
    def __init__(self, side):
        self.width = SCREEN_WIDTH / side - 10
        self.height = SCREEN_HEIGHT / side - 10
        self.x = (self.width + 10) / -2 
        self.y = SCREEN_HEIGHT + (self.height + 10) / 2

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Memory Tile Game")
        self.shape_list = None

    def setup(self, side):
        self.shape_list = []

        for row in range(0, side):
            x = (self.width + 10) / -2 
            y -= self.height + 10
            for column in range(0, side):
                x += width + 10
                arcade.draw_rectangle_filled(x, y, width, height, arcade.color.BLUE)

