import graph_generation as gg
import imperfect_examples as imp
from manim_setup import *


class Clique(Scene):
    def construct(self):
        v, e = gg.complete(4)
        v += list(range(5, 13))
        e += [
            (1, 5),
            (4, 5),
            (1, 9),
            (2, 9),
            (5, 9),
            (9, 10),
            (9, 6),
            (4, 7),
            (5, 7),
            (2, 11),
            (3, 11),
            (10, 12),
            (11, 12),
            (6, 8),
            (6, 7),
            (7, 8),
            (2, 10),
            (6, 10),
            (10, 11),
            (8, 10),
        ]
        lt = {
            1: [-1, 1, 0],
            2: [1, 1, 0],
            3: [1, -1, 0],
            4: [-1, -1, 0],
            5: [-2.5, 2, 0],
            6: [-2, 3.5, 0],
            7: [-7, 2.5, 0],
            8: [-5, 5, 0],
            9: [0.5, 3, 0],
            10: [3, 3.5, 0],
            11: [5, 2, 0],
            12: [6, 5, 0],
        }
        G = Graph(
            v,
            e,
            layout=lt,
        )
        clique = Text("clique", color=RED, slant=ITALIC)
        clique.move_to([0, -2, 0])
        self.play(Create(G))
        self.wait(5)
        self.play(
            G.animate.add_edges(
                *gg.complete(4)[1],
                edge_config={edge: {"stroke_color": RED} for edge in gg.complete(4)[1]},
            )
        )
        self.wait()
        self.add(clique)
        self.wait()
        self.play(
            G[1].animate.scale(2),
            G[2].animate.scale(2),
            G[3].animate.scale(2),
            G[4].animate.scale(2),
        )
        self.wait(0.25)
        self.play(
            G[1].animate.set_color(BLUE_E),
            G[2].animate.set_color(PURE_GREEN),
            G[3].animate.set_color(PURE_BLUE),
            G[4].animate.set_color(PINK),
        )
        self.wait(5)


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
            Graph(
                *imp.C7_complement(),
                layout_scale=scale,
                layout="circular",
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
            Create(graphs[5]),
            run_time=1.5,
        )
        self.wait(6)
        self.play(
            graphs[0].animate.add_edges(
                *gg.cycle(5)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(5)[1]},
            ),
            graphs[1].animate.add_edges(
                *gg.cycle(5)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(5)[1]},
            ),
            graphs[2].animate.add_edges(
                *gg.cycle(5)[1],
                edge_config={e: {"stroke_color": PURE_RED} for e in gg.cycle(5)[1]},
            ),
        )
        self.wait(2)
        self.play(
            graphs[0].animate.remove_vertices(6),
            graphs[1].animate.remove_vertices(6, 7),
            graphs[2].animate.remove_vertices(6, 7),
        )
        self.wait(3)
        self.play(
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
        self.play(
            graphs[3].animate.remove_vertices(8, 9),
            graphs[4].animate.remove_vertices(10, 11, 12),
        )
        self.wait(1)
        self.play(LaggedStartMap(FadeOut, graphs[:-1], shift=2 * LEFT))
        self.play(graphs[-1].animate.change_layout("circular", layout_scale=2))
        self.wait()
        v, e = gg.cycle(7)
        C7 = Graph(
            v,
            [],
            layout="circular",
            layout_scale=2,
        )
        self.add(C7)
        self.play(
            C7.animate.add_edges(
                *e,
                edge_config={edge: {"stroke_color": PURE_BLUE} for edge in e},
            )
        )
        self.wait()
        self.play(VGroup(graphs[-1], C7).animate.arrange(buff=LARGE_BUFF))
        self.wait()
        self.play(FadeOut(graphs[-1]), C7.animate.change_layout("circular"))
        graphs[-1] = C7
        self.play(
            C7.animate.change_layout("circular", layout_scale=scale),
            FadeIn(graphs[:-1]),
        )
        self.play(graphs.animate.arrange_in_grid(buff=LARGE_BUFF))
        self.wait()
