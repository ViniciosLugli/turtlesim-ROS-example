from .base import Client
from rclpy.node import Node
from turtlesim.srv import SetPen as SetPenSrv
from turtlesim.srv._set_pen import SetPen_Request


class SetPen(Client):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__("set_pen", node, f"{turtle_name}/set_pen", SetPenSrv)
        super().connect()

    def set_rgb(
        self,
        r: int,
        g: int,
        b: int,
        width: int = 2,
        off: bool = False,
    ) -> None:
        self.client.call_async(SetPen_Request(r=r, g=g, b=b))
