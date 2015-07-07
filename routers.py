class BaseRouter(object):
    def __init__(self):
        # TODO: need this to reverse urls and config etc
        self.registry = []

    def register(self, request, name):
        self.registry.append((request, name))

    def route(self, request):
        """
        Begins the nested request cascade

        Args:
            request (Request): first request in the chain
        """
        return request.action()


class Router(BaseRouter):
    pass
