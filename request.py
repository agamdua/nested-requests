import requests


class Request(object):
    def __init__(self, url, data, method, router=None, **kwargs):
        """
        Initializes the first request.

        Args:
            url (str): a url that needs to be hit (only post supported for now)
            router (Router): Specifies the router if there is nested behavior
            kwargs (dict): additional configuration of the route
        """
        self.url = url
        self.data = data
        self.method = method

        self.router = router

        for k, v in kwargs.items():
            setattr(self, k, v)

    def action(self):
        response = getattr(requests, self.method)(url=self.url, data=self.data)

        if not self.router:
            return response

        raise NotImplementedError(
            'TODO: Case of nested router to be written'
        )

    def on_success(self):
        raise NotImplementedError(
            'needs to be overwritten if there is no nested route here'
        )

    def on_failure(self):
        raise NotImplementedError(
            'failure behavior needs to be defined by overwriting this method'
        )

POSTRequest = type('POSTRequest', (Request,), {'method': 'POST'})
