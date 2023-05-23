from manim import *
from manim.utils.rate_functions import sqrt
from numpy import rec

class TwoDIntergration(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-3, 3, 0.5],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        rectangle = Rectangle(YELLOW, 4, 4, grid_xstep=0.2, grid_ystep=0.2)

        surface = axes.plot_surface(
            lambda u, v: 0.5 * sqrt(u*u + v*v),
            u_range=[-4, 4],
            v_range=[-4, 4],
            checkerboard_colors=[BLUE_B, BLUE_D]
        )

        self.play(Create(axes))
        self.wait()

        self.move_camera(phi=60 * DEGREES)
        self.wait()
        self.move_camera(theta=-45 * DEGREES)

        self.wait()
        self.begin_ambient_camera_rotation(
            rate=PI / 20, about="theta"
        )

        self.play(Create(surface))
        self.wait(3)
        self.play(Create(rectangle, run_time=8))
        self.wait(7)

        self.stop_ambient_camera_rotation()
        self.remove(surface)

        self.move_camera(theta=90 * DEGREES, phi=-180 * DEGREES)
        self.wait(1)

        self.play(ApplyMatrix([[1, 1],[0, 1]], rectangle))
        self.wait(3)

        self.play(ApplyMatrix([[0, -1], [1, 0]], rectangle))
        self.wait(3)

