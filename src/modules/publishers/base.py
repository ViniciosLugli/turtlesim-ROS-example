from rclpy.node import Node


class Publisher:
    def __init__(self, name: str, node: Node, topic_name: str, topic_type: any):
        # Setup instance variables
        self.name = name
        self.node = node
        self.topic_type = topic_type
        self.topic_name = topic_name
        self.publisher = None

        self.connect()

        self.node.get_logger().info(f"Publisher {self.name} created.")

    def connect(self) -> None:
        self.publisher = self.node.create_publisher(
            self.topic_type, self.topic_name, 10
        )  # Create the publisher to the topic

        self.node.get_logger().info(f"Publisher {self.name} connected.")

    def disconnect(self) -> None:
        self.publisher.destroy()
        self.node.get_logger().info(f"Publisher {self.name} disconnected.")

    def publish(self, message: any) -> None:
        self.publisher.publish(message)
