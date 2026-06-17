# Copyright 2025 Vlad Isuf
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gpiozero import AngularServo
from time import sleep

# Configure the servo on GPIO 18
# Adjust min/max pulse width if motion is limited or jittery
servo = AngularServo(
    18,                  # GPIO pin
    min_angle=0,
    max_angle=180,
    min_pulse_width=0.0005,  # 0.5ms
    max_pulse_width=0.0025   # 2.5ms
)

try:
    for angle in [0, 90, 180, 90]:
        print(f"Setting angle to {angle}°")
        servo.angle = angle
        sleep(1)
finally:
    print("Detaching servo")
    servo.detach()
