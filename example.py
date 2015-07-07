from .request import POSTRequest
from .routers import Router

router = Router()


class FirstRequest(POSTRequest):
    raise NotImplementedError('needs a config')


router.register((FirstRequest, 'first_request'))
