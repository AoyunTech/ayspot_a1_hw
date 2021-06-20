#!/usr/bin/python3 -B

import time
import math

from aoyun_fdcanusb.moteusController import Controller
from aoyun_fdcanusb.moteusReg import MoteusReg

import rospy
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState 
import threading

def thread_job():
    rospy.spin()

positions = [0 for _ in range(12)]
def save_position(data):
    global positions
    positions[0] = data.position[0]
    positions[1] = data.position[1]
    positions[2] = data.position[2]

def listener():
    rospy.init_node('ayspot_a1_hw_pylistener', anonymous=True)
    add_thread = threading.Thread(target = thread_job)
    add_thread.start()
    rospy.Subscriber('/joint_states', JointState, save_position, queue_size=1)
    rospy.sleep(1)

def main():
    global positions
    controller_knee = Controller(controller_ID = 1)
    controller_hip = Controller(controller_ID = 2)
    controller_abad = Controller(controller_ID = 3)
    jump_torque = 2
    freq = 200

    listener()

    while True:
        knee = positions[0]
        hip = positions[1]
        abad = positions[2]

        freq_measure_time = time.time()
        phase = (time.time()*1) % (2. *math.pi)

        controller_knee.set_position(position=knee, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
        controller_hip.set_position(position=hip, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
        controller_abad.set_position(position=abad, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)

        sleep = (1/(freq)) - (time.time() - freq_measure_time)
        if (sleep < 0): sleep = 0
        time.sleep(sleep)

if __name__=='__main__':
    main()
