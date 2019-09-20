from http import HTTPStatus

DEBUG = False


def get_project_name(args=None):
    from remote_server import switch_words
    selected_title, selected_blurb = switch_words.get_project()
    return {
        'title': selected_title,
        'description': selected_blurb,
    }, HTTPStatus.OK, 'application/json'
