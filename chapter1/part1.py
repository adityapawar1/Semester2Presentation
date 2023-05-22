from manim import DOWN, RIGHT, UL, LinearTransformationScene, MathTex, Write, Text

class LinearTransformationRequirements(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
        )

    def construct(self):
        self.add_title("Requirements for Linear Transformations", 1, True)
        self.wait(2)
        self.moving_mobjects = []

        label1 = Text("1.").to_corner(UL, buff=0.5).shift(DOWN)
        label2 = Text("2.").next_to(label1, DOWN, buff=0.3)
        label3 = Text("3.").next_to(label2, DOWN, buff=0.3)

        self.play(Write(label1), Write(label2), Write(label3))

        req1 = Text("Parallel lines stay parallel").next_to(label1, RIGHT, buff=0.2)
        req2 = Text("Spacing between lines stays even").next_to(label2, RIGHT, buff=0.2)
        req3 = Text("Origin does not move").next_to(label3, RIGHT, buff=0.2)

        self.wait(2)
        self.play(Write(req1))
        self.moving_mobjects = []
        self.apply_matrix([[1, 1], [0, 1]])
        self.wait(2)

        self.play(Write(req2))
        self.moving_mobjects = []
        self.apply_matrix([[0, 2], [-1, 2]])
        self.wait(2)

        self.play(Write(req3))
        self.moving_mobjects = []
        self.apply_matrix([[-1, 2], [0, -1]])
        self.wait(2)

        self.add_transformable_mobject(label1, label2, label3)
        self.add_transformable_mobject(req1, req2, req3)
        self.moving_mobjects = []
        self.apply_matrix([[1, 1], [0, 1]])
        self.wait(2)

