import graph_generation as gg
import imperfect_examples as imp
from manim_setup import *


class C7Complement(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7]
        edges = [(i, j) for i in range(1, 8) for j in range(i + 1, 8)].remove((1, 7))
        g1 = Graph(
            vertices,
            edges,
            layout="circular",
            layout_scale=2,
            vertex_config={"radius": 0.20},
        )
        g2 = Graph(
            vertices,
            [(1, 6), (2, 5)],
            layout="circular",
            layout_scale=2,
            vertex_config={"radius": 0.20},
            edge_config={(1, 6): {"stroke_color": RED}, (2, 5): {"stroke_color": RED}},
        )
        self.play(Create(g1, run_time=2))
        self.wait()
        self.play(FadeIn(g2))
        self.play(FadeOut(g1, run_time=2))
        self.wait()


class PropertyPerseverence(Scene):
    def construct(self):
        v, e = gg.complete(8)
        K = Graph(v, e, layout="circular")
        N = Graph(v, [], layout="circular")
        v, e = gg.complete_multipartite([4, 5])
        B = Graph(
            v,
            e,
            vertex_config={
                i: {"fill_color": PURE_BLUE} if i < 5 else {"fill_color": PURE_GREEN}
                for i in range(1, 10)
            },
            layout="partite",
            partitions=[list(range(1, 5)), list(range(5, 10))],
            layout_scale=3,
        )
        self.play(Create(K))
        self.play(
            K[1].animate.set_color(PURE_RED),
            # K[1].animate.scale(3),
            K[4].animate.set_color(PURE_RED),
            # K[4].animate.scale(3),
        )
        self.wait(0.5)
        self.play(K.animate.remove_vertices(1, 4))
        self.wait(0.5)
        self.play(K.animate.change_layout("circular"))
        self.wait()
        self.play(FadeOut(K))
        self.play(Create(N))
        self.play(
            N[1].animate.set_color(PURE_RED),
            N[3].animate.set_color(PURE_RED),
        )
        self.play(N.animate.remove_vertices(1, 3), run_time=0.5)
        self.play(N.animate.change_layout("circular"))
        self.play(FadeOut(N))
        self.play(Create(B))
        self.play(
            B[2].animate.set_color(PURE_RED),
            B[5].animate.set_color(PURE_RED),
            B[8].animate.set_color(PURE_RED),
        )
        self.play(B.animate.remove_vertices(2, 5, 8))
        self.play(B.animate.change_layout("partite", partitions=[[1, 3, 4], [6, 7, 9]]))
        self.wait()
        self.play(
            B.animate.add_vertices(
                2,
                5,
                8,
                vertex_config={
                    i: {"fill_color": PURE_BLUE}
                    if i < 5
                    else {"fill_color": PURE_GREEN}
                    for i in range(1, 10)
                },
            ),
            run_time=0.25,
        )
        self.play(
            B.animate.change_layout(
                "partite", partitions=[list(range(1, 5)), list(range(5, 10))]
            )
        )
        self.play(
            B.animate.add_edges(
                *[edge for edge in e if edge[0] == 2 or edge[1] in [5, 8]]
            )
        )
        self.wait()
        self.play(
            B[1].animate.set_color(PURE_RED),
            B[2].animate.set_color(PURE_RED),
            B[3].animate.set_color(PURE_RED),
            B[4].animate.set_color(PURE_RED),
        )
        self.play(B.animate.remove_vertices(1, 2, 3, 4))
        self.wait(0.5)
        self.play(B.animate.change_layout("circular"))
        self.play(
            B[5].animate.set_color(WHITE),
            B[6].animate.set_color(WHITE),
            B[7].animate.set_color(WHITE),
            B[8].animate.set_color(WHITE),
            B[9].animate.set_color(WHITE),
            run_time=0.5,
        )
        self.wait()


class ImperfectGraphs(Scene):
    def construct(self):
        scale = 1.5
        graphs = VGroup(
            Graph(
                *gg.cycle(5),
                layout_scale=scale,
                layout="circular",
            ),
            Graph(
                *imp.C5_with_square(),
                layout_scale=scale,
                layout="kamada_kawai",
            ),
            Graph(
                *imp.moser_spindle(),
                layout_scale=scale,
                layout="kamada_kawai",
            ),
            Graph(
                *imp.C7_with_interior_stuff(),
                layout_scale=scale,
                layout="kamada_kawai",
            ),
            Graph(
                *imp.C9_with_interior_stuff(),
                layout_scale=scale,
                layout="kamada_kawai",
            ),
        )
        graphs[0].add_vertices(6)
        graphs[0].add_edges((1, 6), (2, 6), (4, 6))
        graphs.arrange_in_grid(buff=LARGE_BUFF)
        self.play(
            Create(graphs[0]),
            Create(graphs[1]),
            Create(graphs[2]),
            Create(graphs[3]),
            Create(graphs[4]),
            run_time=1.5,
        )
        self.wait(5)
        self.play(
            graphs[0].animate.add_edges(
                *gg.cycle(5)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(5)[1]},
            ),
            graphs[1].animate.add_edges(
                *gg.cycle(5)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(5)[1]},
            ),
            graphs[3].animate.add_edges(
                *gg.cycle(7)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(7)[1]},
            ),
            graphs[4].animate.add_edges(
                *gg.cycle(9)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(9)[1]},
            ),
            run_time=1.5,
        )
        self.wait()
