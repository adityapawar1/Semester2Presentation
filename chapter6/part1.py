from manim import *

class TheJacobian(Scene):
    def construct(self):
        poly1_points = [
            [-2, -2, 0],
            [-4, -1, 0],
            [-3, 3, 0],
            [0, 4, 0],
            [2, 1, 0],
            [0, 0, 0],
        ]
        poly2_points = [
            [-2, -1, 0],
            [-3, 0, 0],
            [-4, 2, 0],
            [0, 4, 0],
            [3, 2, 0],
            [-0.5, 0, 0],
        ]
        polygon1 = Polygon(*poly1_points, color=PURPLE_B, fill_opacity= 1.0).shift(LEFT * 3).scale(0.6).shift(DOWN * 0.2)
        func1_label = MathTex(r"\text{Height: } f(x, y)").next_to(polygon1, UP, buff=0.2)
        polygon1_label = Text("Surface A").next_to(polygon1, DOWN, buff=0.2)
        polygon1.set_fill(PURPLE_B)

        polygon2 = Polygon(*poly2_points, color=BLUE_B, fill_opacity= 1.0).next_to(polygon1, RIGHT, buff=2).scale(0.7)
        func2_label = MathTex(r"\text{Height: } f(g(x, y))").next_to(polygon2, UP, buff=0.2)
        polygon2_label = Text("Surface B").next_to(polygon2, DOWN, buff=0.2)
        polygon2.set_fill(BLUE_B)

        self.play(DrawBorderThenFill(polygon1), DrawBorderThenFill(polygon2))
        self.play(Write(polygon1_label), Write(polygon2_label))
        self.wait(2)

        arrow = Arrow(start=RIGHT, end=LEFT, color=GOLD).next_to(polygon2, LEFT, buff=0.75)
        apply_g = MathTex(r"\text{Apply } g").next_to(arrow, UP, buff=0.2)
        self.play(Create(arrow))
        self.play(Write(func1_label))
        self.play(Write(apply_g))
        self.wait(2)

        point = Point(location=np.array([2, 1, 0]), color=BLACK)
        point_label = MathTex(r"(u,v)", color=BLACK).next_to(point, DR, buff=0.2).scale(1.2)
        area_rectangle = Rectangle(width=0.5, height=0.5, fill_opacity=0.3).next_to(point, RIGHT * 0)
        area_rectangle.set_fill(RED)
        self.play(FadeIn(point), Write(point_label))
        self.wait(2)

        transformed_point = Point(location=np.array([-5, 1, 0]), color=BLACK)
        transformed_point_label = MathTex(r"g(u,v)", color=BLACK).next_to(transformed_point, DR, buff=0.2).scale(1.2)
        transformed_area_rectangle = Rectangle(width=0.5, height=0.75, fill_opacity=0.3).next_to(transformed_point, RIGHT * 0).rotate(-20 * DEGREES)
        transformed_area_rectangle.set_fill(RED)

        self.play(FadeIn(transformed_point), Write(transformed_point_label))
        self.play(Create(area_rectangle))
        self.add(area_rectangle.copy())
        self.wait(2)
        self.play(ReplacementTransform(area_rectangle, transformed_area_rectangle))
        self.wait(2)

        self.play(Write(func2_label))
        same_height = Text("Same Height").shift(DOWN * 1.5).scale(0.75)
        different_area = Text("Different Area").next_to(same_height, DOWN).scale(0.75)

        point_arrow = Arrow(same_height, point)
        transformed_point_arrow = Arrow(same_height, transformed_point)
        self.play(Create(point_arrow), Create(transformed_point_arrow))
        self.wait(2)
        self.play(Write(same_height))
        self.wait(2)
        self.play(Write(different_area))
        self.wait(5)
        self.clear()

        area_scale_jacobian = Text("As we zoom in, the transformation from (u,v) to g(u,v) \n closely approximates a linear transformation just like we saw in chapter 3").scale(0.6).shift(UP * 3)
        what_determinant_reps = Text("Since we know the linear transformation at point g(u,v) \n and we want to integrate at that point, \n how can we find the \"area scaling\" factor at that point?").next_to(area_scale_jacobian, DOWN, buff=0.5).scale(0.6)
        the_determinant = Text("THE DETERMINANT").scale(2).next_to(what_determinant_reps, DOWN, buff=0.5)
        jacobian = MathTex(r"""J = 
\begin{bmatrix}
    \frac{\partial x}{\partial u} && \frac{\partial x}{\partial v} \\
    \frac{\partial y}{\partial u} && \frac{\partial y}{\partial v}\\
\end{bmatrix}""").next_to(the_determinant, DOWN, buff=1).scale(1.5)

        self.play(Write(area_scale_jacobian))
        self.wait(2)
        self.play(Write(what_determinant_reps))
        self.wait(2)
        self.play(Write(the_determinant))
        self.wait(2)
        self.play(Write(jacobian))
        self.wait(5)

