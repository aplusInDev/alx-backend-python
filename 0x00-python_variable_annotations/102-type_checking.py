#!/usr/bin/env python3
""" Module that takes a list and returns a list  """
from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    """Function that takes a list lst of integers and floats elements and
    returns their sum as a float"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
