import arcade

arcade.open_window(1200, 700, "lost of shapes")
arcade.set_background_color(arcade.color.RED)

arcade.start_render()

#arcade.draw_line_strip([(50, 50), (50, 300), (300, 50), (300, 300)], arcade.color.GOLD, 3)
arcade.draw_lrtb_rectangle_filled(320, 420, 300, 50, arcade.color.GOLD)
arcade.draw_lrtb_rectangle_outline(450, 550, 300, 50, arcade.color.GOLD, 12)
arcade.draw_xywh_rectangle_filled(380, 120, 300, 80, arcade.color.AO)
arcade.draw_xywh_rectangle_outline(10, 10, 680, 300, arcade.color.CARDINAL, 8)



arcade.finish_render()

arcade.run()
