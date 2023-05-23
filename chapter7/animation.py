from manim import *

class JacobianVisualization(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=20 * DEGREES, theta=-45 * DEGREES)

        # Define a grid of small rectangles using ParametricSurface
        rect_surfaces = VGroup(*[
            Surface(
                lambda u, v: np.array([i + u, j + v, 0]),
                u_range=[0, 0.1], v_range=[0, 0.1],
                resolution=(10, 10), fill_opacity=0.5
            )
            for i in np.arange(0, 1, 0.1)
            for j in np.arange(0, 1, 0.1)
        ])
        rect_label = Text("Rectangular: dA = dx dy").to_edge(UP)

        # Define the equivalent polar sectors using ParametricSurface
        polar_surfaces = VGroup(*[
            Surface(
                lambda u, v: np.array([(i + u)*np.cos(j + v), (i + u)*np.sin(j + v), 0]),
                u_range=[0, 0.1], v_range=[0, PI/2],
                resolution=(10, 10), fill_opacity=0.5
            )
            for i in np.arange(0, 1, 0.1)
            for j in np.arange(0, PI/2, PI/20)
        ])
        polar_label = Text("Polar: dA = r dr dθ").to_edge(UP)

        # Define the Jacobian label
        jacobian_label = Text("|J| = r").to_edge(DOWN)

        # Animate
        self.play(Create(axes), Write(rect_label), Create(rect_surfaces))
        self.wait(2)
        for rect_surface, polar_surface in zip(rect_surfaces, polar_surfaces):
            self.play(Transform(rect_surface, polar_surface), run_time=0.2)
        self.play(Transform(rect_label, polar_label), Write(jacobian_label))
        self.wait(2)