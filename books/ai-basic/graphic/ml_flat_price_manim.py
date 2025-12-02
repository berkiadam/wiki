from manim import *
import numpy as np

class LinearRegressionFlatPrice(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 0. ADATOK ÉS GRADIENT DESCENT FUTTATÁSA
        # ---------------------------------------------------------
        sizes = np.array([
            35, 40, 42, 45, 48,
            50, 52, 55, 58, 60,
            62, 65, 68, 70, 72,
            75, 78, 80, 85, 90
        ], dtype=float)

        prices = np.array([
            30, 33, 34, 36, 38,
            40, 41, 43, 45, 47,
            48, 50, 52, 53, 55,
            57, 59, 60, 63, 67
        ], dtype=float)

        X = sizes.reshape(-1, 1)
        ones = np.ones_like(X)
        X_design = np.hstack([X, ones])
        y = prices

        theta = np.zeros(2)  # [w, b]
        learning_rate = 1e-4
        epochs = 20000
        n = len(X_design)

        theta_history = []
        snapshot_every = 1500

        for epoch in range(epochs):
            y_hat = X_design @ theta
            error = y_hat - y
            grad = (2.0 / n) * (X_design.T @ error)
            theta -= learning_rate * grad

            if epoch % snapshot_every == 0 or epoch == epochs - 1:
                theta_history.append(theta.copy())

        final_w, final_b = theta

        # ---------------------------------------------------------
        # 1. CÍM ÉS BEVEZETŐ
        # ---------------------------------------------------------
        title = Text("Lineáris regresszió lakásárakra", font_size=42)
        subtitle = Text(
            "Gradient descent (gradienscsökkentés) animáció",
            font_size=28
        ).next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)

        self.play(
            title.animate.to_edge(UP),
            subtitle.animate.next_to(title, DOWN)
        )

        # ---------------------------------------------------------
        # 2. KOORDINÁTARENDSZER ÉS ADATOK
        # ---------------------------------------------------------
        axes = Axes(
            x_range=[30, 95, 5],
            y_range=[25, 70, 5],
            x_length=8,
            y_length=5,
            tips=False,
        ).to_edge(LEFT).shift(DOWN * 0.5)

        # Itt már NEM Tex-et használunk, hogy ne legyen gond az ékezetekkel
        x_label = Text("alapterület (m²)", font_size=24)
        y_label = Text("ár (millió Ft)", font_size=24)

        x_label.next_to(axes.x_axis, DOWN)
        y_label.rotate(PI / 2).next_to(axes.y_axis, LEFT)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        dots = VGroup()
        for s, p in zip(sizes, prices):
            dot = Dot(axes.coords_to_point(s, p), radius=0.04)
            dots.add(dot)

        data_label = Text(
            "1. Tanító adatok (sizes, prices)",
            font_size=28
        ).to_edge(RIGHT).shift(UP * 2)

        self.play(FadeIn(dots, lag_ratio=0.05), FadeIn(data_label))
        self.wait(1.5)

        # ---------------------------------------------------------
        # 3. KEZDETI MODELL: w=0, b=0
        # ---------------------------------------------------------
        init_w, init_b = 0.0, 0.0

        def get_line(w, b, color=YELLOW):
            return axes.plot(
                lambda x: w * x + b,
                x_range=[30, 95],
                stroke_width=4,
                color=color,
            )

        line = get_line(init_w, init_b)
        model_label = Text(
            "2. Kezdeti modell: ŷ = w·x + b\nw = 0, b = 0",
            font_size=26
        ).to_edge(RIGHT)

        self.play(Create(line), FadeIn(model_label))
        self.wait(1.5)

        # ---------------------------------------------------------
        # 4. GRADIENT DESCENT ANIMÁCIÓ
        # ---------------------------------------------------------
        gd_label = Text(
            "3. Gradient descent\nθ = θ - η · ∇θ MSE",
            font_size=26
        ).to_edge(RIGHT).shift(DOWN * 1.5)

        self.play(FadeIn(gd_label))

        current_line = line

        for (w, b) in theta_history[1:]:
            new_line = get_line(w, b)
            self.play(Transform(current_line, new_line), run_time=0.8)
            self.remove(new_line)

        self.wait(0.5)

        # ---------------------------------------------------------
        # 5. VÉGSŐ MODELL KIÍRÁSA
        # ---------------------------------------------------------
        final_text = Text(
            f"4. Betanult modell:\nár ≈ {final_w:.3f} · alapterület + {final_b:.3f}",
            font_size=26
        ).to_edge(RIGHT).shift(DOWN * 2.5)

        self.play(Write(final_text))
        self.wait(2)

        highlight = SurroundingRectangle(current_line, color=YELLOW, buff=0.1)
        self.play(Create(highlight), run_time=1)
        self.wait(2)
