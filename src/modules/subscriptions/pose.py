from base import Subscription
from rclpy.node import Node
from turtlesim.msg import Pose as Pose
from typing import Any


class Pose(Subscription):
    def __init__(self, node: Node, turttle_name: str, subscription_callback: Any):
        super().__init__("pose", node, f"/{turttle_name}/pose", Pose)
        super().connect(subscription_callback)
