from base import Client
from rclpy.node import Node
from std_msgs.msg import Empty as EmptyMsg  # This is a message type
from std_srvs.srv import Empty as EmptySrv  # This is a service type for the client


class Clear(Client):
    def __init__(self, node: Node):
        super().__init__("clear", node, "clear", EmptySrv)
        super().connect()

    def execute(self):
        self.async_call(EmptyMsg())
