from flask import Blueprint

from controllers import (AuthController as ac)

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'], strict_slashes=False)(ac.login)
auth_bp.route('/signup', methods=['POST'], strict_slashes=False)(ac.signup)
auth_bp.route(
    '/renew_token',
    methods=['GET'],
    strict_slashes=False
)(ac.renew_token)
