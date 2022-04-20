

class FourConnectState:

    def __init__(self, state:str,result:str):
        cells = state[:-2].split(',')
        self.state = list(map(lambda cell: FourConnectState.charToNum(cell), cells))
        self.result = result[:-1]

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