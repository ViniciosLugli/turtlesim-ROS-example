from typing import Any


class ModulesManager:
    __modules = {}

    def add(self, module: Any) -> None:
        self.__modules[module.name] = module

    def access(self, name: str) -> any:
        return self.__modules[name]
