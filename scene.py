from pyparsing import White
from manim import *
import numpy as np
class ShowVectorF(Scene):#Shows the vector field on graph
    def construct(self, n):
        # eq = MathTex(r"\vec{F}=<y,x>", font_size=50)
        # eq.shift(3*UP)
        # self.add(eq)
        func = lambda pos: pos[0]*UP+pos[1]*RIGHT
        vector_field = ArrowVectorField(
            func, x_range=[-4, 4, 1], y_range=[-4, 4, 1], length_func=lambda x: x/4, colors=[YELLOW],stroke_width=1
        )
        vector_field.scale(0.75)
        self.add(vector_field)
        nplane=NumberPlane(x_range=[-4, 4, 1], y_range=[-4, 4, 1])
        nplane.scale(0.75)
        self.add(nplane)
        self.wait(n)
        self.remove(*nplane)
        self.remove(*vector_field)
        # self.remove(*eq)
class VectorF(Scene):#Shows vector field equation
    def construct(self,n):
        eq = MathTex(r"\vec{F}=<y,x>", font_size=96)
        eq.shift(RIGHT)
        self.add(eq)
        self.wait(n)
        self.remove(*eq)
class Multi(Scene):
    def construct(self):
        VectorF.construct(self,2)
        ShowVectorF.construct(self,1)
        tex = Tex("A vector F is conservative if....",font_size=50)
        self.play(FadeIn(tex))
        self.wait(1)
        ntex = Tex(r"$\exists$ a function f such that $\nabla f=\vec{F}$",font_size=50)
        self.play(FadeTransform(tex,ntex), stretch=True)
        self.wait(1)
        self.remove(*tex)
        self.remove(*ntex)
