"""
Type annotations for awscrt.common module.

Copyright 2024 Vlad Emelianov
"""

def get_cpu_group_count() -> int: ...
def get_cpu_count_for_group(group_idx: int) -> int: ...
