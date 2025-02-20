



# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.WHITE)

# Get ready to draw
arcade.start_render()

# (The drawing code will go here.)
arcade.draw_text("Arbor Day - Plant a Tree!",
                 130, 300,
                 arcade.color.BLACK, 24)
arcade.draw_lrbt_rectangle_filled(10, 320 , 20, 60, arcade.color.ARCADE_GREEN)
# Finish drawing
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()