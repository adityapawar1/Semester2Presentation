from manim import *

class Derivatives(Scene):
    def construct(self):
        # Add a number line
        number_line = NumberLine()
        self.play(Write(number_line))

        # Represent a function with a dot
        dot = Dot().move_to(number_line.n2p(0))
        self.play(FadeIn(dot))

        # Display function f(x) = 2x
        func = Tex("f(x) = 2x").to_edge(UP)
        self.play(Write(func))

        # Define a linear map function
        def linear_map(x):
            return 2*x

        # Animate the dot moving along the number line under the function
        self.play(dot.animate.move_to(number_line.n2p(linear_map(2))), run_time=3)

        # Write the derivative of the function
        derivative = Tex("f'(x) = 2").to_edge(UP).shift(DOWN)
        self.play(Transform(func, derivative))

        # Animate the dot moving along the number line under the derivative
        self.play(dot.animate.move_to(number_line.n2p(linear_map(2))), run_time=3)

        # Display the Jacobian matrix
        jacobian = Tex(r"$J = \begin{bmatrix} 2 \end{bmatrix}$").to_edge(UP).shift(2*DOWN)
        self.play(Transform(func, jacobian))

        # Animate the dot moving along the number line under the Jacobian matrix
        self.play(dot.animate.move_to(number_line.n2p(linear_map(2))), run_time=3)

        self.wait()
