from http import HTTPStatus


def poll_for_updates(args=None):
    # TODO: if a button was pressed and we don't have a result: tell the client to wait
    # TODO: if a button was pressed and we do have a result: give it to the client (forget the result & the button press)
    # TODO: if a button was not pressed: tell the client there is nothing new
    return {
               'state': 'idle',
               'title': '',
               'description': '',
           }, HTTPStatus.OK, 'application/json'
