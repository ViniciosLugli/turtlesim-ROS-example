from .base import Client
from rclpy.node import Node
from std_srvs.srv._empty import (
    Empty_Request as EmptyMsg,
)  # This is a message type for the service
from std_srvs.srv import Empty as EmptySrv  # This is a service type for the client


class Reset(Client):
    def __init__(self, node: Node):
        super().__init__("reset", node, "reset", EmptySrv)

    def execute(self):
        self.async_call(EmptyMsg())
