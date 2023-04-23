from base import Publisher
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Velocity(Publisher):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__("move", node, f"{turtle_name}/cmd_vel", Twist, 10)

    def apply(self, linear: float, angular: float) -> None:
        self.publish(Twist(linear=linear, angular=angular))
