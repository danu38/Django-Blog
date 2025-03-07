def hi():
    print("Hi there!")
    print("How are you?")


# hi()


def testName(name):
    if name == "Ola":
        print("Hey Ola!")
    elif name == "Sonja":
        print("Hey Sonja!")


# testName("Ola")
# testName("Sonja")


def greet(name):
    print("Hello " + name + "!")


# greet('Danushka')


girls = ["Danushka", "Nerjis", "Yassmin", "Jana"]

""" for name in girls:
    greet(name)
    print('Next Girls')
     """
# greet(name)

for i in range(1, 6):
    print(i)
