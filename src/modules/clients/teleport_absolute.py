from base import Client
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute as TeleportAbsoluteSrv
from turtlesim.srv._teleport_absolute import TeleportAbsolute_Request


class TeleportAbsolute(Client):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__(
            "teleport_absolute",
            node,
            f"{turtle_name}/teleport_absolute",
            TeleportAbsoluteSrv,
        )
        super().connect()

    def teleport(
        self,
        x: float,
        y: float,
        theta: float,
    ) -> None:
        self.async_call(TeleportAbsolute_Request(x, y, theta))
