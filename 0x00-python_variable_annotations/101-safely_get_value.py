#!/usr/bin/env python3
"""Basic annotations - safe_first_element"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
Return = Union[Any, T]
Deflt = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Deflt = None) -> Return:
    """Given the parameters and the return values,
    add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
