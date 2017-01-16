newFilterList = [1,3,4,5,6,7,34,53,434,24]

##similar to list(map ,list(filter
#pass in lambda function and list and store the result in a new list
result = list(filter(lambda x:x%2==0,newFilterList))

print(result)