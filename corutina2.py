def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")

def grep_pyton_coroutine():
    g = grep("python")
    yield from g

g = grep_pyton_coroutine()
next(g)
g.send("Python now")
