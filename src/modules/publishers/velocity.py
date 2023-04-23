from .base import Publisher
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3


class Velocity(Publisher):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__("velocity", node, f"{turtle_name}/cmd_vel", Twist)

    def apply(self, linear: Vector3, angular: Vector3) -> None:
        self.publish(Twist(linear=linear, angular=angular))
