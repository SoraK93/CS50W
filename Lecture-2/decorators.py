def announce(f):
    def wrapper():
        print("About to run th function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()
