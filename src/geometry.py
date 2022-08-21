"""
"""
from turtle import color
from unicodedata import name


class FuselageGeom:
    def __init__(
        self,
        # == GEN ==
        name: str,
        colour: tuple,
        material: str,
        Num_U: int,
        Num_W: int,
        # Mass Props
        Density: float = 0.0,
        mass_area: float = 0.0,
        is_shell: bool = False,
        negative_volume: bool = False,
        # == XFORM ==
        absolute_coord_sys: bool = False,
        X_loc:float=0.0,
        X_rot:float=0.0,
        Y_loc:float=0.0,
        Y_rot:float=0.0,
        Z_loc:float=0.0,
        Z_rot:float=0.0,
        origin_rotation:float=0.0
    ) -> None:
        self.name = name
        self.colour = colour
