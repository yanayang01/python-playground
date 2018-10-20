class Greeter():
    def hello(self, name):
        print("Hello, {}".format(name))


if __name__ == "__main__":
    g = Greeter()
    g.hello("world")