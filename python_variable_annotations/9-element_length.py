#!/usr/bin/env python3
""" Basic annotations - element length """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples containing the length of each element """
    return [(i, len(i)) for i in lst]
