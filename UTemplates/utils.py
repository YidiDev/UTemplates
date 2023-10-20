from .configuration import ConfigurationManager


def convert_value(value: any, conversion_functions_list: list = None) -> any:
    """
    Convert a given value using a list of conversion functions.

    This function applies each conversion function to the given value iteratively. If any
    of the conversion functions transform the value, the transformed value will be used for
    subsequent functions and will be the final output.

    If a custom list of conversion functions is not provided, the function fetches the default
    conversion functions from the ConfigurationManager.

    Args:
        value (any): The value to be converted.
        conversion_functions_list (list, optional): An optional list of custom conversion
                                                   functions. Defaults to None, in which case
                                                   the default conversion functions from the
                                                   ConfigurationManager will be used.

    Returns:
        any: The converted value or the original value if no conversion was applied.

    Example:
        Given the value 123, if one of the conversion functions in the configuration (or in
        the provided custom list) changes numbers into strings prefixed with "Num:",
        the output will be "Num:123".

    Note:
        If using a custom conversion function list, ensure that the functions are properly
        ordered as they will be applied in the order they appear in the list.
    """
    conversion_functions: list = ConfigurationManager.get_conversion_functions() \
        if conversion_functions_list is None else conversion_functions_list
    for func in conversion_functions:
        value: any = func(value)
    return value
