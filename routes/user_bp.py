from flask import Blueprint

from controllers import (UserController as uc)

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'], strict_slashes=False)(uc.get_users)
user_bp.route('/<int:user_id>', methods=['GET'])(uc.get_user)
user_bp.route('/<int:user_id>', methods=['PUT'])(uc.update_user)
user_bp.route('/<int:user_id>', methods=['DELETE'])(uc.delete_user)
