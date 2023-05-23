from manim import *

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=13,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).shift(UP * 2)

        l1 = NumberLine(
            x_range=[-20, 20, 2],
            length=13,
            color=GREEN,
            include_numbers=True,
            font_size=24,
        )


        self.play(Create(l0))
        self.wait()

        arrow = Arrow(start=UP, end=DOWN, color=GOLD).next_to(l0, DOWN, buff=0.2)
        by2 = MathTex(r"\times 2").next_to(arrow, RIGHT, buff=0.1)
        self.play(FadeIn(arrow, by2))
        self.wait()

        self.play(Create(l1))
        self.wait()

        transformation = Matrix([[2]]).next_to(l1, DOWN, buff=1)
        determinant = MathTex("det([2]) = 2").next_to(transformation, DOWN, buff=0.5)

        self.play(Write(transformation))
        self.play(Write(determinant))

