#!/usr/bin/env python3
"""Module that takes a list as argument and returns a list of integers"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list as argument and returns a list of integers"""
    return [(i, len(i)) for i in lst]
