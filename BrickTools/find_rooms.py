import numpy as np
from operator import itemgetter
from itertools import groupby
from .print_array import printArray
from copy import deepcopy
import json
class findRooms:
    def __init__(self, level_arr, floorplan):
        self.level_arr=level_arr
        self.floorplan=floorplan
        self.room_dict={}
        self.room_keys=[]


    def find_rooms(self):
        area_arr=self.detect_areas()
        self.create_room_dict()
        self.src()
        self.create_room_cords()
        self.create_room_arrays()
        return self.room_list, self.minmax_dict
    
    def create_room_cords(self):
        for key in self.room_keys:

            room_cords=self.room_dict[key]
            cord_list=[]
            for cord in room_cords:
                nearby_walls=self.nearby(cord)
                cord_list.append(cord)
                cord_list.extend(nearby_walls)
            res = [*set(cord_list)]
            self.room_dict[key]=res
    """    def create_room(self, arr):
        for cord in arr:
            x=cord[0]
            z=cord[1]
            for y in range(0, len(self.level_arr)):
                block=[y][x][z]"""

    def src(self):
        for key in self.room_dict.keys():
            sub_arr=self.room_dict[key]
            #sub_arr1=deepcopy(self.room_dict[key])
            #sub_arr2=deepcopy(self.room_dict[key])
            x_dict={}
            z_dict={}
            for item in sub_arr:
                x=item[0]
                z=item[1]
                if(x not in x_dict.keys()):
                    x_dict[x]=(z, z)
                else:
                    min_max=x_dict[x]
                    min_z=min_max[0]
                    max_z=min_max[1]
                    if(z>max_z):
                        max_z=z
                    if(z<min_z):
                        min_z=z
                    cord=(min_z, max_z)
                    x_dict[x]=cord
                
                if(z not in z_dict.keys()):
                    z_dict[z]=(x, x)
                else:
                    min_max=z_dict[z]
                    min_x=min_max[0]
                    max_x=min_max[1]
                    if(x>max_x):
                        max_x=x
                    if(x<min_x):
                        min_x=x
                    cord=(min_x, max_x)
                    z_dict[z]=cord
            x_res=self.x_dict_search(x_dict)
            z_res=self.z_dict_search(z_dict)
            if(x_res==True and z_res==True):
                self.room_keys.append(key)
    def z_dict_search(self, z_dict):
        interior=True
        for z in z_dict.keys():
            cord=z_dict[z]
            min_x=cord[0]
            max_x=cord[1]
            if(min_x!=0):
                str=self.floorplan[z][min_x-1]
                if(str=="W"):
                    top="W"
                else:
                    top=None
            else:
                top=None
            if(max_x+1!=len(self.floorplan[0])):
                str=self.floorplan[z][max_x+1]
                if(str=="W"):
                    bottom="W"
                else:
                    bottom=None
            else:
                bottom=None
            if(top!="W" or bottom!="W"):
                interior=False
        return interior
    def x_dict_search(self, x_dict):
            interior=True
            for x in x_dict.keys():
                cord=x_dict[x]
                min_z=cord[0]
                max_z=cord[1]
                if(min_z!=0):
                    str=self.floorplan[min_z-1][x]
                    if(str=="W"):
                        top="W"
                    else:
                        top=None
                else:
                    top=None
                if(max_z+1!=len(self.floorplan)):
                    str=self.floorplan[max_z+1][x]
                    if(str=="W"):
                        bottom="W"
                    else:
                        bottom=None
                else:
                    bottom=None
                if(top!="W" or bottom!="W"):
                    interior=False
            return interior
    #creates new 2D walls array with labeled connected empty space
    #used to detect rooms
    def detect_areas(self):
        z=0
        it=1
        cord_list=[]
        for z in range(0, len(self.floorplan)):
            for x in range(0, len(self.floorplan[0])):
                if(self.floorplan[z][x]=="."):
                    start_point=(z, x)
                    self.find_from_start_points(start_point, it)
                    it+=1

    #finds all adjecent air blocks to a starting air block.
    def find_from_start_points(self, start_point, it):
        q=[]
        q.append(start_point)
        area_cords=[start_point]
        while(q):
            cord=q.pop()
            z=cord[0]
            x=cord[1]
            ans=self.get_adjacent_air(cord)
            self.floorplan[z][x]=it
            q.extend(ans)
        #return arr
    
    #finds all adjecent empty cords to one cord
    #used to find empty spaces that could be rooms
    def get_adjacent_air(self, cords):
        x=cords[1]
        z=cords[0]
        val_list=[]
        if(x-1>=0):
            b_str=self.floorplan[z][x-1]
            if(b_str=="."):
                val_list.append((z, x-1))
        if(x+1<len(self.floorplan[0])):
            b_str=self.floorplan[z][x+1]
            if(b_str=="."):
                val_list.append((z, x+1))
        if(z-1>=0):
            b_str=self.floorplan[z-1][x]
            if(b_str=="."):
                val_list.append((z-1, x))
        if(z+1<len(self.floorplan)):
            b_str=self.floorplan[z+1][x]
            if(b_str=="."):
                val_list.append((z+1, x))
        return val_list

    def print_floorplan(self):
        print("Floorplan")
        for z in range(0, len(self.floorplan)):
            z_str=""
            for x in range(0, len(self.floorplan[0])):
                x_str=self.floorplan[z][x]
                if(type(x_str)==int):
                    x_str=str(x_str)
                z_str=z_str+x_str
            print(z_str)

    #includes walls into room cords
    def build_room_cords(self, cords):
        ans_arr=[]
        ans_arr.extend(cords)
        for cord in cords:
            z=0
            x=0
            ans=self.nearby(cord)
            ans_arr.extend(ans)
        res = [*set(ans_arr)]
        return res

    #finds all walls adjectent to a block, so we can save walls of room (called by build_room_cords)
    def nearby(self, cord):
        x=cord[0]
        z=cord[1]
        max_z=len(self.floorplan)
        max_x=len(self.floorplan[0])
        returnArr=[]
        if(x>0 and z>0):
            block_str=self.floorplan[z-1][x-1]
            if(block_str=="W"):
                returnArr.append((x-1, z-1))
        if(x!=0):
            block_str=self.floorplan[z][x-1]
            if(block_str=="W"):
                returnArr.append((x-1, z))
        if(z!=0):
            block_str=self.floorplan[z-1][x-1]
            if(block_str=="W"):
                returnArr.append((x, z-1))

        if(z+1<max_z):
            block_str=self.floorplan[z+1][x]
            if(block_str=="W"):
                returnArr.append((x, z+1))
            if(x-1>=0):
                block_str=self.floorplan[z+1][x-1]
                if(block_str=="W"):
                    returnArr.append((x-1, z+1))            

        if(x+1<max_x):
            block_str=self.floorplan[z][x+1]
            if(block_str=="W"):
                returnArr.append((x+1, z))
            if(z-1>=0):
                block_str=self.floorplan[z-1][x+1]
                if(block_str=="W"):
                    returnArr.append((x+1, z-1))   
        if(z+1<max_z and x+1<max_x):
            block_str=self.floorplan[z+1][x+1]
            if(block_str=="W"):
                returnArr.append((x+1, z+1))    

        return returnArr




    #creates dictionary of room cords
    def create_room_dict(self):
        for z in range(0, len(self.floorplan)):
            for x in range(0, len(self.floorplan[0])):
                p_str=self.floorplan[z][x]
                if(p_str!="W"):
                    if(str(p_str) not in self.room_dict):
                        self.room_dict[str(p_str)]=[(x, z)]
                    else:
                        self.room_dict[str(p_str)].append((x, z))
    #runs calculation functions on wether an empty space is a room or part of an interior building
    #returns dictionary of all empty space cords and keys for spaces that are rooms


    #creates a 3D array for all detected rooms
    def create_room_arrays(self):
        room_count=0
        self.room_list=[]
        self.minmax_dict={}
        for key in self.room_keys:
            room_cords=self.room_dict[key]

            #finds lowest and biggest x and zs for room area
            min_z=float("inf")
            min_x=float("inf")
            max_z=float("-inf")
            max_x=float("-inf")
            for cord in room_cords:
                if(cord[0]<min_x):
                    min_x=cord[0]
                if(cord[1]<min_z):
                    min_z=cord[1]
                if(cord[0]>max_x):
                    max_x=cord[0]
                if(cord[1]>max_z):
                    max_z=cord[1]
            area_x=max_x-min_x
            area_z=max_z-min_z
            iz=min_z
            ix=min_x
            z=0
            x=0
            y=0
            min_y=0
            max_y=len(self.level_arr)
            room_arr=np.empty((max_y, area_z+1, area_x+1), dtype=object)

            while(iz<=max_z):
                ix=min_x
                x=0
                while(ix<=max_x):
                    
                    if((ix, iz) in room_cords):
                        y=0
                        while(y<max_y):
                            block_str=self.level_arr[y][iz][ix]
                            room_arr[y][z][x]=block_str
                            y+=1
                    else:
                        y=0
                        #fills empty space for parts of the array that arn't part of the room 
                        while(y<max_y):
                            block_str2=("air", "exterior", "None")
                            room_arr[y][z][x]=block_str2
                            y+=1
                        
                    ix+=1
                    x+=1
                z+=1
                iz+=1
            #room_name=level_name+"_room"+str(room_count)+".npy"
            #numpy_room_file=np.save(room_name, room_arr)
            
            min_max=((min_x, min_y, min_z), (max_x, max_y, max_z))
            self.minmax_dict[room_count]=min_max
            self.room_list.append(room_arr)
            room_count+=1


    #master function to detect rooms using a 2D wall array

        

        



