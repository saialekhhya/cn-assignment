class CRC:

    def __init__(self):
        self.cdw = ''

    def xor(self, a, b):
        result = []
        for i in range(1, len(b)):
            if a[i] == b[i]:
                result.append('0')
            else:
                result.append('1')

        return ''.join(result)

    def crc(self, message, key):
        pick = len(key)

        tmp = message[:pick]

        while pick < len(message):
            if tmp[0] == '1':
                tmp = self.xor(key, tmp) + message[pick]
            else:
                tmp = self.xor('0' * pick, tmp) + message[pick]

            pick += 1

        if tmp[0] == "1":
            tmp = self.xor(key, tmp)
        else:
            tmp = self.xor('0' * pick, tmp)

        checkword = tmp
        return checkword

    def encodedData(self, data, key):
        l_key = len(key)
        append_data = data + '0' * (l_key - 1)
        remainder = self.crc(append_data, key)
        codeword = data + remainder
        self.cdw += codeword
        print("Remainder: ", remainder)
        print("Data to be transmitted: ", codeword)

    def reciverSide(self, data, key):
        r = self.crc(data, key)
        size = "0"
        a = size.ljust(len(key)-1,"0")
        print(r)
        if r == a:
            print("No Error. Correct data has been transmitted")
        else:
            print("Error. Data received does not match as the remainder is not zero.")


data = str(input("Enter the data:"))
key = str(input("Enter the divisor:"))
c = CRC()
c.encodedData(data, key)
print('---------------')
received = str(input("Enter the received string:"))
c.reciverSide(received, key)
print('---------------')
print("The correct data is:",c.cdw)