from copy import copy, deepcopy
import numpy as np
import ast

from .find_structures import findStructures
from .print_array import printArray
from .find_exterior import findExterior
from .find_levels_original import findLevels
from .find_rooms import findRooms
from .np_to_printstring import np2string
#LATER:
#create module for floorplan
#add render modes
#save arrs in dataset 


#BEFORE BUILDING DATASET:
#input builder 

#Tommorow:
#compress
#before charlie::
#add total buildings count to db
#test: pulling arrays from dataset/other maps
#build 10,000 datapoints
#create an impressive ai to handle all datapoints to prove usefulness
#easy, no sweat :-P


class Block:
    def __init__(self, id, x, y, z, state, data, type, is_connected=False, is_searched=False):
      self.id=id
      self.x=x
      self.y=y
      self.z=z
      self.state=state
      self.data=data
      self.type=type
      self.is_connected=is_connected
      self.is_searched=is_searched
      self.structures=[]
#Settlement(self.settlement_arr,self.stl, self.pallete, self.entity_path)
class Settlement:
    def __init__(self, settlement_arr, stl, pallete, entity_path):
        self.settlement_array=settlement_arr #.txt or .npy
        self.stl=stl
        self.structs=stl
        self.pallete=pallete
        self.entity_path=entity_path
        self.max_y=len(self.settlement_array)
        self.max_z=len(self.settlement_array[0])
        self.max_x=len(self.settlement_array[0][0])
        self.structs=self.stl["Structures"]
        self.building_count=0 
        self.structures=[]
        


    def add_building(self, building_arr, building_name=None):
        building_name="Building_"+str(self.building_count)
        struct_group=self.structs.create_group(building_name)
        x=Structure(building_name, building_arr, self.pallete, self.entity_path, struct_group)
        x.find_exterior_arr()
        self.structures.append(x)
        self.building_count+=1
        
    def find_all_levels(self): #finds all floors for all buildings
        for structure in self.structures:
            structure.find_levels()
    
    def find_all_rooms(self):
        for structure in self.structures:
            for level in structure.levels:
                if(level.function!="multi_top"):
                    level.find_rooms()




class Structure:
    def __init__(self, structure_name, building_array, pallete, entity_path, struct_group):
        self.structure_name=structure_name
        self.np_arr=building_array
        self.pallete=pallete
        self.entity_path=entity_path
        self.struct_group=struct_group
        self.max_y=len(self.np_arr)
        self.max_z=len(self.np_arr[0])
        self.max_x=len(self.np_arr[0][0])
        self.totalBlocks=self.max_x*self.max_z*self.max_y
        self.xzArea=self.max_x*self.max_z
        self.allFloorCords=[]
        self.levelList=[]
        self.levels=[]
        self.function="None"
        self.struct_group.attrs["function"]=self.function
        self.print_string=""

    def set_function(self, function_str):
        self.function=function_str
        self.struct_group.attrs["function"]=self.function

    def find_exterior_arr(self):
        np_copy=deepcopy(self.np_arr)
        ext_obj=findExterior(np_copy, self.pallete)
        self.exterior_arr=ext_obj.find_exterior()
    
    def find_levels(self):
        level_src_obj=findLevels(self.np_arr, self.exterior_arr, self.pallete)
        results=level_src_obj.find_levels()
        self.symbol_arr=level_src_obj.symbol_arr
        level_cords=[]
        for y in range(1, len(results)):
            bottom=results[y-1]
            top=results[y]
            level_cord=(bottom, top)
            level_cords.append(level_cord)

        self.create_levels(level_cords)

    def create_levels(self, level_cords):
        cord_count=len(level_cords) 
        level_count=0
        if(cord_count==1):
            level_function="single_level"
            level_name="Level_0"
            level_group=self.struct_group.create_group(level_name) # save 3d array here
            level_group.attrs["function"]=level_function
            cord=level_cords[0]
            bottom, top = cord[0], cord[1]
            level_arr=self.np_arr[bottom:top+1]
            level_group.attrs["cords"]=(bottom, top)
            level=Level(level_name, level_arr, self.symbol_arr, cord, level_function, self.pallete, self.entity_path, level_group)
            self.levels.append(level)
        else:
            for i in range(0, len(level_cords)):
                if(i == 0):
                    level_function="multi_bottom"
                elif(i == len(level_cords)-1):
                    level_function="multi_top"
                else:
                    level_function="multi_mid"
                level_name="Level_"+str(i)
                level_group=self.struct_group.create_group(level_name) # save 3d array here
                level_group.attrs["function"]=level_function
                cord=level_cords[i]
                bottom, top = cord[0], cord[1]
                level_arr=self.np_arr[bottom:top+1]
                level_group.attrs["cords"]=(bottom, top)
                level=Level(level_name, level_arr, self.symbol_arr, level_cords[i], level_function, self.pallete, self.entity_path, level_group)
                self.levels.append(level)
        
class Level:
    def __init__(self, level_name, level_array, symbol_arr, cords, function, pallete, entity_path, level_group):
        self.level_name = level_name
        self.level_array = level_array
        self.symbol_arr=symbol_arr
        self.cords=cords
        self.pallete = pallete
        self.entity_path=entity_path
        self.function=function
        self.level_group=level_group
        self.rooms=[]
        self.room_count=0

    def print_level(self):
        bottom, top = self.cords[0], self.cords[1]

        for y in range(bottom, top+1):
            print("Y:"+str(y))
            for z in range(0, len(self.symbol_arr[0])):
                x_str=""
                for x in range(0, len(self.symbol_arr[0][0])):
                    s=self.symbol_arr[y][z][x]
                    x_str=x_str+s
                print(x_str)
    
    def find_floorplan(self):
        self.floorplan=np.empty((len(self.level_array[0]), len(self.level_array[0][0])), dtype=object)
        bottom, top = self.cords[0], self.cords[1]
        for z in range(0, len(self.symbol_arr[0])):
            for x in range(0, len(self.symbol_arr[0][0])):
                y_strip=[]
                for y in range(bottom, top+1):
                    s=self.symbol_arr[y][z][x]
                    y_strip.append(s)
                wall_string=self.is_ystrip_wall(y_strip)
                self.floorplan[z][x]=wall_string

    def is_ystrip_wall(self, y_strip):
        is_wall=True
        contains_func=False
        air_count=0
        struct_count=0
        func_count=0
        for i in range(1, len(y_strip)-1):
            block=y_strip[i]
            if(block=="."):
                is_wall=False
                air_count+=1
            elif(block=="X"):
                struct_count+=1
            else:
                is_wall=False
                func_count+=1
        
        if(is_wall==False):
            if(struct_count == 0):
                is_wall=False
            elif(func_count==0 and air_count<2):
                is_wall=True

        
        if(is_wall==True):
            return "W"
        else:
            return "."



    def find_rooms(self):
        self.find_floorplan()
        x=findRooms(self.level_array, self.floorplan)
        room_list, room_cords = x.find_rooms()
        offset_count=0
        for room_arr in room_list:
            self.add_room(room_arr, room_cords[offset_count])
            offset_count+=1

    def add_room(self, room_arr, offset):
        room_str="Room "+str(self.room_count)
        room_group=self.level_group.create_group(room_str)
        room_group.attrs["offset"]=offset
        room_group.attrs["function"]="None"
        room=Room(room_str, offset, room_arr, self.entity_path, room_group, self.pallete)
        room_aesth_pallete=str(room.aesthetic_pallete)
        room_func_pallete=str(room.function_pallete)
        room_group.attrs["aesthetic_pallete"]=room_aesth_pallete
        room_group.attrs["function_pallete"]=room_func_pallete
        self.rooms.append(room)
        self.room_count+=1
        
class Room:
    def __init__(self, name, offset, room_array, entity_path, room_group, pallete, function=None, ):
        self.name = name
        self.offset = offset
        self.room_array=room_array
        self.function=function
        self.entity_path=entity_path
        self.room_group=room_group
        self.pallete = pallete
        self.function_pallete=[]
        self.aesthetic_pallete=[]
        self.max_y=0
        self.max_x=0
        self.max_z=0
        self.npArr=None
        self.print_string=""
        self.find_pallete()
    def init_room_array(self):
        self.max_y=len(self.npArr)
        self.max_z=len(self.npArr[0])
        self.max_x=len(self.npArr[0][0])
    def find_pallete(self):
        for y in range(0, len(self.room_array)):
            for z in range(0, len(self.room_array[0])):
                for x in range(0, len(self.room_array[0][0])):
                    block_id=self.room_array[y][z][x][0]
                    type=self.pallete[block_id]
                    if(type=="function"):
                        if(block_id not in self.function_pallete):
                            self.function_pallete.append(block_id)
                    elif(type=="aesthetic"):
                        if(block_id not in self.aesthetic_pallete):
                            self.aesthetic_pallete.append(block_id)
class BrickEditor:
    def __init__(self, search_id="door"):
        self.map_p=None
        self.settlement_name=None
        self.is_connected=[]
        self.settlement_arr=[]
        self.search_id=search_id # item to be use as search 4 house point
        self.search_list=[]
        self.arrStructP=[]
        self.ban_list=["dirt", "grass_block", "air"] #edit this to pallete list
        self.building_count=0
        self.settlement=""
    #render_mode decides wether we save pictures, models, etc
    def create_world(self, stl, entity_path, trash, render_mode=None): 
        print("Created world")
        self.stl=stl
        self.entity_path=entity_path #folder to save .npy, .png, .dat
        self.trash = trash
        pallete_str=stl.attrs["pallete"]
        self.pallete=ast.literal_eval(pallete_str)
        self.np_file=stl.attrs["file"]
        self.structs=self.stl.create_group("Structures")
        
        self.init_blocks()
        fs=findStructures(self.structs, self.settlement_arr, self.search_list, self.trash, entity_path)
        buildings=fs.find_buildings()
        self.structs.attrs["count"]=len(buildings)
        self.init_settlement(buildings)
        self.settlement.find_all_levels()
        self.settlement.find_all_rooms()
        if(render_mode=="string"):
            self.find_print_strings()
        self.save_all_arrays_to_database()
        #self.print_all_arrays()
    def find_print_strings(self):
        for structure in self.settlement.structures:
            s_str=np2string(structure.np_arr, self.pallete).p_str
            structure.print_string=s_str
            structure.struct_group.attrs["print_string"]=s_str
            for level in structure.levels:
                for room in level.rooms:
                    p_str=np2string(room.room_array, self.pallete).p_str
                    room.print_string=p_str
                    room.room_group.attrs["print_string"]=p_str
    def save_all_arrays_to_database(self):
        for structure in self.settlement.structures:
            structure_s=self.entity_path+structure.structure_name
            ext_arr=structure.exterior_arr
            s_str=structure_s+".npy"
            e_str=structure_s+"_ext.npy"
            np.save(s_str, structure.np_arr)
            np.save(e_str, ext_arr)
            structure.struct_group.attrs["file"]=s_str
            for level in structure.levels:
                level_s=structure_s+"_"+level.level_name
                s_str=level_s+".npy"
                np.save(s_str, level.level_array)
                level.level_group.attrs["file"]=s_str
                for room in level.rooms:
                    room_s=level_s+"_"+room.name+".npy"
                    np.save(room_s, room.room_array)
                    room.room_group.attrs["file"]=room_s
    def print_all_arrays(self):
        for structure in self.settlement.structures:
            print(structure.structure_name)
            printArray(structure.np_arr)
            for level in structure.levels:
                print(structure.structure_name+" "+level.level_name)
                printArray(level.level_array)
                for room in level.rooms:
                    print(structure.structure_name+" "+level.level_name+" "+room.name)
                    printArray(room.room_array)



    def init_settlement(self, buildings):
        self.settlement=Settlement(self.settlement_arr,self.stl, self.pallete, self.entity_path)
        
        for building in buildings:
            self.settlement.add_building(building)
        #i dont think this function is needed still
        #settlement.calculate_block_percentages() 
    
    def init_blocks(self):
        array=np.load(self.np_file, allow_pickle=True)
        self.max_y=len(array)
        self.max_z=len(array[0])
        self.max_x=len(array[0][0])
        self.settlement_arr=np.empty((self.max_y, self.max_z, self.max_x), dtype=object)
        for y in range(0,self.max_y):
            for z in range(0, self.max_z):
                for x in range(0, self.max_x): 
                    id_str=array[y][z][x][0]
                    type=self.pallete[id_str]
                    if(self.search_id in id_str):
                        block=Block(id_str, x,y,z, array[y][z][x][1],array[y][z][x][2], type)
                        self.search_list.append(block)
                    else:
                        block=Block(id_str, x,y,z, array[y][z][x][1],array[y][z][x][2], type)
                    self.settlement_arr[y][z][x]=block
    

"""create ref:

    def create_settlement(self, map_p, settlement_name, screenshot=True):
        if screenshot == True:
            self.screenshot_all()

"""

