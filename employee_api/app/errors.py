
from flask import jsonify, request
from datetime import datetime

def register_error_handlers(app):

    def error_response(status_code, message, error_type=None, details=None):
        response = {
            "error": {
                "type": error_type or "Error",
                "message": message,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "path": request.path
            }
        }
        if details:
            response["error"]["details"] = details
        return jsonify(response), status_code

    @app.errorhandler(404)
    def not_found(e):
        return error_response(404, "Resource not found", "NotFoundError")

    @app.errorhandler(400)
    def bad_request(e):
        # e.description может содержать подробности ошибки
        details = getattr(e, 'description', None)
        return error_response(400, "Bad request", "BadRequestError", details)

    @app.errorhandler(500)
    def internal_error(e):
        app.logger.error(f"Internal server error: {e}")  # Логируем ошибку
        return error_response(500, "Internal server error", "InternalServerError")
