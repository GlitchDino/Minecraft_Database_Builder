
from copy import copy, deepcopy

class findLevels:
    #tuning is what percent difference struct blocks need to be to be floor
    def __init__(self, np_arr, exterior_arr, pallete, tuning=20):
        self.np_arr=np_arr
        self.exterior_arr=exterior_arr
        self.pallete=pallete
        self.tuning=tuning
        self.doors=[
            "iron_door",
            "oak_door",
            "spruce_door",
            "birch_door",
            "jungle_door",
            "acacia_door",
            "dark_oak_door",
            "crimson_door",
            "warped_door",
            ]
        
    def test_maybe(self, y, np_symbol):
        arr=np_symbol[y]
        
        shape = (lowest_z, lowest_x, highest_z, highest_x) = self.get_structure_shape(arr)
        top=self.get_percent(shape, np_symbol[y-1])
        floor=self.get_percent(shape, np_symbol[y])
        bottom=self.get_percent(shape, np_symbol[y+1])
        if(floor-self.tuning>top and floor-self.tuning>bottom):
            return True

    

        
    def get_percent(self, shape, arr):
        lowest_z, lowest_x, highest_z, highest_x = shape[0], shape[1], shape[2], shape[3]
        count={"structure":0, "trash":0, "aesth":0, "func":0}
        #print(arr)

        for z in range(lowest_z,highest_z):
            for x in range(lowest_x,highest_x):
                if(arr[z][x]=="X"):
                    count["structure"]+=1
                elif(arr[z][x]=="@"):
                    count["aesth"]+=1
                elif(arr[z][x]=="$"):
                    count["func"]+=1
                else:
                    count["trash"]+=1
        total=highest_x*highest_z
        struct_percentage=100*(float(count["structure"])/float(total))
        aesth_percentage=100*(float(count["aesth"])/float(total))
        func_percentage=100*(float(count["func"])/float(total))
        trash_percentage=100*(float(count["trash"])/float(total))
        #print(struct_percentage, aesth_percentage, func_percentage,trash_percentage)
        return struct_percentage

                

    #eliminates extra air from outside, might be a bad feature 
    def get_structure_shape(self, arr):
        lowest_z, lowest_x, = len(arr), len(arr[0])
        highest_z, highest_x = 0, 0
        for z in range(0,len(arr)):
            for x in range(0, len(arr[0])):
                if(arr[z][x]=="X"):
                    if(z>highest_z):
                        highest_z=z
                    if(z<lowest_x):
                        lowest_z=z
                    if(x>highest_x):
                        highest_x=x
                    if(x<lowest_x):
                        lowest_x=x
        return lowest_z, lowest_x, highest_z, highest_x
    def find_levels(self): #this method is stupid, just use precents
        np_symbol=deepcopy(self.np_arr)
        ext_symbol=deepcopy(self.exterior_arr)
        floor_ys=[]
        maybe=[]
        for y in range(0, len(self.np_arr)):
            for z in range(0, len(self.np_arr[0])):
                ox_string=""
                ex_string=""
                for x in range(0, len(self.np_arr[0][0])):
                    o_id=self.np_arr[y][z][x][0]
                    e_id=self.exterior_arr[y][z][x][0]
                    original_val=self.pallete[o_id]
                    ext_val=self.pallete[e_id]
                    if original_val == "structure":
                        o_str="X"
                    elif(o_id in self.doors):
                        o_str="X"
                    elif original_val == "aesthetic":
                        o_str="@"
                    elif original_val == "function":
                        o_str="$"
                    else:
                        o_str="."

                    if ext_val == "structure":
                        e_str="X"
                    elif ext_val == "aesthetic":
                        e_str="@"
                    elif ext_val == "function":
                        e_str="$"
                    else:
                        e_str="."
                    ox_string=ox_string+o_str
                    ex_string=ex_string+e_str
                    np_symbol[y][z][x]=o_str
                    ext_symbol[y][z][x]=e_str
                connected_str=ox_string+"      "+ex_string
                
                #print(connected_str)
            r_x=self.calc_x(np_symbol[y], ext_symbol[y])
            if(type(r_x)!=list):
                floor_ys.append(y)
            else:
                r_z=self.calc_z(np_symbol[y], ext_symbol[y])
                print("RZ")
                print(r_z)
                z_t=0
                x_t=0
                if(type(r_z)==list):
                    for item in r_z:
                        if(item==True):
                            z_t+=1
                if(type(r_x)==list):
                        
                    for item in r_x:
                        if(item==True):
                            x_t+=1
                if(z_t>4 or x_t>4):
                    self.test_maybe(y, np_symbol)
                    maybe.append(y)
                    #test maybe
                    
        for y in maybe:
            is_floor=self.test_maybe(y, np_symbol)
            if(is_floor==True):
                floor_ys.append(y)

        floor_ys.append(len(self.np_arr)-1)
        
        floor_ys = [*set(floor_ys)]
        floor_ys.sort()
        
        #create floor maybe list, run dist test on it, add floor if distribution test is true too
        remove_list=[]
        for ys in range(0, len(floor_ys)-1):
            bot_floor=floor_ys[ys]
            top_floor=floor_ys[ys+1]
            if(bot_floor+2>top_floor):
                remove_list.append(bot_floor)
        for item in remove_list:
            floor_ys.remove(item)
        self.symbol_arr=np_symbol
        return floor_ys
        #print(floor_ys)
        #print(maybe)


    def calc_x(self, np_arr, ext_arr):
        x_truth_table=[]
        for z in range(0, len(np_arr)):
            z_strip="".join(ext_arr[z])
            first_x=z_strip.find("X")
            last_x=z_strip.rfind("X")
            if(first_x!=-1 and last_x!=-1 and first_x!=last_x):
                #print(first_x, last_x)
                dist=(z, first_x, last_x)
                x_truth_table.append(self.check_x(np_arr, dist))
        if False not in x_truth_table and len(x_truth_table)!=0:
            return True
        else:
            return x_truth_table
    def calc_z(self, np_arr, ext_arr):
        z_truth_table=[]
        for x in range(0, len(np_arr[0])):
            x_strip=[]
            for z in range(0, len(np_arr)):
                x_strip.append(ext_arr[z][x])
            x_strip="".join(x_strip)
            first_z=x_strip.find("X")
            last_z=x_strip.rfind("X")
            if(first_z!=-1 and last_z!=-1 and first_z!=last_z):
                dist=(x, first_z, last_z)
                z_truth_table.append(self.check_z(np_arr, dist))
        if False not in z_truth_table and len(z_truth_table)!=0:
            return True
        else:
            return z_truth_table, 
    def check_z(self, arr, dist):
        x=dist[0]
        first_z=dist[1]
        last_z=dist[2]
        
        for z in range(first_z, last_z):
            if(arr[z][x]=="."):
                return False
        return True
    

    def check_x(self, arr, dist):
        z=dist[0]
        first_x=dist[1]
        last_x=dist[2]
        
        for x in range(first_x, last_x):
            if(arr[z][x]=="."):
                return False
        return True