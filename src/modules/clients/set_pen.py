from .base import Client
from rclpy.node import Node
from turtlesim.srv import SetPen as SetPenSrv


class SetPen(Client):
    def __init__(self, node: Node, turtle_name: str):
        super().__init__("set_pen", node, f"{turtle_name}/set_pen", SetPenSrv)

    def set_rgb(
        self,
        r: int,
        g: int,
        b: int,
    ) -> None:
        self.client.call_async(SetPenSrv.Request(r=r, g=g, b=b, width=3, off=False))

    def disable(self):
        self.client.call_async(SetPenSrv.Request(off=True, width=3))

    def enable(self):
        self.client.call_async(SetPenSrv.Request(off=False, width=3))
