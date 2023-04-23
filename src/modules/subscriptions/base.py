from rclpy.node import Node
from typing import Any


class Subscription:
    def __init__(self, name: str, node: Node, topic_name: str, topic_type: Any):
        # Setup instance variables
        self.name = name
        self.node = node
        self.topic_type = topic_type
        self.topic_name = topic_name
        self.subscription = None

        self.node.get_logger().info(f"Subscription {self.name} created.")

    def connect(self, subscription_callback: Any) -> None:
        self.subscription = self.node.create_subscription(
            self.topic_type, self.topic_name, subscription_callback, 10
        )  # Create the subscription to the topic with the callback

        self.node.get_logger().info(f"Subscription {self.name} connected.")

    def disconnect(self) -> None:
        self.subscription.destroy()
        self.node.get_logger().info(f"Subscription {self.name} disconnected.")
