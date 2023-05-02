
from copy import copy, deepcopy

class findLevels:
    #tuning is what percent difference struct blocks need to be to be floor
    def __init__(self, np_arr, exterior_arr, pallete, tuning=10):
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
        
        #shape = (lowest_z, lowest_x, highest_z, highest_x) = self.get_structure_shape(arr)
        shape = (0, 0, len(np_symbol[0]), len(np_symbol[0][0]))
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
        if(total<20):
            struct_percentage=0
        else:
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
        floor_ys.append(0)
        for y in range(1, len(self.np_arr)-1):
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

