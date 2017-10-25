def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")




g = grep("python")
next(g)
g.send("Hello world")
g.send("Hello python world")
g.throw(RuntimeError, "banana error")