
class np2string:
    def __init__(self, arr, pallete):
        self.arr=arr
        self.pallete=pallete
        self.create_pstr()
    
    def create_pstr(self):
        str_list=[]
        p_str=""
        for y in range(0, len(self.arr)):
            p_str=p_str+"\nfloor "+str(y)
            for z in range(0, len(self.arr[0])):
                p_str=p_str+"\n"
                for x in range(0, len(self.arr[0][0])):
                    block_str=self.arr[y][z][x][0]
                    if(self.pallete[block_str]=="aesthetic"):
                        s="@"
                    elif(self.pallete[block_str]=="function"):
                        s="F"
                    elif(self.pallete[block_str]=="structure"):
                        s="X"
                    else:
                        s="."
                    p_str=p_str+s
        self.p_str=p_str