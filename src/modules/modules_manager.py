from typing import Any
from rclpy.node import Node


class ModulesManager:
    __modules = {}
    __node = None

    def __init__(self, node: Node):
        self.__node = node

    def add(self, class_module: Any, *args) -> None:
        self.__node.get_logger().info(f"Loading class module {class_module.__name__}")

        module = class_module(self.__node, *args)
        self.__modules[module.name] = module

        self.__node.get_logger().info(f"Module {module.name} has been loaded")

    def access(self, name: str) -> any:
        if name in self.__modules:
            return self.__modules[name]
        else:
            raise Exception(f"Module {name} not found")
