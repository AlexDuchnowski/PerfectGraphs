from typing import List, Tuple

import graph_generation


def lollipop_5() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.complete(5)
    vertices += [6, 7, 8, 9]
    edges += [(6, 1), (7, 6), (8, 7), (9, 8)]
    return vertices, edges


def barbell_5_5() -> Tuple[List[int], List[Tuple[int]]]:
    v1, e1 = graph_generation.complete(5)
    v2, e2 = graph_generation.shift(*graph_generation.complete(5), 5)
    return v1 + v2, e1 + e2 + [(1, 6)]


def rook_8() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = list(range(9))
    edges = []
    for i in range(9):
        for j in range(i + 1, 9):
            if i % 3 == j % 3 or i // 3 == j // 3:
                edges += [(i, j)]
    return graph_generation.shift(vertices, edges, 1)


def fan_4_2() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = range(6)
    edges = []
    for i in range(1, 6):
        edges += [(0, i)]
    for i in range(2, 6):
        edges += [(1, i)]
    return graph_generation.shift(vertices, edges, 1)


def hanoi_2() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(9)
    edges += [(2, 9), (3, 5), (6, 8)]
    return vertices, edges


def sun_4() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.complete(4)
    vertices += [5, 6, 7, 8]
    edges += [(1, 5), (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (4, 8), (1, 8)]
    return vertices, edges


def king_3_3() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = list(range(9)), []
    for i in range(9):
        for j in range(i + 1, 9):
            if ((i % 3) - (j % 3)) ** 2 <= 1 and ((i // 3) - (j // 3)) ** 2 <= 1:
                edges += [(i, j)]
    return graph_generation.shift(vertices, edges, 1)


def windmill_4_5() -> Tuple[List[int], List[Tuple[int]]]:
    blades = [
        graph_generation.shift(*graph_generation.complete(3), 3 * i) for i in range(5)
    ]
    vertices = [v for blade in blades for v in blade[0]] + [16]
    edges = [e for blade in blades for e in blade[1]] + [(v, 16) for v in vertices[:-1]]
    return vertices, edges
