from typing import List, Tuple
import graph_generation


def C5_with_central() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = [0,1,2,3,4,5,6]
    edges = [(0,1),(1,2),(3,4),(4,5),(5,0),(0,6),(1,6),(3,6)]
    return vertices, edges

def C5_with_square() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(5)
    vertices += [7,8]
    edges += [(1,7),(7,8),(8,2)]

def moser_spindle() -> Tuple[List[int], List[Tuple[int]]]:
    vertices = [0,1,2,3,4,5,6]
    edges = [(0,1),(0,2),(0,6),(1,2),(1,3),(2,3),(3,4),(3,5),(4,6),(5,6)]
    return vertices, edges

def C7_with_interior_stuff() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(7)
    vertices += [8,9,10,11,12]
    edges += [(8,3),(8,5),(9,1),(9,3),(9,4),(11,4),(12,2),(8,10),(11,9),(9,12),(10,11)]
    return vertices, edges

def C9_with_interior_stuff() -> Tuple[List[int], List[Tuple[int]]]:
    vertices, edges = graph_generation.cycle(9)
    vertices += [10,11,12,13,14,15]
    edges += [(10,1),(10,2),(10,5),(11,4),(12,6),(12,8),(13,2),(13,3),(13,9),(14,3),(15,1),(15,8),(10,11),(11,12),(12,13),(13,14),(14,15),(15,10)
              , (10,13),(11,14)]
    return vertices, edges