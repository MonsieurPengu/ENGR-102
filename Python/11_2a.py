def polate(listx,listy,query):
    #sorting
    for i in listx:
        for k in range(len(listx)-1):
            if(listx[k]>listx[k+1]):
                dummy = listx[k]                                                    #just a bubble sort
                listx[k] = listx[k+1]
                listx[k+1] = dummy
                dummy = listy[k]
                listy[k] = listy[k + 1]
                listy[k + 1] = dummy
    return do(listx,listy,query)
def do(listx,listy,query):
    answer = 0
    if(query<listx[0] or query > listx[len(listx)-1]):
        answer = listy[len(listy)-1]+(listy[len(listy)-1]-listy[0])/(listx[len(listx)-1]-listx[0])*(query-listx[len(listx)-1])          #extrapolation
    else:
        for i in range(1,len(listx)-1):
            if(query>=listx[i-1] and query <=listx[i]):
                answer = listy[i] + (listy[i] - listy[i-1]) / (listx[i] - listx[i-1]) * (query - listx[i])              #interpolation
    return answer

listx = []
listy = []
file = input("What is the file name with the extension included?")
with open(file,'r') as f:
    for i in f:
        a = i.split(' ')
        listx.append(int(a[0]))                     #gte as lists
        listy.append(int(a[1]))
query = float(input("Enter the query value "))                              #cant be eequal to avalue alreadyy
print(polate(listx,listy,query))



