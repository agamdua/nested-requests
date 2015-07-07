Nested Requests
===============

Take 2 on the nested requests problem.

#### Situation:
Make one request and based on the response make another request. Repeat.

How much conditional logic should go in the function that is most likely the
controller (or if you're using django, views)?

Controllers should be thin. This library moves the control logic
from the controllers to the routers.


**Note**: the requests with which the routers are configured should really not
contain business logic. They should be viewed as a layer of abstraction on top
of the business logic layer.


#### Example

Please refer `examples.py` for now.


#### License
ISC license
