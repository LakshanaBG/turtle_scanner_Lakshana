import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleScannerNode(Node):
    def __init__(self):
        super().__init__('turtle_scanner_node')

        self.pose_scanner = None
        self.pose_target = None

        self.sub_scanner = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.scanner_pose_callback,
            10
        )

        self.sub_target = self.create_subscription(
            Pose,
            '/turtle_target/pose',
            self.target_pose_callback,
            10
        )

        self.get_logger().info('turtle_scanner_node started')

    def scanner_pose_callback(self, msg):
        self.pose_scanner = msg

    def target_pose_callback(self, msg):
        self.pose_target = msg


def main(args=None):
    rclpy.init(args=args)
    node = TurtleScannerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
