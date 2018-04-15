def say_hello(name=None):
    return {"message": "Hello {}, from api.greeting".format(name or "")}