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
        tex1 = Tex("A vector F is conservative if....",font_size=50)
        self.play(Write(tex1))
        self.wait(1)
        tex2 = Tex(r"$\exists$ a function f such that $\nabla f=\vec{F}$",font_size=50)
        self.play(FadeTransform(tex1,tex2), stretch=True)
        self.wait(2)
        self.play(FadeOut(tex2))
        tex3 = Tex(r"Now how do we find if a vector F has a corresponding function f for which $\nabla f=\vec{F}$?",font_size=25)
        self.play(Write(tex3))
        self.wait(3)
        tex4 = Tex(r"Let's first take the case where $\vec{F}$ is a 2 dimensional vector",font_size=50)
        self.play(FadeTransform(tex3,tex4), stretch=True)
        self.wait(2)
        self.play(FadeOut(tex4))
        tex5 = Tex(r"If $\vec{F}$ is 2 dimensional then $\vec{F}=\text{N} \hat{i}+\text{M} \hat{j}$",font_size=50).shift(2*UP)
        tex6 = Tex(r"Say $\exists$ f such that $\nabla f=\vec{F}$",font_size=50).shift(UP)
        tex7 = Tex(r"Then $\frac{\partial f}{\partial x} = N$ and $\frac{\partial f}{\partial y} = M$",font_size=50)
        tex8 = Tex(r"Since $\frac{\partial f}{\partial x \partial y}=\frac{\partial f}{\partial y \partial x}$",font_size=50).shift(DOWN)
        tex9 = Tex(r"Then that must mean $\frac{\partial N}{\partial y} = \frac{\partial M}{\partial x}$",font_size=50).shift(2*DOWN)
        self.play(Write(tex5))
        self.wait(1)
        self.play(FadeIn(tex6))
        self.wait(1)
        self.play(Write(tex7))
        self.wait(1)
        self.play(FadeIn(tex8))
        self.wait(1)
        self.play(FadeIn(tex9))
        tgroup1 = [tex5,tex6,tex7,tex8,tex9]
        vgroup1 = VGroup(*tgroup1)
        self.play(FadeOut(vgroup1))
        tex10 = Tex(r"So we can say that $\vec{F}=N \hat{i}+ M \hat{j}$ is conservative if:", font_size=50).shift(UP)
        tex11 = Tex(r"$\frac{\partial N}{\partial y} = \frac{\partial M}{\partial x}$", font_size=50)
        self.play(Write(tex10))
        self.wait(1)
        self.play(Write(tex11))
        self.wait(1)
        self.play(FadeOut(tex10))
        self.play(FadeOut(tex11))
        tex12 = Tex(r"How about the case where the vector F is 3 dimensional? How do we figure out if its conservative?", font_size=25)
        self.play(Write(tex12))
        self.play(tex12.animate.shift(2*UP))
        self.wait(0.5)
        tex13 = Tex(r"To solve this conundrum, we introduce a new operator called curl", font_size=25)
        self.play(Write(tex13))
        self.play(tex13.animate.shift(UP))
        self.wait(1)
        self.play(Uncreate(tex12))
        self.play(Uncreate(tex13))
        tex14 = Tex(r"The curl of $\vec{F}(x,y,z) = F_{x} \hat{i}+ F_{y} \hat{j} + F_{z} \hat{k}$ is:")
        tex15 = Tex(r"$ \text{curl}\vec{F} = \begin{bmatrix} \hat{i} & \hat{j} & \hat{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z}\\ F_{x} & F_{y} & F_{z} \end{bmatrix}$")
        self.play(Create(tex14))
        self.play(tex14.animate.shift(2*UP))
        self.play(Write(tex15))
        self.wait(1)
        self.play(Uncreate(tex14))
        self.play(tex15.animate.shift(2*UP))
        tex16 = Tex(r"So $\text{curl} \vec{F} = (\frac{\partial F_{z}}{\partial y} - \frac{\partial F_{y}}{\partial z}) \hat{i} - (\frac{\partial F_{z}}{\partial x} - \frac{\partial F_{z}}{\partial x}) \hat{j} + (\frac{\partial F_{y}}{\partial x} - \frac{\partial F_{x}}{\partial y}) \hat{k}$")
        self.play(Write(tex16))
        tex17 = Tex(r"We say that $\vec{F}$ is conservative if the curl of F is $\vec{0}$").shift(DOWN)
        self.play(Write(tex17))


        
        
        

