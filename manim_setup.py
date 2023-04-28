import numpy as np
from manim import *

FONT = "Times New Roman"

config.background_color = DARKER_GRAY

COLOR_SEQ = [
    PURE_BLUE,
    PURE_GREEN,
    ORANGE,
    PINK,
    TEAL,
    PURPLE_A,
    YELLOW,
    BLUE,
    MAROON_E,
    DARK_BROWN,
]

t2c = {
    "\chi": BLUE,
    "\omega": RED,
    "G": GREEN,
    "\geq": GOLD,
    "=": YELLOW,
    r"\neq": PURE_RED,
}
kw = dict(font_size=80, tex_to_color_map=t2c)
