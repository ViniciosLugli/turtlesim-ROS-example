from .base import Parameter
from rclpy.node import Node
import rclpy


class Background(Parameter):
    def __init__(self, node: Node):
        super().__init__(node, "background", "turtlesim")

    def get_rgb(self) -> (int, int, int):
        return (
            self.get_value("background_r"),
            self.get_value("background_g"),
            self.get_value("background_b"),
        )

    def set_rgb(self, r: int, g: int, b: int) -> None:
        self.set_value("background_r", r)
        self.set_value("background_g", g)
        self.set_value("background_b", b)
