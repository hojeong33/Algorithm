# 오목
def myMehod():
    mylist = []
    for i in range(19):
        mylist.append(list(map(int, input().split())))
    t = 5
    for i in range(19):
        for j in range(19):
            if mylist[i][j] != 0:
                r = i + 1
                c = j + 1
                if mylist[i][j + 1] == mylist[i][j]:
                    while t > 0:
                        if mylist[i][j + 1] == mylist[i][j]:
                            t -= 1
                            j += 1
                        else:
                            break
                    if mylist[i][j + 1] != mylist[i][j]:
                        return mylist[i][j], r, c
                j=c-1
                i=r-1
                t = 5
                if mylist[i + 1][j] == mylist[i][j]:
                    while t > 0:
                        if mylist[i + 1][j] == mylist[i][j]:
                            t -= 1
                            i += 1
                        else:
                            break
                    if mylist[i + 1][j] != mylist[i][j]:
                        return mylist[i][j], r, c
                j = c - 1
                i = r - 1
                t = 5
                if mylist[i + 1][j + 1] == mylist[i][j]:
                    while t > 0:
                        if mylist[i + 1][j + 1] == mylist[i][j]:
                            t -= 1
                            j += 1
                            i += 1
                        else:
                            break
                    if mylist[i + 1][j + 1] != mylist[i][j]:
                        return mylist[i][j], r, c
                return 0,'',''


ans=myMehod()
print(ans[0])
print('{} {}'.format(ans[1],ans[2]))
