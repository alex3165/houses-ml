# Arguments table
# -i: Input file to process
# -f: Filter to use


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


def areArgumentsValid(required, args):
    RES = list(filter(lambda x: x in args, required))
    return len(RES) == len(required)
