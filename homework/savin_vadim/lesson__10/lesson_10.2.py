def repeate(count):
    def any_line(func):
        def wrap(text):
            for _ in range(count):
                func(text)
                print("")
            return
        return wrap
    return any_line


@repeate(4)
def example(text):
    print(text)


example("print me")
