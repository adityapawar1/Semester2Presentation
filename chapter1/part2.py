from manim import DOWN, GREEN, ORANGE, UL, Arrow, LinearTransformationScene, Matrix, ReplacementTransform, SurroundingRectangle, Vector, Write

class RepresentingLinearTransformations(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        self.add_title("Representing Linear Transformations", 1, True)
        self.wait(2)

        vector = self.add_vector([1, 1])

        self.moving_mobjects = []
        self.apply_matrix([[3, -2], [1, 1]])
        self.wait(2)

        m0 = Matrix([[3, -2], [1, 1]]).to_corner(UL, buff=0.5).shift(DOWN)
        m0.add(SurroundingRectangle(m0.get_columns()[0]).set_color(GREEN))
        m0.add(SurroundingRectangle(m0.get_columns()[1]).set_color(ORANGE))
        self.play(Write(m0))
        self.wait(5)

        self.moving_mobjects = []
        self.apply_matrix([[1, 0.5], [0.5, 1]])

        m1 = Matrix([[3.5, -1.5], [2.5, 0]]).to_corner(UL, buff=0.5).shift(DOWN)
        m1.add(SurroundingRectangle(m1.get_columns()[0]).set_color(GREEN))
        m1.add(SurroundingRectangle(m1.get_columns()[1]).set_color(ORANGE))
        self.play(ReplacementTransform(m0, m1))
        self.wait(2)


