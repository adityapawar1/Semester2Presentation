from manim import LinearTransformationScene

class IntroScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        self.add_title("Linear Transformations")
        self.wait(2)
        self.moving_mobjects = []

        self.apply_matrix([[1, 1], [0, 1]])
        self.wait(2)
        self.moving_mobjects = []

        self.apply_matrix([[0, -1], [1, 0]])
        self.wait(2)
        self.moving_mobjects = []

        self.apply_matrix( [[-2, 1], [2, 1]] )
        self.wait(2)
        self.moving_mobjects = []

        self.apply_matrix([[5, 2], [3, 2]])
        self.wait(2)
        self.moving_mobjects = []

        self.apply_matrix( [[1, 0], [0, 0]])
        self.wait(2)
        self.moving_mobjects = []
