from manim import *

class DerivativeAnimation(LinearTransformationScene):
    def construct(self):
        # Define the function to be differentiated
        t_range = [-TAU, TAU]
        func = ParametricFunction(lambda t: np.array([t, np.sin(t), 0]), t_range=t_range, color=RED)
        self.play(Create(func))

        # Define the linear map and its Jacobian matrix
        linear_map = [[2, 1], [1, 2]]
        jacobian = Matrix(linear_map)

        # Apply the linear map to the function and show the Jacobian matrix
        self.apply_transposed_matrix(linear_map)
        self.wait()
        self.play(Write(jacobian))