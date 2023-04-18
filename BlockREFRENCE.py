import numpy

import findRoomsClean as findRooms
import os
from lib import render as ren
import json

#LATER:
#create module for find_all_rooms and find_all_levels
#save offsets of settlements, buildings and levels
#Examine room_offsets, might be fucked

#BEFORE BUILDING DATASET:

#input builder 

#MAYBE BEFORE:
#do pallete in parser
#write room-iding for 1 room buildings
#autoplace wool:
    #identify where to place red wool
    #remove connected red wool (so there arn't duplicates)
#make calc wall equation change depending on room height





class Settlement:
    def __init__(self, settlement_name, settlement_array, aesthetic, path):
        self.settlement_name=settlement_name
        self.settlement_array=settlement_array #.txt or .npy
        self.aesthetic=aesthetic #style of the town, medivial, ruined, etc.
        self.pallete=None
        self.path=path
        self.structures=[]
        self.arr_settlement=None
        self.building_count=0
        self.distributionDict={}
        self.percentageDict={}
        self.npArr=[]
        self.max_y=0
        self.max_x=0
        self.max_z=0
        self.settlementPallete=[]
        self.settlement_dict={}


    
    #adds building to settlement class
    def add_building(self, building_arr, building_name=None):
        self.buildPallete()
        if(building_name==None):
            name_str="Building_"+str(self.building_count)
            building_name=name_str
            x=Structure(building_name, self.aesthetic, building_arr, self.pallete, path=self.path)
            x.init_struct_array()
            x.find_exterior_arr()
        self.structures.append(x)
        self.building_count+=1

    #builds the dictionary we use to save and print settlements. Makes it easier to load.
    def build_dictionary(self):
        self.settlement_dict["Settlement"]={"name": self.settlement_name, 
                                            "fp":self.settlement_array, 
                                            "aesthetic":self.aesthetic,
                                            "real_cord": (0, 0, 0),
                                            "size": (self.max_x, self.max_y, self.max_z),
                                            "pallete": self.pallete,
                                            "Structures":{}
                                            }
        
        for building in self.structures:
            self.settlement_dict["Settlement"]["Structures"][building.building_name]={
                "file":building.building_array,
                "ext_file":building.exterior_arr,
                "function":building.function,
                "size": (building.max_x, self.max_y, self.max_z),
                "offset": (0, 0, 0),
                "Levels":{}
            }
            for level in building.levels:
                self.settlement_dict["Settlement"]["Structures"][building.building_name]["Levels"][level.level_name]={
                "file": level.level_array,
                "function": level.function,
                "size": (level.max_x, level.max_y, level.max_z),
                "offset": level.level_cords,
                "Rooms":{}
                }
                room_c=0
                for room in level.rooms:
                    room_key="room_"+str(room_c)
                    self.settlement_dict["Settlement"]["Structures"][building.building_name]["Levels"][level.level_name]["Rooms"][room_key]={
                    "file": room.room_array,
                    "function": room.function,
                    "size": (room.max_x, room.max_y, room.max_z),
                    "offset": room.offset,
                    "room_pallete": room.room_pallete
                    }
                    room_c+=1
    def print_dictionary(self, indent=2):
        print(json.dumps(self.settlement_dict, sort_keys=False, indent=indent))
    
    #finds what blocks are in each room
    def find_room_pallete(self):
        for building in self.structures:
            for level in building.levels:
                for room in level.rooms:

                    for y in range(0, room.max_y):
                        for z in range(0, room.max_z):
                            for x in range(0, room.max_x):
                                block_id=room.npArr[y][z][x][0]
                                if block_id not in room.room_pallete.keys():
                                    purp=self.pallete[block_id]
                                    room.room_pallete[block_id]=(purp, 1)
                                else:
                                    purp=room.room_pallete[block_id][0]
                                    it=room.room_pallete[block_id][1]
                                    it+=1
                                    room.room_pallete[block_id]=(purp, it)
    #calculates what blocks are in the map, and what precent of the map they make up
    def calculate_block_percentages(self):
        y, x, z = 0, 0, 0

        while(y<self.max_y):
            while(x<self.max_x):
                while(z<self.max_z): 
                    id_str=self.npArr[y][x][z][0]
                    if(id_str not in self.distributionDict.keys()):
                        self.distributionDict[id_str]=1
                    else:
                        self.distributionDict[id_str]+=1
                    
                    z+=1
                z=0
                x+=1
            y+=1
            x=0

        for key in self.distributionDict.keys():
            block_count=self.distributionDict[key]
            percentage=100*(float(block_count)/float(self.totalBlocks))
            self.percentageDict[key]=percentage
        sort=sorted(self.percentageDict.items(), key=lambda x:x[1], reverse=True)
        self.percentageDict=dict(sort)
    #calculates precent
    def calculate_all_building_percentages(self):
        for item in self.structures:
            item.calculate_building_block_percentages()
    
    #master function to make 

    def find_all_levels(self):
        for item in self.structures:
            item.y_distribution_tagged(self.pallete)
            item.find_floors()
            item.init_level()
    
    def find_all_rooms(self):
        for item in self.structures:
            item.find_building_rooms()

    def print_buildings(self):
        print("Structures in Settlement "+self.settlement_name+":")
        if(len(self.structures)>0):
            for structure in self.structures:
                print(structure.building_name)
        else:
            print("No buildings exist for this settlement")

    def save_settlement(self, output_file=None): #saves settlement class data to .txt to be recovered later
        if(output_file==None):
            output_file=self.path+self.settlement_name+"_save_file.txt"
        with open(output_file, 'w') as of:
            of.write(json.dumps(self.settlement_dict))



    def buildPallete(self):
        for key in self.distributionDict.keys():
            self.settlementPallete.append(key)
        #print(self.settlementPallete)
        p=Pallete("standard", self.settlementPallete)
        self.pallete=p.buildPallete()
        #return selfpallete
        #llete)

class Structure:
    def __init__(self, building_name, aesthetic, building_array, settlement_pallete, path=None, function=None,):
        self.building_name=building_name
        self.aesthetic=aesthetic
        self.function=function
        self.path=path
        self.building_array=building_array
        self.settlement_pallete=settlement_pallete
        self.npArr=[]
        self.levels=[]
        self.level_count=0
        self.max_x=0
        self.max_y=0
        self.max_z=0
        self.totalBlocks=0
        self.distributionDict={}
        self.percentageDict={}
        self.floor_percentage_dictionary={}
        self.percentageFloorDict={}
        self.percentages=[]
        self.sortedPercents=[]
        self.floorY=[]
        self.floorPointers=[]

    def init_struct_array(self):
        self.npArr=numpy.load(self.building_array, allow_pickle=True)
        self.max_y=len(self.npArr)
        self.max_x=len(self.npArr[0])
        self.max_z=len(self.npArr[0][0])
        self.totalBlocks=self.max_x*self.max_z*self.max_y
        self.xzArea=self.max_x*self.max_z
        self.allFloorCords=[]
        self.levelList=[]
        self.exterior_arr=[]
    
    def returnArr(self):
        return self.npArr
    def find_exterior_arr(self):
        self.exterior_arr=fe.find_exterior(self.building_array, self.settlement_pallete)

        
    #creates precentages of blocks for each indexed level of a building
    def calculate_building_block_percentages(self):
        y, x, z = 0, 0, 0

        while(y<self.max_y):
            pur=0
            while(x<self.max_x):
                
                while(z<self.max_z): 
                    id_str=self.npArr[y][x][z][0]
                    if(id_str not in self.distributionDict.keys()):
                        self.distributionDict[id_str]=1
                    else:
                        self.distributionDict[id_str]+=1
                        
                    if(id_str not in self.floor_percentage_dictionary.keys()):
                        self.floor_percentage_dictionary[id_str]=1
                    else:
                        self.floor_percentage_dictionary[id_str]+=1
                    
                    z+=1
                z=0
                x+=1   
            for key in self.floor_percentage_dictionary.keys():
                block_countY=self.floor_percentage_dictionary[key]
                percentage=100*(float(block_countY)/float(self.xzArea))
                self.percentageFloorDict[key]=percentage
                pur=pur+percentage
            sort=sorted(self.percentageFloorDict.items(), key=lambda x:x[1], reverse=True)
            self.percentageFloorDict=dict(sort)
            self.percentages.append(self.percentageFloorDict)
            #print("PERCENT FLOOR DICTIONARY")
            #print(self.percentageFloorDict)
            #print(pur)
            self.floor_percentage_dictionary={}
            #used to be percentageDict
            self.percentageFloorDict={}
            
            y+=1
            x=0


        for key in self.distributionDict.keys():
            block_count=self.distributionDict[key]
            percentage=100*(float(block_count)/float(self.totalBlocks))
            self.percentageDict[key]=percentage
        sort=sorted(self.percentageDict.items(), key=lambda x:x[1], reverse=True)
        self.percentageDict=dict(sort)

    #creates dictionary of the percent of type blocks (trash/function/aesthetic/structure)
    #in each y level of the 3D array
    #This is used later to detect where the floors of our buildings are,
    #a floor level will have a much greater level of structure blocks than it's y+1 y-1 nieghbors
    def y_distribution_tagged(self, pallete, verbose=False):
        
        for item in self.percentages:       
            test_distribution={
                "trash":0,
                "function":0,
                "aesthetic":0,
                "structure":0
            }
            pur=0
            for block in item.keys():
                #print(block)
                tag=pallete[block]

                val=item[block]
                pur+=val

                total=test_distribution[tag]

                cur_total=total+val
                test_distribution.update({tag:cur_total})
            self.sortedPercents.append(test_distribution)
        y_inc=0
        if(verbose==True):
            print("NEW BUILDING")
            for item in self.sortedPercents:
                print("floor "+str(y_inc)+" block distribution:")
                print(item)
                y_inc+=1
        



    def find_floors(self, diff=20, verbose=False):
        y=0
        top_y=len(self.sortedPercents)-1
        for item in self.sortedPercents:
            if(y==0):
                if(item["structure"]>5):
                    self.floorY.append(y)
                    bottom_y=y
                else:
                    #delete
                    print("FLOOR ISSUE PLEASE CHECK")
            else:
                if(y+1!=top_y and y!=top_y):
                    prev=self.sortedPercents[y-1]
                    next=self.sortedPercents[y+1]
                    cur_structPer=item["structure"]
    
                    prev_structPer=prev["structure"]
                    next_structPer=next["structure"]
                    if(cur_structPer-diff>prev_structPer and cur_structPer-diff>next_structPer):
                        self.floorY.append(y)
                    
            y+=1
        self.floorY.append(top_y)
        if(verbose==True):
            print("Floors found at levels:")
            for item in self.floorY:
                print(item)

    def init_level(self):
        print("INIT FLOOR")
        print(self.floorY)
        if(len(self.floorY)<2 or len(self.floorY)%2!=0):
            print("Error initilizing floors for building:")
            print(self.building_name)
        elif(len(self.floorY)==2):
            floorFunction="singleLevel"
            floorCords=(self.floorY[0], self.floorY[1])
            self.allFloorCords.append(floorCords)
            self.levelList.append((floorCords, floorFunction))
            #self.add_level(floorFunction, floorCords)
        else:
            i=0
            for cord in self.floorY:
                if(i<len(self.floorY)-1):

                    floorCords=(self.floorY[i], self.floorY[i+1])
                    self.allFloorCords.append(floorCords)
                i+=1
            floor_c=0
            while(floor_c<len(self.allFloorCords)):
                if(floor_c==0):
                    floorFunction="multiBottom"
                elif(floor_c==len(self.allFloorCords)-1):
                    floorFunction="multiTop"
                else:
                    floorFunction="multiMid"
                self.levelList.append((self.allFloorCords[floor_c],floorFunction))
                floor_c+=1
        self.save_floor()
        
      
    def save_floor(self):
        level_count=0
        for item in self.levelList:
            cords=item[0]
            bottomY=cords[0]
            topY=cords[1]+1
            function=item[1]
            levelArr=self.npArr[bottomY:topY]
            name_str=self.building_name+"_level"+str(level_count)

            save_str=self.path+name_str+".npy"
            
            

            self.floorPointers.append(save_str)
            numpy.save(save_str, levelArr)
            self.levels.append(Level(save_str, name_str, cords, self.aesthetic, function=function, path=self.path))
            level_count+=1

    def find_building_rooms(self):
        for level in self.levels:
            level.pallete=self.settlement_pallete
            #print(self.settlement_pallete)
            level.find_level_rooms()


    def add_level(self, function):
        self.level_count+=1
        level_name="floor_"+str(self.level_count)

class Level:
    def __init__(self, level_array, level_name, level_cords, aesthetic, path=None,pallete=None, function=None):
        self.level_name=level_name
        self.aesthetic=aesthetic
        self.function=function
        self.level_array=level_array
        self.level_cords=level_cords
        self.pallete=pallete
        self.path=path
        self.room_count=0
        self.rooms=[]
        self.npArr=0
        self.max_y=0
        self.max_x=0
        self.max_z=0

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

    def init_level_array(self):
        self.npArr=numpy.load(self.level_array, allow_pickle=True)

        self.max_y=len(self.npArr)
        self.max_x=len(self.npArr[0])
        self.max_z=len(self.npArr[0][0])
    
    def find_level_rooms(self):
        self.init_level_array()
        if(self.function!="multiTop"):
            #builds 2D array of all possible walls

            printy.printArr(self.npArr)
            bottom_floor=0
            top_floor=self.max_y-1
            dx=[]
            dz=[]
            i=1
            y=1
            x=0
            z=0
            while(x<self.max_x):
                dz=[]
                while(z<self.max_z):
                    wall=True
                    dy=[]
                    while(y<top_floor):
                        block_str=self.npArr[y][x][z][0]
                        dy.append(block_str)

                        #do a chance percentage
                        #
                        y+=1
                    #calculates if index is a wall or not
                    wall=self.is_wall(dy, 60)
                    dz.append(wall)
                    z+=1
                    y=0    
                dx.append(dz)
                x+=1
                z=0
            print("Wall Arr")
            #print(dx)
            dx=numpy.array(dx)
            room_arrs, room_cords=findRooms.find_rooms(dx, self.level_array, self.path)
            self.print_rooms(room_arrs)
            #print(room_arrs)
            for item in room_arrs:
                name=item[:-4]
                number=name[-1:]
                cords=room_cords[int(number)]
                self.add_room(name, cords, item)




    def print_rooms(self, room_list):
        room_count=0
        for room_p in room_list:
            room=numpy.load(room_p, allow_pickle=True)
            print("Room "+str(room_count))
            printy.printArr(room)
            room_count+=1


    def is_wall(self, yArr, tolerance):
        total=len(yArr)
        yArrTagged=[]
        for item in yArr:
            if(item=="air"):
                yArrTagged.append("air")
            elif(item not in self.doors): #if item isnt door
                tag=self.pallete[item]
                yArrTagged.append(tag)
            else:
                yArrTagged.append("door")
        


        wallChance=100
        doorChance=100
        isDoor=False
        wall=True
        answer=None
        block_weight=100*1/total
        for item in yArrTagged:
            if(item=="air"):
                wallChance-=block_weight
            elif(item=="door"):
                answer= "X"#used to be D
            elif(item!="structure"):
                wallChance-=(block_weight/2)
        if(answer==None):
            if(wallChance==100):
                answer= "X"
            elif(wallChance==0):
                answer= "."
            elif(wallChance>tolerance):
                answer= "X"
            else:
                answer= "."

        return answer
        
    def add_room(self, name, offset, arr_p):
        x=Room(name, offset, arr_p, self.aesthetic, path=self.path)
        x.init_room_array()
        #x.room_pallete()
        self.rooms.append(x)

        self.room_count+=1
        #name_str="Room_"+str(room_count)

class Room:
    def __init__(self, name, offset, room_array, aesthetic, path=None, function=None, ):
        self.name = name
        self.offset = offset
        self.room_array=room_array
        self.aesthetic = aesthetic
        self.function=function
        self.path=path
        self.room_pallete={}
        self.max_y=0
        self.max_x=0
        self.max_z=0
        self.npArr=None
    def init_room_array(self):
        self.npArr=numpy.load(self.room_array, allow_pickle=True)

        self.max_y=len(self.npArr)
        self.max_z=len(self.npArr[0])
        self.max_x=len(self.npArr[0][0])


class tagBlock:
    def __init__(self, id, state, data, function):
        self.id=id
        self.state=state
        self.data=data
        self.function=function
    
class Block:
    def __init__(self, id, x, y, z, state, data, is_connected=False, is_searched=False):
      self.id=id
      self.x=x
      self.y=y
      self.z=z
      self.state=state
      self.data=data
      self.is_connected=is_connected
      self.is_searched=is_searched

class BlockEditor:
    def __init__(self):
        self.map_p=None
        self.settlement_name=None
        self.is_connected=[]
        self.houses=[]
        self.block_arr=[]
        self.wool_list=[]
        self.arrStructP=[]
        self.ban_list=["dirt", "grass_block", "air"] #edit this to pallete list
        self.max_x=0
        self.max_y=0
        self.max_z=0
        self.building_count=0
        self.settlement=""
    
    def printConnected(self):
        for item in self.is_connected:
            print(item.x, item.y, item.z, item.id)

       
    def init_blocks(self):
        array=numpy.load(self.map_p, allow_pickle=True)
        name=self.map_p[:-4]
        x=0
        y=0
        z=0
        
        self.max_y=len(array)
        self.max_x=len(array[0])
        self.max_z=len(array[0][0])
        self.block_arr=numpy.empty((self.max_y, self.max_x, self.max_z), dtype=object)
        while(y<self.max_y):
            while(x<self.max_x):
                while(z<self.max_z): 
                    #print(array[y][x][z])
                    id_str=array[y][x][z][0]
                    if(id_str=="red_wool"):
                        block=Block(id_str, x,y,z, array[y][x][z][1],array[y][x][z][2])#is_connected=true
                        self.wool_list.append(block)
                    else:
                        block=Block(id_str, x,y,z, array[y][x][z][1],array[y][x][z][2])
                    self.block_arr[y][x][z]=block
                    
                    z+=1
                z=0
                x+=1
            y+=1
            x=0
        return self.block_arr


        #return self.block_arr()
    
    def initSettlement(self, structure_p_arr,aesthetic, function=None):
        settlement=Settlement(self.settlement_name, self.map_p, aesthetic, path=self.path)
        settlement.init_settlement_array()
        settlement.calculate_block_percentages()
        for fp in structure_p_arr:
            settlement.add_building(fp)
        settlement.print_buildings()
        self.settlement=settlement
    

    

    #function that loads settlement from settlement_save file


    #parses map into settlement class 
    def create_settlement(self, map_p, settlement_name, screenshot=True):
        self.map_p=map_p
        self.settlement_name=settlement_name
        parent_dir=os.getcwd()
        self.path = os.path.join(parent_dir, settlement_name)
        os.makedirs(self.path, exist_ok = True)
        self.path=self.path+"/"
        self.init_blocks()

        find_structure_obj=fs.findStructures(self.block_arr, self.wool_list, self.settlement_name, self.path)
        structure_arrays=find_structure_obj.find_structures()
        
        self.initSettlement(structure_arrays,"test_Settlement")
        self.settlement.calculate_all_building_percentages()
        #self.settlement.buildPallete()
        self.settlement.find_all_levels() #write into module
        self.settlement.find_all_rooms()  #write into module
        self.settlement.find_room_pallete()
        self.settlement.build_dictionary()
        self.settlement.save_settlement()
        if screenshot == True:
            self.screenshot_all()

        self.settlement.print_dictionary()
        #print(self.settlement.pallete)


    #name=folder_name
    def load_settlement(self, name):
        sf_p=name+"/"+name+"_save_file.txt"
        np_p=name+"/"+name+".npy"
        self.path=name

        with open(sf_p) as json_file:
            save_file = json.load(json_file)
        #print(json.dumps(save_file, indent=2))
        settlement_dict=save_file["Settlement"]
        self.pallete=settlement_dict["pallete"]
        self.settlement=Settlement(name, np_p, settlement_dict["aesthetic"], path=self.path)
        struct_dict=settlement_dict["Structures"]
        struct_arr=[]
        for struct_key in struct_dict.keys():
            struct=struct_dict[struct_key]
            struct_obj=Structure(struct_key,settlement_dict["aesthetic"],struct["file"],self.pallete,self.path, function=struct["function"])
            self.aesthetic=settlement_dict["aesthetic"]
            level_dict=struct["Levels"]
            level_arr=[]
            for level_key in level_dict.keys():
                level_obj=Level(level_dict[level_key]["file"],level_key,level_dict[level_key]["offset"],self.aesthetic, self.path, self.pallete, function=level_dict[level_key]["function"])

                room_dict=level_dict[level_key]["Rooms"]
                for room_key in room_dict.keys():
                    
                    room_info=room_dict[room_key]
                    room_obj=Room(room_key, room_info["offset"],room_info["file"],self.aesthetic,self.path,function=room_info["function"])
                    #print(room_info)
                    level_obj.rooms.append(room_obj)
                struct_obj.levels.append(level_obj)
            struct_arr.append(struct_obj)
        self.settlement.structures=struct_arr
        self.print_settlement()
        self.screenshot_all()

    def print_settlement(self):
        print("Settlement: "+self.settlement.settlement_name)
        print("Buildings:")
        for struct in self.settlement.structures:
            print("|")
            print("|--> "+struct.building_name)
            for level in struct.levels:
                print("|  |")
                print("|  |-->"+level.level_name)
                for room in level.rooms:
                    print("|  |  |-->"+room.name)
        #print(s_str.keys())
    
    def screenshot_all(self):
        print(self.path)
        img_path=self.path+"/images" 
        os.makedirs(img_path, exist_ok = True)

        for structure in self.settlement.structures:
            out=img_path+"/"+structure.building_name
            ren.get_struct_img(structure.building_array, out)
            for level in structure.levels:
                #out=img_path+"/"+level.level_name
                for room in level.rooms:
                    out=img_path+"/"+".png"
                    ren.get_room_img(room.room_array, out)




#BlockEditor().load_settlement("House2")



BlockEditor().create_settlement("House2.npy", "House2")