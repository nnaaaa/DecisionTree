

class FourConnectState:

    def __init__(self, state:str,result:str):
        cells = state[:-2].split(',')
        self.state = list(map(lambda cell: FourConnectState.charToNum(cell), cells))
        self.result = result

    def show(self):
        for i in range(0, 6):
            row = []
            for j in range(0, 7):
                index = 6*(j+1) - i - 1
                row.append(FourConnectState.numToChar(self.state[index]))
            print(row)

        print(self.result)

    @staticmethod
    def charToNum(char):
        if char == 'b':
            return 0
        elif char == 'o':
            return 1
        elif char == 'x':
            return -1

    @staticmethod
    def numToChar(num):
        if num == 0:
            return 'b'
        elif num == 1:
            return 'o'
        elif num == -1:
            return 'x'