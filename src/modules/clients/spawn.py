from base import Client
from rclpy.node import Node
from turtlesim.srv import Spawn as SpawnSrv
from turtlesim.srv._spawn import Spawn_Request, Spawn_Response


class Spawn(Client):
    def __init__(self, node: Node):
        super().__init__("spawn", node, "spawn", SpawnSrv)
        super().connect()

    def new(self, x: float, y: float, theta: float, name: str) -> Spawn_Response:
        return self.call(Spawn_Request(x=x, y=y, theta=theta, name=name))
