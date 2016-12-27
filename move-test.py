#!/usr/bin/env python3

# Copyright (c) 2016 Mastersoft
# Using examples from the Cozmo SDK by Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Drive And Turn

Make Cozmo drive forwards and then turn 90 degrees to the left.
'''

import cozmo
from time import sleep

from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.lights import Light, green_light, blue_light, red_light



def cozmo_program(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    action = robot.drive_straight(distance_mm(300),speed_mmps(1000), in_parallel= True)
    while not robot.is_moving:
        sleep(0.1)
    while robot.is_moving:
        robot.set_all_backpack_lights(green_light)
        sleep(0.2)
        robot.set_all_backpack_lights(blue_light)
        sleep(0.2)
        robot.set_all_backpack_lights(red_light)
        sleep(0.2)
  #  robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    #robot.turn_in_place(degrees(90)).wait_for_completed()


cozmo.run_program(cozmo_program)
