from typing import List, Tuple

import graph_generation


def C5_with_square() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(5)
    vertices += [6, 7]
    edges += [(1, 6), (6, 7), (7, 2)]
    return vertices, edges


def moser_spindle() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 1),
        (1, 6),
        (5, 6),
        (4, 6),
        (2, 7),
        (3, 7),
        (4, 7),
    ]
    return vertices, edges


def C7_with_interior_stuff() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(7)
    vertices += [8, 9]
    edges += [
        (8, 3),
        (8, 5),
        (9, 1),
        (9, 3),
        (9, 4),
    ]
    return vertices, edges


def C9_with_interior_stuff() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(9)
    vertices += [10, 11, 12]
    edges += [(10, 1), (10, 2), (10, 5), (11, 4), (12, 6), (12, 8), (10, 12), (11, 12)]
    return vertices, edges


def C7_complement() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.complete(7)
    for e in graph_generation.cycle(7)[1][:-1] + [(1, 7)]:
        edges.remove(e)
    return vertices, edges
