import arcade

arcade.open_window(1200, 700, "lost of shapes")
arcade.set_background_color(arcade.color.RED)

arcade.start_render()

#arcade.draw_line_strip([(50, 50), (50, 300), (300, 50), (300, 300)], arcade.color.GOLD, 3)

#arcade.draw_lrtb_rectangle_filled(320, 420, 300, 50, arcade.color.GOLD)
#arcade.draw_lrtb_rectangle_outline(450, 550, 300, 50, arcade.color.GOLD, 12)
#arcade.draw_xywh_rectangle_filled(380, 120, 300, 80, arcade.color.AO)
#arcade.draw_xywh_rectangle_outline(10, 10, 680, 300, arcade.color.CARDINAL, 8)

#arcade.draw_circle_filled(450, 300, 75, arcade.color.DARK_TAUPE)
#arcade.draw_circle_outline(450, 300, 150, arcade.color.FLUORESCENT_YELLOW, 15)

#arcade.draw_triangle_filled(300, 600, 600, 600, 450, 350, arcade.color.BLUE_SAPPHIRE)
#arcade.draw_triangle_outline(600, 600, 490, 300, 700, 700, arcade.color.CADET_GREY, 15)

#arcade.draw_arc_filled(800, 500, 100, 100, arcade.color.DEEP_PUCE, 30, 350)
#arcade.draw_arc_outline(980, 500, 200, 100, arcade.color.EUCALYPTUS, -180, 0, 10)
#arcade.draw_arc_outline(980, 500, 200, 100, arcade.color.EUCALYPTUS, 0, 180, 10)



arcade.finish_render()

arcade.run()
