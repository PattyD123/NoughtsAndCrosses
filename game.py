from typing_extensions import Unpack
import arcade

# Reference code

# argument/s for classes are it's parent/s (inheritance)
# arguments added when creating an object are for the object

# Sprite sizing
SPRITE_SCALING = 0.5

# Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "SPACE MERCENARY"

# Movement
MOVEMENT_SPEED = 5

# Shooting
LASER_SCALING = 0.8
SHOOT_SPEED = 15
LASER_SPEED = 12
# BULLET_DAMAGE = 1

# Layer name bullets
LAYER_NAME_LASERS = "Lasers"

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

        # background variable
        self.background = None

        # list containing players
        self.player_list = None

        # set background colour
        arcade.set_background_color(arcade.color.BLACK)

        # Shooting initialisation
        self.can_shoot = False
        self.shoot_timer = 0
        self.shoot_pressed = False
    
    def setup(self):
        """Setup game, initialise variables"""

        # sprite lists
        self.player_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()

        # setup shooting
        self.can_shoot = True
        self.shoot_timer = 0

        # setup player
        self.player_sprite = Player(r"C:\Users\pdaly\Documents\Projects\SpaceMercenary\images\rocket.PNG", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # set background
        self.background = arcade.load_texture(r"C:\Users\pdaly\Documents\Projects\SpaceMercenary\images\spaceBG.jpg")

    def on_draw(self):
        """Render screen"""

        # This command has to happen before we start drawing
        arcade.start_render()
        
        # Draw the background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw all the sprites
        self.player_list.draw()
        self.laser_list.draw()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player
        self.player_list.update()

        # check if player has shot
        if self.can_shoot:
            if self.shoot_pressed:
                arcade.play_sound(self.shoot_sound)
                laser = arcade.Sprite(r"C:\Users\pdaly\Documents\Projects\SpaceMercenary\images\laserFinal.PNG", LASER_SCALING)
                # bullet can only go up
                laser.change_y = LASER_SPEED
                laser.center_x = self.player_sprite.center_x
                laser.center_y = self.player_sprite.center_y
                self.laser_list.append(laser)
        
        # loop through lasers
        for laser in self.laser_list:
            # check if laser hit something

            # check if laser exited map
            if laser.bottom > self.width or laser.top < 0:
                laser.remove_from_sprite_lists()
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
        
        if key == arcade.key.SPACE:
            self.shoot_pressed = True

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

        if key == arcade.key.SPACE:
            self.shoot_pressed = False
def main():
    """The Main function"""
    #initialise the game and run it
    newGame = game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    newGame.setup()
    arcade.run()

if __name__ == "__main__":
    main()