from base import Client
from rclpy.node import Node
from turtlesim.srv import Kill as KillSrv
from turtlesim.srv._kill import Kill_Request, Kill_Response


class Kill(Client):
    def __init__(self, node: Node):
        super().__init__("kill", node, "kill", KillSrv)
        super().connect()

    def murder(self, name: str) -> None:
        self.async_call(Kill_Request(name=name))
