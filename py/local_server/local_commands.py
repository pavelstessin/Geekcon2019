from http import HTTPStatus

WAIT = 'wait'
IDLE = 'idle'
RESULTS_READY = 'results_ready'

# TODO remove the following PoC code !!!
teststate = IDLE
testcounter = 0


def poll_for_updates(args=None):
    # TODO: if a button was pressed and we don't have a result: tell the client to wait
    # TODO: if a button was pressed and we do have a result: give it to the client (forget the result & the button press)
    # TODO: if a button was not pressed: tell the client there is nothing new

    # TODO: call one of the following:
    # -------------------------------
    # return respond_with_project_results(params={})
    # return respond_wait()
    # return respond_idle()




    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    global teststate
    global testcounter

    # TODO remove the following PoC code !!!
    if teststate == IDLE:
        testcounter += 1
        if testcounter > 5:
            testcounter = 0
            teststate = WAIT
        return respond_idle()
    elif teststate == WAIT:
        testcounter += 1
        if testcounter > 5:
            testcounter = 0
            teststate = RESULTS_READY
        return respond_wait()
    else:
        testcounter += 1
        if testcounter > 5:
            testcounter = 0
            teststate = IDLE
            return respond_with_project_results(params={})
        else:
            return respond_wait()

    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST



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
