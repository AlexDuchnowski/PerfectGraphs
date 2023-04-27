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


class PerfectDefinition(Scene):
    def construct(self):
        text = VGroup(
            Text(
                "A graph G is perfect if and only if",
                font=FONT,
                t2s={"G": ITALIC, "perfect": ITALIC},
                t2w={"perfect": BOLD},
            ),
            Text("the chromatic number equals"),
            Text("the size of the maximum clique"),
            Text("both in the graph itself and"),
            Text("in every induced subgraph."),
        )
        text.arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(text), run_time=10)
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, text))


class WeakPerfectGraphTheorem(Scene):
    def construct(self):
        lines = VGroup(
            Text("The Weak Perfect Graph Theorem", font=FONT, weight=BOLD),
            Tex("A graph $G$ is perfect if and only if \\overline{$G$} is perfect."),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(lines[0]))
        self.wait(2)
        self.play(Write(lines[1]))
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, lines))


class StrongPerfectGraphTheorem(Scene):
    def construct(self):
        lines = VGroup(
            Text("The Strong Perfect Graph Theorem", font=FONT, weight=BOLD),
            Tex(
                "A graph $G$ is perfect if and only if it contains no odd hole or odd antihole."
            ),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        self.play(Write(lines[0]))
        self.wait(2)
        self.play(Write(lines[1]))
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, lines))
