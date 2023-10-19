from .configuration import ConfigurationManager


def convert_value(value: any) -> any:
    conversion_functions: list = ConfigurationManager.get_conversion_functions()
    for func in conversion_functions:
        value: any = func(value)
    return value
