from http import HTTPStatus

DEBUG = False


def get_project_name(args):
    import switch_words
    selected_title, selected_blurb = switch_words.get_project()
    code = HTTPStatus.OK
    content_type = 'text/plain'
    return selected_title, code, content_type
