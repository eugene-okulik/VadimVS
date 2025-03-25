def finish_me(func):
    def wrap(*args, **kwargs):
        func(*args, **kwargs)
        print("")  # для задания пустой строки, как в задаче
        print("finished")
    return wrap


@finish_me
def example(text):
    print(text)


example("Test " + str(11 + 22))
