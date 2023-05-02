import requests
#http://localhost:9000/blocks?x=0&y=-62&z=0&dx=21&dy=19&dz=25&includeState=true&includeData=true


def send_request(output, x, y, z, dx, dy, dz, includeState=True, includeData=True):
    request_string="http://localhost:9000/blocks?x="+str(x)+"&y="+str(y)+"&z="+str(z)+"&dx="+str(dx)+"&dy="+str(dy)+"&dz="+str(dz)
    if(includeState==True):
        request_string=request_string+"&includeState=true"
    if(includeData==True):
        request_string=request_string+"&includeData=true"
    response=requests.get(request_string)
    rf=open(output, "w")
    rf.write(response.text)
    rf.close()

print("Pulling in blocks...")
#send_request("SettlementTest1.txt",-175, -61, -260, 88, 14, 116)
send_request("medival1_part2.txt",-22, 71, -175, 97, 22, 93) #God... Please... Work

print("Done")