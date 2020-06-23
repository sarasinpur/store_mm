import os

def check_ping():
    hostname = "8.8.8.8"
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

pingstatus = check_ping()

file1 = open("D:\\Users\\sarasinpur\\Desktop\\Work\\MM_Store\\myfile.txt","a")#append mode 
file1.write(pingstatus) 
file1.close()

print(pingstatus)