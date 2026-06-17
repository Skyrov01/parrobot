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

from .interactions_routes import interactions_bp
from .servo_routes import servo_bp
from .context import set_ros_node



def register_routes(app, node):
    
    app.register_blueprint(interactions_bp)
    app.register_blueprint(servo_bp)
    app.logger.info("[Routes] Registered all routes with Flask app")
