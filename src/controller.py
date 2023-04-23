from rclpy.node import Node
from geometry_msgs.msg import Vector3

from modules.modules_manager import ModulesManager
from modules.clients import *
from modules.parameters import *
from modules.publishers import *
from modules.subscribers import *


class TurtleController(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.__modules_manager = ModulesManager(self)

        self.__modules_manager.add(Reset)
        self.__modules_manager.add(SetPen, "turtle1")
        self.__modules_manager.add(Velocity, "turtle1")
        self.__modules_manager.add(Background)

        self.__modules_manager.access("reset").execute()
        self.__modules_manager.access("background").set_rgb(0, 0, 0)
        self.__modules_manager.access("set_pen").set_rgb(255, 255, 255)

        self.timer_ = self.create_timer(0.1, self.test_move)

    def test_move(self):
        linear = Vector3(x=1.0, y=0.0, z=0.0)
        angular = Vector3(x=0.0, y=0.0, z=0.5)
        self.__modules_manager.access("velocity").apply(linear, angular)
