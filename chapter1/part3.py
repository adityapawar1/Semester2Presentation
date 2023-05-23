from manim import *
class DeterminantOfMatrixB(LinearTransformationScene):

    CONFIG = {
        "show_coordinates": True,
        "background_line_style": {
            "stroke_width": 3,
        },
        "show_basis_vectors": False,
        "i_hat_color": BLUE,
        "j_hat_color": GREEN,
        "back_basis_cols": [BLUE, GREEN],
        "fore_basis_cols": ["#d40b37", "#d4b90b"],
        "t_matrix": [[2, 0], [-1, 1]],
        "t_i_matrix": [[2, 0], [0, 1]],
        "t_j_matrix": [[1, 0], [-1, 1]],
        "a_b_cols": [BLUE, GREEN],
        "det_col": YELLOW_D,
    }

    def construct(self):
        self.back_basis_cols = [BLUE, GREEN]
        self.fore_basis_cols = ["#d40b37", "#d4b90b"]
        self.a_b_cols = [BLUE, GREEN]
        self.back_basis_cols= [BLUE, GREEN]
        self.fore_basis_cols= ["#d40b37", "#d4b90b"]
        self.t_matrix= [[2, 0], [-1, 1]]
        self.t_i_matrix= [[2, 0], [0, 1]]
        self.t_j_matrix= [[1, 0], [-1, 1]]
        self.a_b_cols= [BLUE, GREEN]
        self.det_col= YELLOW_D

        back_grid, fore_grid = self.background_plane, self.plane
        back_basis = self.get_basis_vectors(*self.back_basis_cols)
        fore_basis = self.get_basis_vectors(*self.fore_basis_cols)
        back_sq = self.get_unit_square().set_color_by_gradient(*self.back_basis_cols)
        fore_sq = self.get_unit_square().set_color_by_gradient(*self.fore_basis_cols)

        fore_mobs = VGroup(fore_grid, fore_sq, fore_basis)
        back_mobs = VGroup(back_grid, back_basis, back_sq)

        standard_basis_text = (
            Text("standard basis")
            .to_corner(UP + RIGHT)
            .set_color_by_gradient(*self.back_basis_cols)
        )
        trans_basis_text = (
            Text("transformed basis")
            .next_to(standard_basis_text, DOWN)
            .shift(0.3 * LEFT)
            .set_color_by_gradient(*self.fore_basis_cols)
        )

        self.add(back_grid, back_basis, back_sq, standard_basis_text)
        self.wait()

        b_equals = Text("B =")
        b_equals[0].set_color(self.a_b_cols[1]).scale(1.5)
        matrix = (
            Matrix(
                np.array(self.t_matrix).transpose(), include_background_rectangle=True
            )
            .scale(0.75)
            .set_column_colors(*self.fore_basis_cols)
        )
        b_matrix = VGroup(b_equals, matrix).arrange_submobjects().shift(UP + 4 * LEFT)

        self.play(
            Write(b_equals), FadeIn(matrix.background_rectangle), Write(matrix.brackets)
        )
        self.wait()
        self.play(Write(matrix.get_columns()[0]))
        self.play(Write(matrix.get_columns()[1]))
        self.wait()

        self.moving_vectors += fore_basis
        self.transformable_mobjects += [fore_grid, fore_sq]

        self.play(*[GrowFromPoint(mob, ORIGIN) for mob in fore_mobs[1:]])

        self.remove(fore_basis, fore_grid)
        self.play(Wiggle(back_basis[0]))
        self.add(fore_basis, fore_grid)

        self.moving_mobjects = []
        self.apply_transposed_matrix(
            self.t_i_matrix,
            run_time=1,
            added_anims=[
                FadeIn(matrix.get_columns()[0], opacity=0.5)
            ],
        )
        self.remove(*self.moving_vectors, fore_grid)
        self.play(Wiggle(back_basis[1]))
        self.add(fore_grid, fore_basis)
        self.moving_mobjects = []
        self.apply_transposed_matrix(
            self.t_j_matrix,
            run_time=1,
            added_anims=[FadeIn(matrix.get_columns()[1])],
        )
        self.play(Write(trans_basis_text, lag_ratio=0.3))
        self.wait()

        self.play(ApplyWave(back_sq, amplitude=0.5), run_time=2)
        self.play(ApplyWave(fore_sq, amplitude=0.5), run_time=2)
        self.wait()

        self.play(
            ApplyMethod(b_matrix.to_corner, UP + LEFT),
            FadeOut(standard_basis_text),
            FadeOut(trans_basis_text),
            ApplyMethod(back_sq.shift, 4 * LEFT),
            ApplyMethod(back_basis.shift, 4 * LEFT),
        )

        curved_arrow = CurvedArrow(
            back_sq.get_right() + 0.2 * RIGHT,
            fore_sq.get_left() + 0.2 * LEFT,
            angle=-PI / 4,
        )
        question_mark = Text("X ?").set_color(self.det_col).next_to(curved_arrow, UP)
        question_mark[0][0].set_color(WHITE)
        scaled_area = VGroup(curved_arrow, question_mark)
        self.play(Create(scaled_area))

        fade_mobs = [back_grid, fore_grid]
        self.play(*[ApplyMethod(mob.fade, darkness=0.1) for mob in fade_mobs])

        transformed_rect = Polygon(
            ORIGIN,
            [-0.5, 0.5, 0],
            [1.5, 0.5, 0],
            [2, 0, 0],
            stroke_color=back_sq.get_stroke_color(),
            fill_color=back_sq.get_fill_color(),
            fill_opacity=back_sq.get_fill_opacity(),
        )
        transformed_rects = [
            transformed_rect,
            transformed_rect.copy().shift(0.5 * (UP + LEFT)),
        ]

        for index, rect in enumerate(transformed_rects):
            factor = (
                Text(f"{index+1}", color=self.det_col)
                .scale(1.5)
                .next_to(question_mark[0][0])
                .add_background_rectangle()
            )
            try:
                self.play(
                    TransformFromCopy(back_sq, rect), Transform(question_mark[0][1], factor)
                )
                self.wait(0.5)
            except:
                pass

        det_b = MathTex("det(B)", " = ").scale(1.5).next_to(b_matrix, 2 * RIGHT)
        det_b[0][:3].set_color(self.det_col)
        det_b[0][4].set_color(self.a_b_cols[0])
        self.play(Write(det_b))
        self.play(ApplyMethod(factor.copy().next_to, det_b, RIGHT))
        self.wait(3)

        fade_mobs = [mob for mob in self.mobjects if mob is not back_grid]
        for mob in fade_mobs:
            mob.fade(0.5)

        self.play(ApplyWave(back_grid, amplitude=2), run_time=2)
        self.wait()

