import requests
#http://localhost:9000/blocks?x=0&y=-62&z=0&dx=21&dy=19&dz=25&includeState=true&includeData=true
import time

def send_request(output, x, y, z, dx, dy, dz, includeState=True, includeData=True):
    request_string="http://localhost:9000/blocks?x="+str(x)+"&y="+str(y)+"&z="+str(z)+"&dx="+str(dx)+"&dy="+str(dy)+"&dz="+str(dz)
    n=dx*dy*dz
    max_n=100*100*100
    if(n>max_n):
        if(dx>100):

            rx=x
            fc=0
            while(rx<dx):
                remaining = dx-rx
                sx=100
                print("Rx: "+str(rx))
                
                if(remaining<100):
                    sx=remaining
                else:
                    tx=rx+100
                    if(tx<dx):
                        rx+=100

                request_string="http://localhost:9000/blocks?x="+str(rx)+"&y="+str(y)+"&z="+str(z)+"&dx="+str(sx)+"&dy="+str(dy)+"&dz="+str(dz)

                

        elif(dz>100):
            tz=0
        else:
            print("later")
            

    
    print(request_string)
    if(includeState==True):
        request_string=request_string+"&includeState=true"
    if(includeData==True):
        request_string=request_string+"&includeData=true"
    print("Sending request...")
    st= time.time()
    response=requests.get(request_string)
    
    n=dx*dy*dz
    #elapsed_time = et - st
    print("n: "+str(n))
    #print("Time:", elapsed_time)	
    elapsed_time = time.time() - st
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

    print("Request received. Writing...")
    rf=open(output, "w")
    rf.write(response.text)
    print("Writing complete.")
    rf.close()

print("Pulling in blocks...")
#send_request("SettlementTest1.txt",-175, -61, -260, 88, 14, 116)
#send_request("MEDIVAL_1.txt",-27, 69, -232, 221, 66, 156) #God... Please... Work
send_request("3k_test.txt",0, 0, 0, 100, 100, 100)

print("Done")