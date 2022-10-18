cantidad = 100
msg = ''
for i in range(0,2):
    for j in range(0,4):
        msg += str(j+4*i)+' '
    msg += '\n'

for x in range(8,cantidad,8):
    msg += '\n'
    for i in range(0,2):
        for j in range(x,x+4):
            if (j+4*i>=cantidad):
                msg += '__ '
            else:
                msg += str(j+4*i)+' '
        msg += '\n'

print(msg)

for x in range(1,(cantidad//8)+1):
    print(x)