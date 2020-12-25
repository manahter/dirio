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
        print(f"metod 1, add: {value}, now value : {self.value}, val2: {val2}")
        return self.value

    @classmethod
    def metod2(cls, value, val2=""):
        cls.value = 2
        print(f"metod 2, add: {value}, now value : {cls.value}, val2: {val2}")
        return cls.value

    @staticmethod
    def metod3(value, val2=""):
        TryClass.value += value
        print(f"metod 3, add: {value}, now value : {TryClass.value}, val2: {val2}")
        return TryClass.value


if __name__ == "__main__":
    import time
    try:
        from dirio import Dirio
    except:
        from ..dirio import Dirio

    dr_cls = Dirio(target=TryClass, args=(888,), kwargs={}, worker=False)

    print("Starting values   :", dr_cls.value, dr_cls)
    print("\n"*2)

    while True:
        print("Run the method and give us the response reading code : dr_code=True")
        cv = dr_cls.metod1(5, val2="1", dr_code=True)

        print("Is there data in the reading code? : dr_code=43534")
        while not dr_cls.metod1(dr_code=cv):
            print("We are waiting for the data with this code :", cv)

            time.sleep(.1)
        print("Returned metod 1 data :", dr_cls.metod1(dr_code=cv))

        print("Methods called this way give the last return value :  nothing or dr_code=False")
        print("Trying metod 2, called and returned :", dr_cls.metod2(10, val2="2", dr_code=False))
        print("Trying metod 3, called and returned :", dr_cls.metod3(15, val2="3"))
        print("\n"*2)

        time.sleep(3)

    dr_cls.dr_terminate()