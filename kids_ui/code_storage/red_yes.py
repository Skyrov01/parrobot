#Start code here
import time
BASE_URL = f"http://192.168.8.130:5000"
def run_motor(motor, position, method, speed):
  import requests
  global BASE_URL
  r = requests.post(f"{BASE_URL}/servo/{motor}/position/{position}/method/{method}/speed/{speed}")
  if r.status_code == 200:
    print(f"All good: {r.status_code}")
  else:
    print(f"Something is bad: {r.status_code}")
def play_sound(name):
  import requests
  global BASE_URL
  r = requests.post(f"{BASE_URL}/sound/play/{name}")
  print(r.status_code)
  if r.status_code == 200:
    print(f"All good{r.status_code}")
  else:
    print(f"Something is bad{r.status_code}")
# This is just an example. Keep it here until you make # your own code
run_motor("head_rotate", 90.0, "instant", 1.0)
time.sleep(1)
play_sound("red_yes_02")
time.sleep(1)
# From down here # your own code
for i in range(10):
  run_motor("head_tilt", 135.0, "instant", 1.0)
  time.sleep(1)
  run_motor("head_tilt", 90.0, "instant", 1.0)
  time.sleep(1)
