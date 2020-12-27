import time


class TryClass:
    value = 1
    valu = 2
    val = 3
    va = 4
    v = 5

    def __init__(self, value=4):
        print("Created TryClass :", self)
        self.value = value

    def metod1(self, value, val2=""):
        self.value += value
        print(f"\t>>> metod 1, add: {value}, now value : {self.value}, val2: {val2}")
        time.sleep(2)
        return self.value

    @classmethod
    def metod2(cls, value, val2=""):
        cls.value = 2
        print(f"\t>>> metod 2, add: {value}, now value : {cls.value}, val2: {val2}")
        return cls.value

    @staticmethod
    def metod3(value, val2=""):
        TryClass.value += value
        print(f"\t>>> metod 3, add: {value}, now value : {TryClass.value}, val2: {val2}")
        return TryClass.value


def event_call(other_arg, kwarg="-", result=None):
    """Call this metod, on returned result"""
    print(f"Bind Result, {result}\n"*10)
    print("other_arg", other_arg)
    print("kwarg", kwarg)


if __name__ == "__main__":
    try:
        from dirio import Dirio
    except:
        from ..dirio import Dirio

    dr_cls = Dirio(target=TryClass, args=(888,), kwargs={}, worker=False)

    print("Starting values   :", dr_cls.value, dr_cls)
    print("\n"*2)

    print("Wait 1 sec for your reply.  metod 1 :", dr_cls.metod1(5, val2="1", dr_wait=1))
    print("Wait until the reply comes. metod 1 :", dr_cls.metod1(5, val2="1", dr_wait=-1))

    code0 = dr_cls.metod1(5, val2="1", dr_code=True)
    print("Metod 1, call, via bind to func", dr_cls.dr_bind(code0, event_call, args=("OtHeR aRg", ), kwargs={"kwarg": "KwArG"}))

    while True:
        #
        dr_cls.dr_binds_check()

        print("Run the method and give us the response reading code : dr_code=True")
        code1 = dr_cls.metod1(5, val2="1", dr_code=True)

        print("Is there data in the reading code? : dr_code=43534")
        while not dr_cls.metod1(dr_code=code1):
            print("We are waiting for the data with this code :", code1)

            time.sleep(.5)
        print("Returned metod 1 data :", dr_cls.metod1(dr_code=code1))

        print("Methods called this way give the last return value :  nothing or dr_code=False")

        code2 = dr_cls.metod2(10, val2="2", dr_code=True)
        print("Search by code only                 :", dr_cls.dr_code(code2, wait=1))

        print("Trying metod 2, called and returned :", dr_cls.metod2(10, val2="2", dr_code=False))
        print("Trying metod 3, called and returned :", dr_cls.metod3(15, val2="3"))
        print("\n"*2)

        time.sleep(3)

    dr_cls.dr_terminate()
