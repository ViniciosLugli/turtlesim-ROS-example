from ..clients import Client
from rclpy.node import Node
import rclpy
from typing import Any
from rcl_interfaces.msg import ParameterType, ParameterValue
from rcl_interfaces.msg import Parameter as ParameterMsg
from rcl_interfaces.srv._set_parameters import SetParameters


class Parameter(Client):
    def __init__(self, node: Node, name: str, srv_name: str):
        self.node = node
        self.name = name

        self.req = SetParameters.Request()

        super().__init__(name, node, f"{srv_name}/set_parameters", SetParameters)

    def get_value(self, name: str):
        return NotImplementedError("get_value() method is not implemented yet.")

    def set_value(self, param_name, param_value):
        if isinstance(param_value, float):
            val = ParameterValue(
                double_value=param_value, type=ParameterType.PARAMETER_DOUBLE
            )
        elif isinstance(param_value, int):
            val = ParameterValue(
                integer_value=param_value, type=ParameterType.PARAMETER_INTEGER
            )
        elif isinstance(param_value, str):
            val = ParameterValue(
                string_value=param_value, type=ParameterType.PARAMETER_STRING
            )
        elif isinstance(param_value, bool):
            val = ParameterValue(
                bool_value=param_value, type=ParameterType.PARAMETER_BOOL
            )

        self.req.parameters = [ParameterMsg(name=param_name, value=val)]
        self.async_call(self.req)
