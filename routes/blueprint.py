from flask import Blueprint
from controllers.controllers import *

blueprint = Blueprint('blueprint', __name__)


blueprint.route('/course', methods=['GET'])(get_course_main)
blueprint.route('/module_desc', methods=['GET'])(get_module_desc_main)
blueprint.route('/module_version', methods=['GET'])(get_module_version_main)
blueprint.route('/pm_version', methods=['GET'])(get_pm_version_main)
blueprint.route('/program_map', methods=['GET'])(get_program_map_main)
