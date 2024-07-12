from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
import os
from ament_index_python.packages import get_package_share_path
from launch.substitutions import Command


def generate_launch_description():
    urdf_path = os.path.join(get_package_share_path('robot_description'),
                             urdf_path,'Robot.urdf')
    
    robot_description = ParameterValue()
    return LaunchDescription([])