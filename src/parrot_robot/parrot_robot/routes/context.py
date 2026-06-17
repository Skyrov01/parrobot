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

ros_node = None

def set_ros_node(node):
    global ros_node
    ros_node = node
    print(f"[CONTEXT] ros_node set to: {ros_node}")

def get_ros_node():
    global ros_node
    if ros_node is None:
        print("[CONTEXT] Warning: ros_node is not set")
    else:
        print(f"[CONTEXT] Returning ros_node: {ros_node}")      
    return ros_node
