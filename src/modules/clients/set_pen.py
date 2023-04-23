from base import Client
from rclpy.node import Node
from turtlesim.srv import SetPen as SetPenSrv
from turtlesim.msg import Color


class SetPen(Client):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__("set_pen", node, f"{turtle_name}/set_pen", SetPenSrv)
        super().connect()

    def rgb(
        self,
        r: int,
        g: int,
        b: int,
    ) -> None:
        self._client.call_async(Color(r=r, g=g, b=b))
