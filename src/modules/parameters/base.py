from rclpy.node import Node
import rclpy
from typing import Any


class Parameter:
    def __init__(self, node: Node, name: str):
        self.node = node
        self.name = name

        self.node.get_logger().info(f"Paremeter {self.name} created.")

    def get_value(self, name: str):
        return self.node.get_parameter(name).get_parameter_value()

    def set_value(self, name: str, type: rclpy.Parameter.Type, value: Any) -> None:
        new_param_value = rclpy.parameter.Parameter(
            name,
            type,
            value,
        )

        self.node.set_parameters([new_param_value])
