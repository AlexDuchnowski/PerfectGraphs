from manim_setup import *


class Title(Scene):
    def construct(self):
        lines = VGroup(
            Text("Perfect Graphs", font_size=80, font=FONT, weight=BOLD),
            Text("Alex Duchnowski & Luke Hammer", font_size=50, font=FONT),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(lines[1]))
        self.wait(2)
        self.play(Write(lines[0]))
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, lines, run_time=1.25))


class IsThisBoundSharp(Scene):
    def construct(self):
        # Tex to color map
        t2c = {
            "\chi": BLUE,
            "\omega": TEAL,
            "G": GREEN,
            "\geq": ORANGE,
            "=": RED,
        }
        # Configuration to pass along to each Tex mobject
        kw = dict(font_size=72, tex_to_color_map=t2c)
        lines = VGroup(
            MathTex("\chi(G)\geq\omega(G)", **kw),
            MathTex("\chi(G)=\omega(G)", **kw),
            Text(
                "Is this bound sharp?",
                font=FONT,
                t2s={"sharp": ITALIC},
                t2w={"sharp": BOLD},
                t2c={"sharp": RED},
            ),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(Write(lines[0]), run_time=3)
        self.wait(WAIT_TIME)
        self.play(Write(lines[2], run_time=1))
        self.wait(WAIT_TIME)
        self.play(
            TransformMatchingTex(
                lines[0].copy(),
                lines[1],
                matched_keys=["\chi", "\omega", "G"],
            ),
        )
        self.wait()
        self.play(LaggedStartMap(FadeOut, lines[0], shift=2 * RIGHT, run_time=1))
        self.play(LaggedStartMap(FadeOut, lines[2], shift=2 * RIGHT, run_time=1))


class PerfectDefinition(Scene):
    def construct(self):
        defn = Tex(
            "A graph $G$ is \\underline{perfect} if and only if the chromatic number \\\\ equals the size of the maximum clique, both\\\\in the graph itself and in every induced subgraph."
        )
        self.play(Write(defn), run_time=10)
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, defn, run_time=1))
