#!/usr/bin/python3 -B

import time
import asyncio
import math
import moteus

max_pos = 1.0
min_pos = -1.0

class Servo:
    def __init__(self, id):
        self.id = id
        self.controller = moteus.Controller(id=id)

    async def stop(self):
        await self.controller.set_stop()

    async def move_to_pos(self, target_pos, cycle):
        while cycle > 0:
            cycle -= 1
            state = await self.controller.set_position(
                    position=math.nan,
                    velocity=2.0,
                    maximum_torque=10.0,
                    stop_position=target_pos,
                    query=True)

            # Print out just the position register.
#            print("Position:", state.values[moteus.Register.POSITION])
#            print("Velocity:", state.values[moteus.Register.VELOCITY])
#            print("Torque  :", state.values[moteus.Register.TORQUE])
#            print()
            await asyncio.sleep(0.02)

        print("Position:", state.values[moteus.Register.POSITION])

async def hello():
    print("Helle world1111111111111111")
    await asyncio.sleep(1)
    print("Helle world2222222222222222")

async def main():
    print("Starting test...")
    servo_test1 = Servo(8)

    while True:
        await servo_test1.stop()
        await servo_test1.move_to_pos(0.3, 25)
        await servo_test1.stop()
        await servo_test1.move_to_pos(-0.3, 25)

if __name__ == '__main__':
    asyncio.run(main())
