import arcade

arcade.open_window(1200, 700, "lost of shapes")
arcade.set_background_color(arcade.color.RED)

arcade.start_render()

#arcade.draw_line_strip([(50, 50), (50, 300), (300, 50), (300, 300)], arcade.color.GOLD, 3)

arcade.finish_render()

arcade.run()
