#!/usr/bin/env python3
"""Basic annotations - safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a list lst of integers and floats elements and
    returns their sum as a float"""
    if lst:
        return lst[0]
    else:
        return None
