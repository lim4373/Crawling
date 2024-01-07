from dataclasses import make_dataclass
# #test_file03 ->python모듈을 사용해서 변환
MyFile = make_dataclass(
    "MyFile",
    fields=[("mypath", str), ("mystr", str)],
    namespace={
        "my_write": lambda self: self._write_file(self),
        "my_read": lambda self: self._read_file(self),
        "_write_file": lambda self: self.__class__._write_file(self),
        "_read_file": lambda self: self.__class__._read_file(self), # 외부 함수 호출 참조
    },
)

@staticmethod
def _write_file(self):
    with open(self.mypath, 'a') as f:
        f.write(self.mystr)

@staticmethod
def _read_file(self):
    with open(self.mypath, 'r') as f:
        print(f.read())

MyFile._write_file = _write_file
MyFile._read_file = _read_file

if __name__ == "__main__":
    my_file = MyFile("file.txt", "Hello, World! 배아파요")
    my_file.my_write()
    my_file.my_read()
