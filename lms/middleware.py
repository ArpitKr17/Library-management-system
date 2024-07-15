import logging

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('django')

    def __call__(self, request):
        response = self.get_response(request)
        endpoint = request.path
        method = request.method
        user = request.user if request.user.is_authenticated else 'Anonymous'
        self.logger.info(f"Endpoint: {endpoint}, Method: {method}, User: {user}")
        self.logger.info(f"{request.method} {request.path} {response.status_code}")
        return response
