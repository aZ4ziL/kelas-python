class Hello:
    def __init__(self, nama) -> None:
        self.nama = nama

    def hello(self) -> str:
        return "Hello: %s" % self.nama

    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

    @classmethod
    def test():
        pass


@aoisdhoasidh
def test():
    pass
