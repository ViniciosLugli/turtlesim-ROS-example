from rclpy.node import Node
from typing import Any


class Client:
    def __init__(self, name: str, node: Node, srv_name: str, srv_type: Any):
        # Setup instance variables
        self.name = name
        self.node = node
        self.srv_type = srv_type
        self.srv_name = srv_name
        self.client = None

        self.node.get_logger().info(f"Client {self.name} created.")

    def connect(self) -> None:
        self.client = self.node.create_client(
            self.srv_type, self.srv_name, 10
        )  # Create the client for the service

        # Wait for the service to be available before continuing ( client connect to the service )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info(
                f"Client {self.name} waiting for service {self.srv_name}."
            )

        self.node.get_logger().info(
            f"Client {self.name} connected to service {self.srv_name}."
        )

    def disconnect(self) -> None:
        self.node.destroy_client(self.client)
        self.node.get_logger().info(f"Client {self.name} disconnected.")

    def callback(self, future: Any) -> None:
        try:  # Try to get the response from the future
            response = future.result()
            self.node.get_logger().info(
                f"Client {self.name} received response: {response}"
            )
        except Exception as e:  # If the future fails, log the error
            self.node.get_logger().error(
                f"Client {self.name} failed to receive response: {e}"
            )

    def async_call(self, request: Any, custom_callback: Any = None) -> None:
        self.node.get_logger().info(f"Client {self.name} sending request: {request}")
        future = self.client.call_async(request)  # Call the service asynchronously
        future.add_done_callback(
            custom_callback if custom_callback else self.callback
        )  # Add a callback to the future to handle the response

    def call(self, request: Any) -> Any:
        self.node.get_logger().info(f"Client {self.name} sending request: {request}")
        return self.client.call(request)  # Call the service synchronously
