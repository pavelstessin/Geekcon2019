from http import HTTPStatus
from time import sleep

WAIT = 'wait'
IDLE = 'idle'
RESULTS_READY = 'results_ready'
GREEN_PRESSED = False

last_result = None

# TODO remove the following PoC code !!!
test_state = IDLE
test_counter = 0

def check_green_button():
    global GREEN_PRESSED
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(9, GPIO.OUT)
    GPIO.output(9, GPIO.HIGH)
    while True:
        sleep(0.01)
        if not GREEN_PRESSED:
            if GPIO.input(13):
                print("GREEN is PRESSED")
                GREEN_PRESSED = True
            else:
                print("IDLE")


def poll_for_updates(args=None):
    global test_state
    global test_counter
    global GREEN_PRESSED
    # TODO: if a button was pressed and we don't have a result: tell the client to wait
    # TODO: if a button was pressed and we do have a result: give it to the client (optional: forget the result & the button press)
    # TODO: if a button was not pressed: tell the client there is nothing new

    # TODO: call one of the following:
    # -------------------------------
    # return respond_with_project_results(params={})
    # return respond_wait()
    # return respond_idle()

    if test_state == IDLE:
        if GREEN_PRESSED:
            test_state = WAIT
            GREEN_PRESSED = False
            return respond_wait()

        return respond_idle()
    elif test_state == WAIT:
        test_counter += 1
        if test_counter > 5:
            test_counter = 0
            go_get_results(params={})
            test_state = RESULTS_READY
        return respond_wait()
    else:
        assert test_state == RESULTS_READY
        test_state = IDLE
        return respond_with_project_results()



    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST

    # TODO remove the following PoC code !!!
    # if test_state == IDLE:
        # test_counter += 1
        # if test_counter > 5:
            # test_counter = 0
            # test_state = WAIT
        # return respond_idle()
    # elif test_state == WAIT:
        # test_counter += 1
        # if test_counter > 5:
            # test_counter = 0
            # go_get_results(params={})
            # test_state = RESULTS_READY
        # return respond_wait()
    # else:
        # assert test_state == RESULTS_READY
        # test_state = IDLE
        # return respond_with_project_results()

    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
    # TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST


def go_get_results(params):
    from local_server.talk_to_remote_server import generate_project
    global last_result
    last_result = generate_project(params)


def respond_with_project_results():
    assert last_result, 'No result, cannot return anything'
    return _results_maybe(), HTTPStatus.OK, 'application/json'


def respond_wait():
    return {
               'state': WAIT,
               'title': '',
               'description': '',
           }, HTTPStatus.OK, 'application/json'


def respond_idle():
    return _results_maybe(), HTTPStatus.OK, 'application/json'


def _results_maybe():
    if last_result:
        return {
            'state': RESULTS_READY,
            'title': last_result.get('title', '?'),
            'description': last_result.get('description', '?'),
        }
    else:
        return {
            'state': IDLE,
            'title': '',
            'description': '',
        }
