from typing import List, Tuple


def complete(n: int) -> Tuple[List[int], List[Tuple[int]]]:
    vertices = list(range(1, n + 1))
    edges = [(u, v) for u in vertices for v in vertices[u:]]
    return vertices, edges


def path(n: int) -> Tuple[List[int], List[Tuple[int]]]:
    vertices = list(range(1, n + 1))
    edges = [(u, u + 1) for u in vertices]
    return vertices, edges


def cycle(n: int) -> Tuple[List[int], List[Tuple[int]]]:
    if n < 3:
        raise ValueError(
            f"Cannot construct a cycle with fewer than 3 vertices ({n} < 3)."
        )
    vertices, edges = path(n)
    edges.append((n, 1))
    return vertices, edges


def complete_multipartite(sizes: List[int]) -> Tuple[List[int], List[Tuple[int]]]:
    if len(sizes) < 2:
        raise ValueError(f"A complete multipartite graph must have at least two parts.")
    if len(sizes) == 2:
        X = list(range(1, sizes[0] + 1))
        Y = list(range(sizes[0] + 1, sum(sizes) + 1))
        vertices = X + Y
        edges = [(x, y) for x in X for y in Y]
        return vertices, edges
    else:
        rest_v, rest_e = complete_multipartite(sizes[:-1])
        Z = list(range(sum(sizes[:-1]), sum(sizes) + 1))
        vertices = rest_v + Z
        edges = rest_e + [(x, z) for x in rest_v for z in Z]
        return vertices, edges