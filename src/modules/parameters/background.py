from base import Parameter
from rclpy.node import Node
import rclpy


class Background(Parameter):
    @staticmethod
    def get_background(node: Node) -> (int, int, int):
        return (
            Background.__get_value(node, "background_r"),
            Background.__get_value(node, "background_g"),
            Background.__get_value(node, "background_b"),
        )

    @staticmethod
    def set_background(node: Node, r: int, g: int, b: int) -> None:
        Background.__set_value(node, "background_r", rclpy.Parameter.Type.INTEGER, r)
        Background.__set_value(node, "background_g", rclpy.Parameter.Type.INTEGER, g)
        Background.__set_value(node, "background_b", rclpy.Parameter.Type.INTEGER, b)
