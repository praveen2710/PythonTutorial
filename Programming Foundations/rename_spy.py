import os

def rename_files():
    #1 Get Files in list
    file_list = os.listdir("/Users/shonababu/Documents/prank")
    print(file_list)

    os.chdir("/Users/shonababu/Documents/prank")  
  
    #2 Rename all files in list
    for file_name in file_list:
        #print(file_name)
        os.rename(file_name,file_name.translate(None,"0123456789"))       
        
rename_files()
