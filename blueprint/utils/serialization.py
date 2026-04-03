"""
Serialization utilities for AngleHelper.

Provides functions for converting between Python objects and JSON-compatible formats.
"""

def convert_tuples_to_lists(obj):
    """Convert tuples to lists for JSON serialization.
    
    Args:
        obj: Object to convert (dict, list, tuple, or other)
        
    Returns:
        Converted object with all tuples replaced by lists
    """
    if isinstance(obj, dict):
        return {k: convert_tuples_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_tuples_to_lists(item) for item in obj]
    else:
        return obj


def convert_lists_to_tuples(obj):
    """Convert lists back to tuples for deserialization.
    
    Args:
        obj: Object to convert (dict, list, or other)
        
    Returns:
        Converted object with point lists replaced by tuples
    """
    if isinstance(obj, dict):
        return {k: convert_lists_to_tuples(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # Check if this list represents a point (length 2 with numbers)
        if len(obj) == 2 and all(isinstance(x, (int, float)) for x in obj):
            return tuple(obj)
        else:
            return [convert_lists_to_tuples(item) for item in obj]
    else:
        return obj