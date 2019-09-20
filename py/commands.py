
DEBUG = False


def get_project_name(args):
    print('You called get_project_name with {}'.format(args))

    if DEBUG:
        return "It works! words={}".format(args.get('word'))
    else:
        import switch_words
