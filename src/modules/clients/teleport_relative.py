from base import Client
from rclpy.node import Node
from turtlesim.srv import TeleportRelative as TeleportRelativeSrv
from turtlesim.srv._teleport_relative import TeleportRelative_Request


class TeleportRelative(Client):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__(
            "teleport_relative",
            node,
            f"{turtle_name}/teleport_relative",
            TeleportRelativeSrv,
        )
        super().connect()

    def teleport(
        self,
        linear: float,
        angular: float,
    ) -> None:
        self.async_call(TeleportRelative_Request(linear, angular))
