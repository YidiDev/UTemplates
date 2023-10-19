import os
import json
import importlib
from types import ModuleType


DEFAULT_CONFIG_PATH: str = "u_templating_config.json"
ENV_CONFIG_PATH: str = "U_TEMPLATING_CONFIG_PATH"


class ConfigurationManager:
    _conversion_functions: list = None

    @classmethod
    def _load_config(cls) -> None:
        config_path: str = os.environ.get(ENV_CONFIG_PATH, DEFAULT_CONFIG_PATH)
        if not os.path.exists(config_path):
            raise ValueError(f"Config file not found at {config_path}")

        with open(config_path, 'r') as f:
            config: dict[str, any] = json.load(f)

        conversion_functions: list = []
        for function_path in config["conversions"]:
            parts: list[str] = function_path.split('.')
            module_path: str = '.'.join(parts[:-1])
            function_name: str = parts[-1]

            module: ModuleType = importlib.import_module(module_path)
            function = getattr(module, function_name)
            conversion_functions.append(function)

        cls._conversion_functions: list = conversion_functions

    @classmethod
    def get_conversion_functions(cls) -> list:
        if cls._conversion_functions is None:
            cls._load_config()
        return cls._conversion_functions
