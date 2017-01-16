###File Handling

##Writing to file
#open file in write mode
file = open("demo_file.txt","w")

#writing to file without a  buffer
file.write("writing to file from program \n I am the best")
file.write("\n writing by calling write again")
#read contents of file does not work  when in write mode
# print(file.read())

#always close your file to avoid file handling issue
file.close()

##Reading from file
#open file in read mode
file = open("demo_file.txt","r")

#loads one line at a time and also we can mention how many bytes to read from each line
print(file.readline(2))

print(file.read(10))
#read contents of file
print(file.read())
##############the above brings pointer to end of file hence the below does not print anything###########
print(file.read(10))

#always close your file to avoid file handling issue
file.close()


##Appedning to exisiting file
#re-opening file in write mode will clear existing data if we do in write mode hence append 'a' mode
file = open("demo_file.txt","a")

#adding to existing file will add where the write pointer was ended
file.write("Writng when opening in second time")
#read contents of file does not work  when in write mode
# print(file.read())

#always close your file to avoid file handling issue
file.close()
