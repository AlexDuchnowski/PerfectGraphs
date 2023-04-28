import graph_generation as gg
import imperfect_examples as imp
import perfect_examples as perf
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


class IsThisBoundSharp(Scene):
    def construct(self):
        # t2c = {"\chi": BLUE, "\omega": RED, "G": GREEN, "\geq": GOLD, "=": YELLOW}
        # kw = dict(font_size=80, tex_to_color_map=t2c)
        lines = VGroup(
            MathTex("\chi(G)\geq\omega(G)", **kw),
            MathTex("\chi(G)=\omega(G)", **kw),
            Text(
                "Is this bound sharp?",
                font=FONT,
                t2s={"sharp": ITALIC},
                t2w={"sharp": BOLD},
                t2c={"sharp": YELLOW},
            ),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)

        self.play(Write(lines[0]), run_time=2)
        self.wait(3)
        self.play(Write(lines[2]))
        self.wait()
        self.play(
            TransformMatchingTex(
                lines[0].copy(),
                lines[1],
                matched_keys=["\chi", "\omega", "G", "(", ")"],
            ),
        )
        self.wait()
        self.play(
            LaggedStartMap(FadeOut, lines[0], shift=2 * RIGHT),
            LaggedStartMap(FadeOut, lines[2], shift=2 * RIGHT),
        )
        self.play(lines[1].animate.move_to([0, 3.25, 0]))
        lt_scale = 1.25
        graphs = VGroup(
            Graph(
                *gg.complete(6),
                vertex_config={i + 1: {"fill_color": COLOR_SEQ[i]} for i in range(6)},
                edge_config={e: {"stroke_color": RED} for e in gg.complete(6)[1]},
                layout="circular",
                layout_scale=lt_scale,
            ),
            Graph(
                list(range(1, 7)),
                [],
                vertex_config={i + 1: {"fill_color": COLOR_SEQ[0]} for i in range(6)},
                layout="circular",
                layout_scale=lt_scale,
            ),
            Graph(
                *gg.complete_multipartite([3, 3]),
                vertex_config={
                    i + 1: {"fill_color": COLOR_SEQ[i < 3]} for i in range(6)
                },
                edge_config={(2, 4): {"stroke_color": RED}},
                layout="partite",
                partitions=[[1, 2, 3], [4, 5, 6]],
                layout_scale=lt_scale,
            ),
            Graph(
                *gg.complete_multipartite([2, 2, 1, 1]),
                vertex_config={
                    i + 1: {"fill_color": COLOR_SEQ[[0, 0, 1, 1, 2, 3][i]]}
                    for i in range(6)
                },
                edge_config={
                    ([1, 3, 5, 6][i], [1, 3, 5, 6][j]): {"stroke_color": RED}
                    for i in range(4)
                    for j in range(i + 1, 4)
                },
                layout={
                    1: [-1.25, 0.75, 0],
                    2: [-0.75, 1.25, 0],
                    3: [0.75, 1.25, 0],
                    4: [1.25, 0.75, 0],
                    5: [1, -1, 0],
                    6: [-1, -1, 0],
                },
                layout_scale=lt_scale,
            ),
        )
        center_graph = Graph(
            list(range(1, 7)),
            [(1, 2), (1, 3), (2, 3), (4, 5)],
            vertex_config={
                i + 1: {"fill_color": COLOR_SEQ[[0, 1, 2, 0, 1, 0][i]]}
                for i in range(6)
            },
            edge_config={e: {"stroke_color": RED} for e in [(1, 2), (1, 3), (2, 3)]},
            layout="circular",
            layout_scale=lt_scale,
        )
        graphs.arrange_in_grid(buff=(5, LARGE_BUFF))
        self.wait()
        self.play(Create(graphs[0]), run_time=2)
        self.wait(3)
        self.play(Create(graphs[1]), run_time=2)
        self.wait()
        self.play(Create(graphs[2]), run_time=2)
        self.wait(3)
        self.play(Create(graphs[3]), run_time=2)
        self.wait(5)
        self.play(Create(center_graph))
        self.wait(3)


class PropertyPerseverence(Scene):
    def construct(self):
        K = Graph(
            *gg.complete(8),
            layout="circular",
            vertex_config={i + 1: {"fill_color": COLOR_SEQ[i]} for i in range(8)},
        )
        N = Graph(
            list(range(1, 9)),
            [],
            layout="circular",
            vertex_config={i + 1: {"fill_color": COLOR_SEQ[0]} for i in range(8)},
        )
        B = Graph(
            *gg.complete_multipartite([4, 5]),
            vertex_config={
                i: {"fill_color": PURE_BLUE} if i < 5 else {"fill_color": PURE_GREEN}
                for i in range(1, 10)
            },
            layout="partite",
            partitions=[list(range(1, 5)), list(range(5, 10))],
            layout_scale=3,
        )
        parts = [[1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11, 12]]
        M = Graph(
            *gg.complete_multipartite([2, 3, 3, 4]),
            layout="circular",
            layout_scale=3,
            vertex_config={
                v: {"fill_color": COLOR_SEQ[i]} for i in range(4) for v in parts[i]
            },
        )
        self.play(Create(K))
        self.play(
            K[1].animate.set_color(PURE_RED),
            K[4].animate.set_color(PURE_RED),
        )
        self.wait(0.5)
        self.play(K.animate.remove_vertices(1, 4))
        self.wait(0.5)
        self.play(K.animate.change_layout("circular"))
        self.wait()
        self.play(Uncreate(K))
        self.play(Create(N), run_time=0.5)
        self.play(
            N[1].animate.set_color(PURE_RED),
            N[3].animate.set_color(PURE_RED),
        )
        self.play(N.animate.remove_vertices(1, 3), run_time=0.5)
        self.play(N.animate.change_layout("circular"))
        self.play(Uncreate(N))
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
                *[
                    edge
                    for edge in gg.complete_multipartite([4, 5])[1]
                    if edge[0] == 2 or edge[1] in [5, 8]
                ]
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
        self.wait()
        self.play(Uncreate(B))
        self.play(Create(M), run_time=2)
        self.wait()
        self.play(
            M[1].animate.set_color(PURE_RED),
            M[5].animate.set_color(PURE_RED),
            M[10].animate.set_color(PURE_RED),
            M[12].animate.set_color(PURE_RED),
        )
        self.play(M.animate.remove_vertices(1, 5, 10, 12))
        self.wait()
        self.play(M.animate.change_layout("circular", layout_scale=3))
        self.wait(2)
        self.play(Uncreate(M))


class NotGuaranteed(Scene):
    def construct(self):
        G = Graph(
            *gg.cycle(5),
            vertex_config={
                i + 1: {"radius": 0.2, "fill_color": COLOR_SEQ[[0, 1, 0, 1, 2][i]]}
                for i in range(5)
            },
            layout_scale=3,
            layout="circular",
        )
        G.rotate(13 * PI / 10)
        G.add_vertices(
            6,
            vertex_config={6: {"radius": 0.2, "fill_color": COLOR_SEQ[2]}},
        )
        G.add_edges((1, 6), (2, 6), (4, 6))
        # G.shift(0.425 * LEFT)
        # t2c = {"\chi": BLUE, "\omega": RED, "G": GREEN, r"\neq": PURE_RED}
        # kw = dict(font_size=80, tex_to_color_map=t2c)
        stats_before = MathTex("\chi(G)=3=3=\omega(G)", **kw)
        stats_after = MathTex(r"\chi(G)=3\neq 2=\omega(G)", **kw)
        group = VGroup(G, stats_before).arrange(DOWN, buff=LARGE_BUFF)
        stats_after.move_to(stats_before)
        self.play(Create(G))
        self.wait()
        self.play(Write(stats_before))
        self.wait(2)
        self.play(
            G.edges[(1, 2)].animate.set_color(RED),
            G.edges[(1, 6)].animate.set_color(RED),
            G.edges[(2, 6)].animate.set_color(RED),
        )
        self.wait()
        self.play(
            G.edges[(1, 2)].animate.set_color(WHITE),
            G.edges[(1, 6)].animate.set_color(WHITE),
            G.edges[(2, 6)].animate.set_color(WHITE),
        )
        self.wait(3)
        self.play(G[6].animate.set_color(PURE_RED), run_time=1.5)
        self.wait()
        self.play(G.animate.remove_vertices(6))
        self.wait(0.5)
        self.play(
            TransformMatchingTex(
                stats_before,
                stats_after,
                matched_keys=["\chi", "\omega", "=", "3"],
            ),
        )
        self.wait(5)


class Complements(Scene):
    def construct(self):
        group_1 = VGroup(
            Graph(*gg.complete(10), layout="circular"),
            Graph(list(range(1, 11)), [], layout="circular"),
        )
        K3_1 = gg.complete(3)
        K3_2 = gg.shift(*K3_1, 3)
        K3_3 = gg.shift(*K3_2, 3)
        c_1 = {i + 1: COLOR_SEQ[(i // 3) - 1] for i in range(9)}
        c_2 = {i + 1: COLOR_SEQ[i % 3] for i in range(9)}
        group_2 = VGroup(
            Graph(
                *gg.complete_multipartite([3, 3, 3]),
                layout="circular",
            ),
            Graph(
                K3_1[0] + K3_2[0] + K3_3[0],
                K3_1[1] + K3_2[1] + K3_3[1],
                layout="circular",
            ),
        )
        group_3 = VGroup(
            Graph(*gg.cycle(5), layout="circular"),
            Graph(
                [1, 4, 2, 5, 3],
                gg.cycle(5)[1],
                layout="circular",
            ),
        )
        groups = [group_1, group_2, group_3]
        for i in range(len(groups)):
            self.play(Create(groups[i][0]), Create(groups[i][1]))
            self.wait()
            self.play(groups[i].animate.arrange(RIGHT, buff=LARGE_BUFF))
            if i == 0:
                for j in range(1, 11):
                    self.play(
                        group_1[0][j].animate.set_color(COLOR_SEQ[j - 1]),
                        group_1[1][j].animate.set_color(COLOR_SEQ[0]),
                        run_time=0.1,
                    )
            if i == 1:
                for j in range(1, 10):
                    self.play(
                        group_2[0][j].animate.set_color(c_1[j]),
                        group_2[1][j].animate.set_color(c_2[j]),
                        run_time=0.1,
                    )
                for j in range(1, 10, 3):
                    self.play(
                        group_2[0][j].animate.move_to(
                            (
                                group_2[0][j].get_center()
                                + group_2[0][j + 1].get_center()
                            )
                            / 2
                        ),
                        group_2[1][j].animate.move_to(
                            (
                                group_2[1][j].get_center()
                                + group_2[1][j + 1].get_center()
                            )
                            / 2
                        ),
                        group_2[0][j + 2].animate.move_to(
                            (
                                group_2[0][j + 2].get_center()
                                + group_2[0][j + 1].get_center()
                            )
                            / 2
                        ),
                        group_2[1][j + 2].animate.move_to(
                            (
                                group_2[1][j + 2].get_center()
                                + group_2[1][j + 1].get_center()
                            )
                            / 2
                        ),
                        run_time=0.5,
                    )
            if i == 2:
                for j in range(1, 6):
                    self.play(
                        group_3[0][j].animate.set_color(
                            COLOR_SEQ[[0, 1, 0, 1, 2][j - 1]]
                        ),
                        group_3[1][j].animate.set_color(
                            COLOR_SEQ[[0, 1, 0, 1, 2][j - 1]]
                        ),
                        run_time=0.1,
                    )
                self.wait()
                self.play(
                    group_3[1][2].animate.move_to(groups[i][1][4]),
                    group_3[1][3].animate.move_to(groups[i][1][2]),
                    group_3[1][4].animate.move_to(groups[i][1][5]),
                    group_3[1][5].animate.move_to(groups[i][1][3]),
                )
            self.wait(3)
            self.play(Uncreate(groups[i][0]), Uncreate(groups[i][1]))
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
        moser_cycle = [(1, 6), (6, 4), (4, 7), (7, 2), (2, 1)]
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
                *moser_cycle,
                edge_config={e: {"stroke_color": PURE_RED} for e in moser_cycle},
            ),
        )
        self.wait(2)
        self.play(
            graphs[0].animate.remove_vertices(6),
            graphs[1].animate.remove_vertices(6, 7),
            graphs[2].animate.remove_vertices(3, 5),
        )
        self.wait(3)
        self.play(FadeOut(graphs))
        hole_defn = Tex(r"A \underline{hole} is an induced cycle of length at least 4.")
        self.play(Write(hole_defn))
        self.wait(3)
        self.play(Unwrite(hole_defn))
        self.play(FadeIn(graphs))
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
        self.play(FadeOut(graphs[-1], C7))
        antihole_defn = VGroup(
            Tex(r"If a collection of vertices forms a hole"),
            Tex(r"in the complement of a graph $G$, then"),
            Tex(r"we say they form an \underline{antihole} in $G$."),
        ).arrange(DOWN, aligned_edge=LEFT)
        self.play(Write(antihole_defn), run_time=3)
        self.wait(3)
        self.play(Unwrite(antihole_defn))
        self.play(FadeIn(graphs[-1], C7))
        self.wait()
        self.play(FadeOut(graphs[-1]), C7.animate.change_layout("circular"))
        self.wait()
        graphs[-1] = C7
        self.play(
            C7.animate.change_layout("circular", layout_scale=scale),
            FadeIn(graphs[:-1]),
        )
        self.play(graphs.animate.arrange_in_grid(buff=LARGE_BUFF))
        self.wait(3)


class PerfectGraphs(Scene):
    def construct(self):
        lt_scale = 1.5
        v_c = {"radius": 0.05}
        graphs = VGroup(
            Graph(
                *perf.lollipop_5(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="kamada_kawai",
            ),
            Graph(
                *perf.barbell_5_5(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="kamada_kawai",
            ),
            Graph(
                *perf.rook_8(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="kamada_kawai",
            ),
            Graph(
                *perf.fan_4_2(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="circular",
            ).rotate(-2 * PI / 3),
            Graph(
                *perf.hanoi_2(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="partite",
                partitions=[[1], [2, 9], [3, 8], [4, 5, 6, 7]],
            ),
            Graph(
                *perf.sun_4(),
                layout_scale=lt_scale,
                vertex_config=v_c,
                layout="kamada_kawai",
            ),
        ).arrange_in_grid(buff=LARGE_BUFF)
        self.play(
            Create(graphs[0]),
            Create(graphs[1]),
            Create(graphs[2]),
            Create(graphs[3]),
            Create(graphs[4]),
            Create(graphs[5]),
        )
        self.wait(10)
