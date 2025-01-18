f = open('abc.txt', 'w+')
k = open('qws.txt','a')


def reader(a):
    a.seek(0)
    print(a.read())

def writer(b,string):
    b.write(str(string))

reader(f)
writer(k,'aman')
reader(k)