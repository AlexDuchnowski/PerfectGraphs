from typing import List, Tuple
import graph_generation


def lollipop_5() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.complete(5)
    vertices += [6,7,8,9]
    edges += [(6,1),(7,6),(8,7),(9,8)]
    return vertices, edges

def barbell_5_5() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = [0,1,2,3,4,5,6,7,8,9]
    edges = []
    for i in range(5):
        for j in range(i,5):
            edges += [(i,j), (i+5,j+5)]
    edges += [(0,5)]
    return vertices, edges

def rook_8() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = list(range(64))
    edges = []
    for i in range(64):
        for j in range(i,64):
            if i%8 == j%8 or i//8 == j//8:
                edges += [(i,j)]
    return vertices, edges

def fan_4_2() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = range(6)
    edges = []
    for i in range(1,6):
        edges += [(0,i)]
    for i in range(2,6):
        edges += [(1,i)]
    return vertices, edges

def hanoi_2() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(9)
    edges += [(2,9),(3,5),(6,8)]
    return vertices, edges

def sun_4() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.complete(4)
    vertices += [5,6,7,8]
    edges += [(1,5),(2,5),(2,6),(3,6),(3,7),(4,7),(4,8),(1,8)]