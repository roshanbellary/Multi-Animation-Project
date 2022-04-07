from manim import *
import numpy as np
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class Multi(Scene):
    def construct(self):
        func = lambda pos: pos[0]*UP+pos[1]*RIGHT
        vector_field = ArrowVectorField(
            func, x_range=[-4, 4, 1], y_range=[-4, 4, 1], length_func=lambda x: x/4, colors=[YELLOW],stroke_width=1
        )
        self.add(vector_field)
        nplane=NumberPlane()
        self.add(nplane)
        dot = Dot().shift(LEFT)
        vector_field.nudge(dot,-2,60, True)
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(dot)
        self.wait(6)
        # rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)
        # self.add(VGroup(rtarrow1).arrange(DOWN))

