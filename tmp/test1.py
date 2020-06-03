from functools import wraps
def test01(func):
    print(func)
    # @wraps(func)
    def wrappers(*args, **kwargs):
        func(*args, **kwargs)
        print("func_doc:%s" % func.__name__)
        print("test01-data")
    return wrappers


@test01()
def test02(data, data1="asdda"):
    print("data:%s" % data)
    print(test02.__name__)




if __name__ == "__main__":
    test02("dadadadsdsadasdsa")
