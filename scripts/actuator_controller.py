#!/usr/bin/python3 -B

import time
import math
from aoyun_fdcanusb.moteusController import Controller
from aoyun_fdcanusb.moteusReg import MoteusReg
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState 
import threading

def thread_job():
    rospy.spin()

positions = [0 for _ in range(12)]
def save_position(data):
    global positions
    for i in range(12):
        positions[i] = (data.position[i] / math.pi)
#        rospy.loginfo('positions[%d]: %f; data.position[%d] %f', i, positions[i], i, data.position[i])

def listener():
    rospy.init_node('ayspot_a1_hw_pylistener', anonymous=True)
    add_thread = threading.Thread(target = thread_job)
    add_thread.start()
    rospy.Subscriber('/joint_states', JointState, save_position, queue_size=1)
    rospy.sleep(1)

def main():
    global positions
#    controller_hip_lf   = Controller(controller_ID = 3)
#    controller_thigh_lf = Controller(controller_ID = 1)
#    controller_shank_lf = Controller(controller_ID = 2)
#    controller_hip_rf   = Controller(controller_ID = 6)
    controller_thigh_rf = Controller(controller_ID = 4)
    controller_shank_rf = Controller(controller_ID = 5)
#    controller_hip_lh   = Controller(controller_ID = 9)
#    controller_thigh_lh = Controller(controller_ID = 7)
#    controller_shank_lh = Controller(controller_ID = 8)
#    controller_hip_rh   = Controller(controller_ID = 12)
#    controller_thigh_rh = Controller(controller_ID = 10)
#    controller_shank_rh = Controller(controller_ID = 11)

    listener()

    jump_torque = 2
    freq = 200
    while True:
#        hip_lf   = positions[0]
#        thigh_lf = positions[1]
#        shank_lf = positions[2]
#        hip_rf   = positions[3]
        thigh_rf = positions[4] - (0.25214188/2.0)
        shank_rf = positions[5]
#        hip_lh   = positions[6]
#        thigh_lh = positions[7]
#        shank_lh = positions[8]
#        hip_rh   = positions[9]
#        thigh_rh = positions[10]
#        shank_rh = positions[11]

        freq_measure_time = time.time()
        phase = (time.time()*1) % (2. *math.pi)

#        controller_hip_lf.set_position(position=hip_lf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_thigh_lf.set_position(position=thigh_lf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_shank_lf.set_position(position=shank_lf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)

#        controller_hip_rf.set_position(position=hip_rf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
        controller_thigh_rf.set_position(position=thigh_rf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
        controller_shank_rf.set_position(position=shank_rf, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_hip_lh.set_position(position=hip_lh, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_thigh_lh.set_position(position=thigh_lh, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_shank_lh.set_position(position=shank_lh, max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_hip_rh.set_position(position=positions[9], max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_thigh_rh.set_position(position=positions[10], max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)
#        controller_shank_rh.set_position(position=positions[11], max_torque=jump_torque, kd_scale=5, get_data=True, print_data=False)

        sleep = (1/(freq)) - (time.time() - freq_measure_time)
        if (sleep < 0): sleep = 0
        time.sleep(sleep)

if __name__=='__main__':
    main()
