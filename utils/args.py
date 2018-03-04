def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            if argv[0] in opts:
                opts[argv[0]].append(argv[1])
            else:
                opts[argv[0]] = [argv[1]]
        argv = argv[1:]
    return opts
