
DEBUG = False


def get_project_name(args):
    if DEBUG:
        print('You called get_project_name with {}'.format(args))
        return "It works! words={}".format(args.get('word'))
    else:
        import switch_words
        return switch_words.get_project()
