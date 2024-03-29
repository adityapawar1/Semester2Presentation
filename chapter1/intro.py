from manim import RIGHT, UP, LinearTransformationScene
import numpy as np

class IntroScene(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        self.setup()
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

        self.apply_nonlinear_transformation(self.func)
        self.moving_mobjects = []

    def func(self, point):
        x, y, z = point
        return (x)*RIGHT + (y+np.sin(x))*UP
