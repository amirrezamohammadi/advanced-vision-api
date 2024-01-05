def countOccurrence(a):
    k = {}
    for j in a:
        if j in k:
            k[j] +=1
        else:
            k[j] =1
    return k

def formatedResult(b):
    myList = []
    for i in b:
        myList.append(i['name'])

    myDict = countOccurrence(myList)
    new = sorted(myDict.items(), key=lambda x:x[1])
    converted_dict = dict(new)
    finalResult= ''
    for key, value in converted_dict.items():
        text ='{} {},'.format(value,key)
        finalResult = finalResult + text
    return finalResult[:len(finalResult)-1]