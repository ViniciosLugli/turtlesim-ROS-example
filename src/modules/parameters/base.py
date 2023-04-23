from rclpy.node import Node
import rclpy
from typing import Any


class Parameter:
    @staticmethod
    def __get_value(node: Node, name: str):
        return node.get_parameter(name).get_parameter_value()

    @staticmethod
    def __set_value(
        node: Node, name: str, type: rclpy.Parameter.Type, value: Any
    ) -> None:
        new_param_value = rclpy.parameter.Parameter(
            name,
            type,
            value,
        )

        node.set_parameters([new_param_value])
