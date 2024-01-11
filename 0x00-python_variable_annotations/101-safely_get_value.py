#!/usr/bin/env python3
"""Basic annotations - safe_first_element"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'),
                                    None]) -> Union[Any, TypeVar('T')]:
    if key in dct:
        return dct[key]
    else:
        return default