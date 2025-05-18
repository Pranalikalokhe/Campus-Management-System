import logging
from datetime import datetime

class UserActionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename='user_actions.log',
            level=logging.INFO,
            format='%(asctime)s %(levelname)s: %(message)s'
        )

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        if user.is_authenticated:
            path = request.path
            if 'login' in path:
                logging.info(f"{user.username} logged in")
            elif 'logout' in path:
                logging.info(f"{user.username} logged out")
            elif 'enroll' in path:
                logging.info(f"{user.username} enrolled in a course")
            elif 'upload' in path:
                logging.info(f"{user.username} submitted an assignment")

        return response
