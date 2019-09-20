from http import HTTPStatus

DEBUG = False


def get_project_name(args):
    import switch_words
    result = switch_words.get_project()
    code = HTTPStatus.OK
    content_type = 'text/plain'
    return result, code, content_type
