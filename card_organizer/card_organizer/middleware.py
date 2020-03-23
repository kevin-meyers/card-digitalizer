from django.contrib.sessions.middleware import SessionMiddleware

class MySessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        if request.path_info.startswith('/api/'):
            return
        super(MySessionMiddleware, self).process_request(request)

    def process_response(self, request, response):
        if request.path_info.startswith('/api/'):
            return response
        return super(MySessionMiddleware, self).process_response(request, response)
