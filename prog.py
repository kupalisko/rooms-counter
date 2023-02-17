with open("mapa1.txt", "r") as vstup:
    path1 = vstup.readlines()

path = []

for times, line in enumerate(path1):
    path.append([znak for znak in line])
    if times< len(path1)-1:path[times].remove('\n')

stop = False
izby = 0
setold = set()
while True:
    for i in range(1,len(path[0])-1):
        for j in range(1,len(path)-1):
            if path[i][j] == " ":
                print(i, j)
                path[i][j] = '*'
                stop = True
                break
        if stop:
            stop=False
            break
            
    else : break


    setold.add((i,j))
    while len(setold)>0:
        setnew = set()
        for z in setold:
            i,j = z[0],z[1]
            
            if path[i-1][j] == " " and i-1>0:
                setnew.add((i-1,j))
                path[i-1][j] = '*'
            if path[i+1][j] == " " and i+1<len(path[0]):
                setnew.add((i+1,j))
                path[i+1][j] = '*'
            if path[i][j-1] == " "and j-1>0:
                setnew.add((i,j-1))
                path[i][j-1] = '*'
            if path[i][j+1] == " " and j+1 <len(path):
                setnew.add((i,j+1))
                path[i][j+1] = '*'
            setold = setnew

        for line in path:
            for char in line:
                print(char, end='')
            print()
        print("")

    izby += 1

print(path)
for line in path:
    for char in line:
        print(char, end='')
    print()

print(setnew)
print(izby)