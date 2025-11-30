from manim import *

class GradientDescentUpdate(Scene):
    def construct(self):
        # Tengelyek
        axes = Axes(
            x_range=[0, 60, 10],
            y_range=[0, 60, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True}
        ).to_edge(LEFT)

        self.play(Create(axes))

        # Kezdeti paraméterek
        w_initial = 0.1
        w_new = 0.05

        # Kezdeti egyenes: y = w_initial * x
        line_initial = axes.plot(lambda x: w_initial * x, color=RED)
        label_initial = MathTex(r"y = 0.1x", color=RED).next_to(line_initial, UP)

        self.play(Create(line_initial), FadeIn(label_initial))

        # Képletek megjelenítése
        formula1 = MathTex(
            r"w \leftarrow w - \eta \frac{\partial L}{\partial w}"
        ).scale(0.8).to_edge(UP).shift(RIGHT * 2)

        formula2 = MathTex(
            r"w \leftarrow 0.1 - 0.01 \cdot 5"
        ).scale(0.8).next_to(formula1, DOWN)

        formula3 = MathTex(
            r"w \leftarrow 0.1 - 0.05 = 0.05"
        ).scale(0.8).next_to(formula2, DOWN)

        self.play(Write(formula1))
        self.play(Write(formula2))
        self.play(Write(formula3))

        # Új egyenes (y = 0.05x)
        line_new = axes.plot(lambda x: w_new * x, color=YELLOW)
        label_new = MathTex(r"y = 0.05x", color=YELLOW).next_to(line_new, UP)

        # Animáció: a piros egyenes morfol a sárgává
        self.play(
            Transform(line_initial, line_new),
            Transform(label_initial, label_new),
            run_time=3
        )

        self.wait(2)
