import random

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class SpawnTargetNode(Node):
    def __init__(self):
        super().__init__('spawn_target_node')

        # Create the client for the /spawn service
        self.client = self.create_client(Spawn, '/spawn')

        # Wait until the service is available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')

        # Create random coordinates in [1, 10]
        x = random.uniform(1.0, 10.0)
        y = random.uniform(1.0, 10.0)

        # Optional: random angle between 0 and 2*pi
        theta = random.uniform(0.0, 6.28)

        # Create the request
        self.request = Spawn.Request()
        self.request.x = x
        self.request.y = y
        self.request.theta = theta
        self.request.name = 'turtle_target'

        # Save coordinates so we can print them later
        self.target_x = x
        self.target_y = y

        # Call the service asynchronously
        self.future = self.client.call_async(self.request)
        self.future.add_done_callback(self.spawn_callback)

    def spawn_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(
                f"Turtle '{response.name}' spawned at x={self.target_x:.2f}, y={self.target_y:.2f}"
            )
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = SpawnTargetNode()
    rclpy.spin_until_future_complete(node, node.future)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
