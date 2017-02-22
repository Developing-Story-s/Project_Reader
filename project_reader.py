import os

st = ''
check = 'synchronise_users'
for r, d, f in os.walk(os.getcwd(), topdown=True):
    for fl in f:
        if fl.endswith('.py'):
            file = open(r + '/' + fl, 'r')
            line = file.readline()

            i = 0
            while line:
                i += 1
                if check in line and 'import' not in line and 'read.py' not in fl:
                    st += 'From: ' + r + '/' + fl + '\n' + 'ON FILE: ' + fl + '\nLine:' + str(i) + ' -- ' + line + '\n'
                line = file.readline()
if st:
    log = open("Found_log/" + check + "_log.txt", 'wb')
    log.write(st)
    print('Logged')
