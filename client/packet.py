import math

class Packet:
    def __init__(self, type=0, data="", author = "SERVER"):
       self.type = type
       self.data = data
       self.author = author
    def pack(self) -> bytearray:
        if type(self.data) == str:
            return bytearray(str(self.author) + ";" + str(self.type) + "^" + self.data, "utf-8")
    def unpack(self, pckt: bytearray) -> tuple:
        decoded = pckt.decode("utf-8")
        self.author = decoded.split(";")[0]
        remainingData = ";".join(decoded.split(";")[1:])
        arr = remainingData.split("^")
        self.type = int(arr[0])
        self.data = "^".join(arr[1:])
        if self.type == 0 or self.type == 1 or self.type == 2 or self.type == 255:
            return (self.author, self.type, self.data)
    def __repr__(self):
        return f"Packet({repr(self.author)}, {repr(self.type)}, {repr(self.data)})"

def tileIntToBools(tileValue: int) -> list[bool]:
    bools = []
    divisors = [8, 4, 2, 1]
    for divisor in divisors:
        i = math.floor(tileValue/divisor)
        bools.append(bool(i))
        tileValue -= i*divisor
    return bools