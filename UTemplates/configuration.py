import os
import json
import importlib
from types import ModuleType


DEFAULT_CONFIG_PATH: str = "utemplates_config.json"
ENV_CONFIG_PATH: str = "UTEMPLATES_CONFIG_PATH"


class ConfigurationManager:
    """A manager class to handle the loading and storage of conversion functions from a configuration file."""
    _conversion_functions: list = None

    @classmethod
    def _load_config(cls) -> None:
        """
        A private method to load conversion functions from the configuration file.
        The configuration file's path is first searched in the environment variable `ENV_CONFIG_PATH`.
        If not found, it falls back to the `DEFAULT_CONFIG_PATH`.
        """
        config_path: str = os.environ.get(ENV_CONFIG_PATH, DEFAULT_CONFIG_PATH)
        if not os.path.exists(config_path):
            print("UTemplates is starting without a config file")
            if config_path == DEFAULT_CONFIG_PATH:
                cls._conversion_functions: list = []
            else:
                raise ValueError(f"Config file not found at {config_path}")
        print(f"UTemplates is starting with the following config path: {config_path}")

        with open(config_path, 'r') as f:
            config: dict[str, any] = json.load(f)

        conversion_functions: list = []
        for function_path in config.get("conversions", []):
            parts: list[str] = function_path.split('.')
            module_path: str = '.'.join(parts[:-1])
            function_name: str = parts[-1]

            module: ModuleType = importlib.import_module(module_path)
            function = getattr(module, function_name)
            conversion_functions.append(function)

        cls._conversion_functions: list = conversion_functions
        print(f"UTemplates is running with the following list of conversion functions: ")
        print([func.__name__ for func in cls._conversion_functions])

    @classmethod
    def get_conversion_functions(cls) -> list:
        """
        Public method to fetch the loaded conversion functions.
        If the functions haven't been loaded yet, it triggers the loading process.
        Returns:
            list: A list of loaded conversion functions.
        """
        if cls._conversion_functions is None:
            cls._load_config()
        return cls._conversion_functions
