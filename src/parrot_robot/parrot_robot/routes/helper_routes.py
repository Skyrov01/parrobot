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

from flask import Blueprint, request, jsonify
from .context import ros_node  




helper_bp = Blueprint("helper", __name__)

ros_node = None  


# Test route to confirm the server is running
@helper_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok", "message": "Parrot HTTP Bridge is alive!"})