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

from flask import Flask, request, Response, jsonify, Blueprint
from .context import ros_node  
interactions_bp = Blueprint("interactions", __name__)


@interactions_bp.route('/nod/<speed>/<int:count>', methods=['POST'])
def nod_route(speed, count):
    
    # Here you could publish a NodCommand
    return jsonify({
        "status": "nod triggered",
        "speed": speed,
        "count": count
    })

