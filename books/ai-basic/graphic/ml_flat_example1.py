from manim import *
import numpy as np

class ML_Flat_Example1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-20, 20, 2],
            y_range=[-20, 20, 2],
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": True,
                         "font_size": 15}
        ).shift(LEFT * 2)
        self.play(Create(axes))

        # Kezdeti paraméterek
        w = 0.0
        b = 0.0

        eta = 1e-3

        eta_w = 1e-4   # vagy még kisebb
        eta_b = 1e-3

        epochs = 2000
        anim_every = 20
        # Tanító adatok NORMALIZÁLVA a –10..10 demóhoz

        # eredeti adatok
        sizes = np.array([
            35, 40, 42, 45, 48,
            50, 52, 55, 58, 60,
            62, 65, 68, 70, 72,
            75, 78, 80, 85, 90
        ], dtype=float)

        prices = np.array([
            247.1, 262, 300.09, 326.2, 333.2, 
            381.99, 350.49, 382, 425.69, 368.1, 
            417.29, 444, 437.29, 548.009, 527.6, 
            556.99, 555.789, 546.1, 588.39, 605

        ], dtype=float)




        # 1) x értékek skálázása –10..10 közé
        sizes_scaled = (sizes - sizes.mean()) / sizes.std() * 5

        # 2) y értékek skálázása úgy, hogy bias ~2 legyen
        prices_scaled = (prices - prices.mean()) / prices.std() * 4 + 2

        # Ezeket tanítjuk
        X = sizes_scaled.reshape(-1, 1)
        ones = np.ones_like(X)
        X_design = np.hstack([X, ones])
        y = prices_scaled
        n = len(X_design)

        def get_line(w, b):


            print(f"b értéke: {b}")
            print(f"w értéke: {w}")

            return axes.plot(
                lambda x: w * x + b,
                x_range=[-20, 20],
                color=YELLOW
            )

        line = get_line(w, b)
        self.play(Create(line))

        # ---------------------------
        #  LEARNING... VILLOGÓ SZÖVEG
        # ---------------------------
        learning_text = Text("Learning...", color=BLUE).scale(0.7)
        learning_text.to_corner(UR)

        self.play(FadeIn(learning_text))

        # Rövidített tudásszöveg
        param_text = Text(
            f"w = {w:.2f},  b = {b:.2f}",
            font_size=32,
            color=WHITE
        ).to_corner(UL)
        self.play(Write(param_text))

        total_runtime = 10
        num_anim_steps = epochs // anim_every
        time_per_anim = total_runtime / max(1, num_anim_steps)

        blink_state = 1  # villogás állapot

        for epoch in range(epochs):
            # --- Tanulás ---
            y_hat = X_design @ np.array([w, b])
            error = y_hat - y
            grad = (2.0 / n) * (X_design.T @ error)
            dw, db = grad

            w -= eta_w * dw
            b -= eta_b * db

            # Minden anim_every-edik epochnál frissítünk
            if epoch % anim_every == 0 or epoch == epochs - 1:
                new_line = get_line(w, b)
                new_param_text = MathTex(
                    fr"w = {w:.3e},\ b = {b:.3e}"
                ).scale(0.7).to_corner(UL)

                # 👁 VILLOGÁS: opacitás váltogatása
                blink_state = 1 - blink_state
                learning_text.set_opacity(blink_state)

                self.play(
                    Transform(line, new_line),
                    Transform(param_text, new_param_text),
                    rate_func=linear,
                    run_time=time_per_anim
                )

        # -------------------------------
        # LEARNING → MODEL IS READY
        # -------------------------------

        ready_text = Text("Model is ready", color=GREEN).scale(0.7)
        ready_text.to_corner(UR)

        self.play(
            FadeOut(learning_text),
            FadeIn(ready_text),
            run_time=1
        )

        self.wait(0.5)

        # -------------------------------
        # POST-TRAIN QUERY
        # -------------------------------

        query_x = 15.1  # 15.1 m²
        query_y = w * query_x + b

        # piros kérdés szöveg
        question = Text(
            "How much does a 15.1 m² apartment cost?",
            color=RED
        ).scale(0.55).to_edge(RIGHT).shift(UP * 2)
        self.play(Write(question))

        # pont a függvényen
        point = axes.coords_to_point(query_x, query_y)
        dot = Dot(point, color=RED)

        # vetítések
        x_axis_point = axes.coords_to_point(query_x, 0)
        y_axis_point = axes.coords_to_point(0, query_y)

        v_line = DashedLine(point, x_axis_point, color=RED, stroke_width=2)
        h_line = DashedLine(point, y_axis_point, color=RED, stroke_width=2)

        x_label = MathTex("15.1", color=RED).scale(0.5).next_to(x_axis_point, DOWN)
        y_label = MathTex(f"{query_y:.2f}", color=RED).scale(0.5).next_to(y_axis_point, LEFT)

        self.play(
            FadeIn(dot),
            Create(v_line),
            Create(h_line),
            Write(x_label),
            Write(y_label),
            run_time=2
        )

        self.wait(3)
