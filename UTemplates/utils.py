from .configuration import ConfigurationManager


def convert_value(value: any) -> any:
    """
    Convert a given value using a list of conversion functions.

    The function fetches the conversion functions from the ConfigurationManager and
    iteratively applies each function on the given value. If any of the functions
    transform the value, the transformed value will be the output.

    Args:
        value (any): The value to be converted.

    Returns:
        any: The converted value or the original value if no conversion was applied.

    Example:
        Given the value 123, if one of the conversion functions in the configuration
        changes numbers into strings prefixed with "Num:", the output will be "Num:123".
    """
    conversion_functions: list = ConfigurationManager.get_conversion_functions()
    for func in conversion_functions:
        value: any = func(value)
    return value
