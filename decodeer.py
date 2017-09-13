refer = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
refer2 = {}
for key in refer:
    mid = refer[key]
    refer2[mid] = key


def enc(x):
    a = list(bin(ord(x)))[2:]
    # a.pop(0)
    # a.pop(0)
    b = [a[i:i+4] for i in range(0,len(a),4)]


    c = [int(''.join(i),2) for i in b]

    new = [refer[i] for i in c]
    return ''.join(new)

# def renc(xs):
#     ly = []
#     for i in xs:
#         ly.append(enc(i))
#     print(ly)
#     for i in ly:
#         if len(i) != len(ly[ly.index(i)+1]) and i != '|':
#             ly.insert('|',ly.index(i)+1)
#     return ''.join(ly)
def renc(xs):
    ly = []
    for i in xs:
        ly.append(enc(i))
    a = [i for i in range(len(ly)-1) if len(ly[i]) != len(ly[i+1])]
    for i in range(len(a)):
        ly.insert(a[i]+1+i,'|')
    return ''.join(ly)




def dehanc(x):
    la = [x[i:i+4] for i in range(0,len(x),4)]
    y = ''
    for i in la:
        bych = ''
        for j in range(4):
            byij = bin(refer2[i[j]])[2:]
            while len(byij) < 4:
                byij = '0' + byij
            bych = bych + byij
        y = y + chr(int(bych,2))
    return y

def deengc(x):
    la = [x[i:i+2] for i in range(0, len(x), 2)]
    y = ''
    for i in la:
        bych = ''
        for j in range(2):
            byij = bin(refer2[i[j]])[2:]
            while len(byij) < 4:
                byij = '0' + byij
            bych = bych + byij
        y = y + chr(int(bych, 2))
    return y


a = ['我', '想', '你', '试', '第', '二', '个', '函', '数', 'r', 'e', 'n', 'c','哈']
b = ['r', 'e', 'n', 'c']
c = ['r']
d = 'ly在变长'
e = 'abcd1234'
print(renc(e))
print(renc(d))
print(renc(a))