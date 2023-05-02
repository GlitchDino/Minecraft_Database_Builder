import requests
#http://localhost:9000/blocks?x=0&y=-62&z=0&dx=21&dy=19&dz=25&includeState=true&includeData=true


def send_request(output, x, y, z, dx, dy, dz, includeState=True, includeData=True):
    request_string="http://localhost:9000/blocks?x="+str(x)+"&y="+str(y)+"&z="+str(z)+"&dx="+str(dx)+"&dy="+str(dy)+"&dz="+str(dz)
    if(includeState==True):
        request_string=request_string+"&includeState=true"
    if(includeData==True):
        request_string=request_string+"&includeData=true"
    print("Sending request...")
    response=requests.get(request_string)
    print("Request received. Writing...")
    rf=open(output, "w")
    rf.write(response.text)
    print("Writing complete.")
    rf.close()

print("Pulling in blocks...")
#send_request("SettlementTest1.txt",-175, -61, -260, 88, 14, 116)
send_request("MEDIVAL_1.txt",-27, 69, -232, 221, 66, 156) #God... Please... Work

print("Done")