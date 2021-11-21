import rclpy

from cv_bridge import CvBridge
from cv_bridge.core import CvBridgeError
from rclpy.node import Node
from sensor_msgs.msg import Image


class VisionSubscriber(Node):
    def __init__(self):
        super().__init__('vision subscriber')
        self.subscription = self.create_subscription(
            Image,
            'topic',
            self.image_callback,
            10
        )
        self.subscription

    def image_callback(self, ros_image):
        self.get_logger().debug("Image received on subscribed topic")
        bridge = CvBridge()
        try:
            cv_image = bridge.imgmsg_to_cv2(ros_image, "mono8")
        except CvBridgeError as e:
            print(e)

        print(cv_image)

def main(args=None):
    rclpy.init(args=args)
    vision_subscriber = VisionSubscriber()
    rclpy.spin(vision_subscriber)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
