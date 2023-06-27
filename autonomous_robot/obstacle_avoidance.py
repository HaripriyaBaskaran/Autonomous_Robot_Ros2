#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.twist = Twist()
        self.initial_velocity = 0.2  # initial velocity
        self.min_velocity = 0.2  # minimum velocity

    def scan_callback(self, scan):
        # Define a threshold for obstacles
        threshold = 1.0

        # Get the minimum distance from the laser scan data
        min_distance = min(scan.ranges)

        # Calculate velocity based on the distance from obstacles
        if min_distance < threshold:
            velocity = self.min_velocity
        else:
            velocity = self.initial_velocity

        # Turn left if an obstacle is detected
        if min_distance < threshold:
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.5
        else:
            # Move forward with the calculated velocity
            self.twist.linear.x = velocity
            self.twist.angular.z = 0.0

        # Publish the twist command
        self.cmd_vel_pub.publish(self.twist)


def main(args=None):
    rclpy.init(args=args)
    obstacle_avoidance = ObstacleAvoidance()
    rclpy.spin(obstacle_avoidance)
    obstacle_avoidance.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
