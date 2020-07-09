def polate(arrays,query):
    #sorting
    for i in arrays:
        for k in range(len(arrays)-1):
            if(arrays[k][0]>arrays[k+1][0]):
                dummy = arrays[k]                                       #sort with a loop
                arrays[k] = arrays[k+1]
                arrays[k+1] = dummy
    return do(arrays,query)
def do(arrays,query):
    answer = []
    for i in range(1,len(arrays[0])-1):
        if(query<arrays[0][0] or query > arrays[len(arrays)-1][0]):                         #extrapolate- use minn and max
            answer.append(arrays[len(arrays)-1][i]+(arrays[len(arrays)-1][i]-arrays[0][i])/(arrays[len(arrays)-1][0]-arrays[0][0])*(query-arrays[len(arrays)-1][0]))
        else:
            for i in range(1,len(arrays)):
                if(query>arrays[i-1][0] and query <arrays[i][0]):
                    for k in range(1,len(arrays[0])):
                        answer.append(arrays[i][k] + (arrays[i][k] - arrays[i-1][k]) / (arrays[i][0] - arrays[i-1][0]) * (query - arrays[i][0]))
    return answer           #use most appropriate line section not just overall line

arrays = []
dimensions = int(input('Enter the number of dimensions '))
file = input("What is the file name with the extension included?")          #get dimensions and open the file
with open(file,'r') as f:
    a=f.read().split('\n')
    temp = []
    for i in a:
        temp = []
        for k in i.split(' '):                      #get list of lists
            temp.append(int(k))
        arrays.append(temp)
query = float(input("Enter the query value "))
print('for x value ', query , 'the following other dimesnions were returned ',polate(arrays,query),sep='')
