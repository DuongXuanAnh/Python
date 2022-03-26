def ab(b1, b2):
    if not (b1 and b2):  # b1 or b2 is empty
        return b1 + b2
    head = ab(b1[:-1], b2[:-1])
    if b1[-1] == '0':  # 0+1 or 0+0
        return head + b2[-1]
    if b2[-1] == '0':  # 1+0
        return head + '1'
    return ab(head, '1') + '0'

print(ab('011','110'))
