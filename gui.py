import arcade

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

class Square:
    def __init__(self, side):
        self.x = (width + 10) / -2 
        self.y = SCREEN_HEIGHT + (height + 10) / 2
        self.width = SCREEN_WIDTH / g - 10
        self.height = SCREEN_HEIGHT / g - 10

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Memory Tile Game")
        self.shape_list = None

    def setup(self, side):
        self.shape_list = []

        for row in range(0, side):
            x = (width + 10) / -2 
            y -= height + 10
            for column in range(0, side):
                x += width + 10
                arcade.draw_rectangle_filled(x, y, width, height, arcade.color.BLUE)

