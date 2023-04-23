from .base import Parameter
from rclpy.node import Node
import rclpy


class Background(Parameter):
    def __init__(self, node: Node):
        super().__init__(node, "background")

    def get_background(self) -> (int, int, int):
        return (
            self.get_value(node, "background_r"),
            self.get_value(node, "background_g"),
            self.get_value(node, "background_b"),
        )

    def set_background(self, r: int, g: int, b: int) -> None:
        self.set_value("background_r", rclpy.Parameter.Type.INTEGER, r)
        self.set_value("background_g", rclpy.Parameter.Type.INTEGER, g)
        self.set_value("background_b", rclpy.Parameter.Type.INTEGER, b)
