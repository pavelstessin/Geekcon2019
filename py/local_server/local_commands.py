from http import HTTPStatus

WAIT = 'wait'

IDLE = 'idle'


def poll_for_updates(args=None):
    # TODO: if a button was pressed and we don't have a result: tell the client to wait
    # TODO: if a button was pressed and we do have a result: give it to the client (forget the result & the button press)
    # TODO: if a button was not pressed: tell the client there is nothing new

    return respond_with_project_results(params={})
    # return respond_wait()
    # return respond_idle()


def respond_with_project_results(params):
    from local_server.talk_to_remote_server import generate_project
    data = generate_project(params)
    return {
               'state': IDLE,
               'title': data.get('title', '?'),
               'description': data.get('description', '?'),
           }, HTTPStatus.OK, 'application/json'


def respond_wait():
    return {
               'state': WAIT,
               'title': '',
               'description': '',
           }, HTTPStatus.OK, 'application/json'


def respond_idle():
    return {
               'state': 'idle',
               'title': '',
               'description': '',
           }, HTTPStatus.OK, 'application/json'
