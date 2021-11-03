import arcade

# argument/s for classes are it's parent/s (inheritance)
# arguments added when creating an object are for the object

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "SPACE MERCENARY"
MOVEMENT_SPEED = 5


class Player(arcade.Sprite):
    """The Player class"""
    
    def update(self):
        """Move the player"""
        self.center_x += self.change_x
        self.center_y += self.change_y

        # check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class game(arcade.Window):
    """The Game class"""
    def __init__(self, width, height, title):
        """Constructor"""

        # call parent class constructor
        super().__init__(width, height, title)

        # list containing players
        self.player_list = None

        # set background colour
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        """Setup game, initialise variables"""

        # player list
        self.player_list = arcade.SpriteList()

        # setup player
        self.player_sprite = Player(r"C:\Users\pdaly\Documents\Projects\SpaceMercenary\rocket.PNG", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
    
    def on_draw(self):
        """Render screen"""

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    """The Main function"""
    #initialise the game and run it
    newGame = game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    newGame.setup()
    arcade.run()

if __name__ == "__main__":
    main()