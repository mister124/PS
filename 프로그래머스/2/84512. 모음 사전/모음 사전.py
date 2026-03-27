def solution(word):
    temp = ['A','E','I','O','U']
    val = []
    answer = []
    def BT():
        answer.append("".join(val))
        if len(val) == 5:
                return
        for a in temp:
            val.append(a)
            BT()
            val.pop()
    BT()
    a = answer.index(word)
    return a