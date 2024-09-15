import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():
    pkg_path = os.path.dirname(__file__)
    xacro_file = os.path.join(pkg_path, 'ego_racecar.xacro')
    
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='ego_robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', xacro_file])
            }],
            remappings=[('/robot_description', 'ego_robot_description')]
        ),
        Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_baselink_to_laser',
        arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'senton/front_right_hinge', 'senton/front_right_wheel']
        ),
        Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_baselink_to_laser',
        arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'senton/front_left_hinge', 'senton/front_left_wheel']
        ),
        
    ])
