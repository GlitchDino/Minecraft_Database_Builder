import requests
#http://localhost:9000/blocks?x=0&y=-62&z=0&dx=21&dy=19&dz=25&includeState=true&includeData=true
import time

def send_request(output, x, y, z, dx, dy, dz, includeState=True, includeData=True):
    request_string="http://localhost:9000/blocks?x="+str(x)+"&y="+str(y)+"&z="+str(z)+"&dx="+str(dx)+"&dy="+str(dy)+"&dz="+str(dz)
    print(request_string)
    if(includeState==True):
        request_string=request_string+"&includeState=true"
    if(includeData==True):
        request_string=request_string+"&includeData=true"
    print("Sending request...")
    st= time.time()
    mins=100
    timeout_max=mins*60
    try:
        response=requests.get(request_string, timeout=timeout_max)
        n=dx*dy*dz
        #elapsed_time = et - st
        print("n: "+str(n))
        #print("Time:", elapsed_time)	
        elapsed_time = time.time() - st
        print('Time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        print("Request received. Writing...")
        rf=open(output, "w")
        rf.write(response.text)
        print("Writing complete.")
        rf.close()

    except:
        elapsed_time = time.time() - st
        print('Failed at:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

send_request("MedivalEmpty2.txt",-137, 3, -12, 180, 40, 29)








print("Pulling in blocks...")
#send_request("SettlementTest1.txt",-175, -61, -260, 88, 14, 116)
#send_request("MEDIVAL_1.txt",-27, 69, -232, 221, 66, 156) #God... Please... Work
#send_request("MEDIVAL2_Settlement1.txt",166, 63, 180, 70, 31, 77)
#send_request("MEDIVAL_falcon_boat2.txt",513, 49, 806, 36, 63, 101)
#send_request("MEDIVAL_falcon_Settlement2_part3_labeled.txt",563, 61, 478, 66, 37, 176)
#send_request("MEDIVAL_falcon_Settlement2_part3_unlabeled.txt",563, 61, 478, 66, 37, 176)
print("Done")