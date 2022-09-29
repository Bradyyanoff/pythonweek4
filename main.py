import arcade

my_window = arcade.open_window(1000, 680, "Graph Paper")
arcade.set_background_color(arcade.color.GRAY)

arcade.start_render()

for xloc in range(50, 1000, 80):
    arcade.draw_line(xloc, 50, xloc, 800, arcade.color.BLACK, 1)
for yloc in range(50, 680, 80):
    arcade.draw_line(50, yloc, 1000, yloc, arcade.color.BLACK, 1)

arcade.finish_render()

arcade.run()
