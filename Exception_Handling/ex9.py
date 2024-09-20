# User Difine Exception
class MyError(Exception):
    pass
try:
    raise MyError("my Error")
except MyError as e:
    print(e)