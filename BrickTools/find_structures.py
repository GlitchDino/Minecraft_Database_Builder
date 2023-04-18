#This finds houses by selecting any building with red wool in it
#returns list of numpy files 
import numpy
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

class findStructures:
    def __init__(self, struct, settlement_map, search_list, trash_list, entity_path, verbose=False):
        self.struct=struct
        self.settlement_map=settlement_map
        self.search_list=search_list
        self.entity_path=entity_path
        self.trash=trash_list#edit this to pallete list
        self.is_connected=[]
        self.houses=[]
        self.structures=[]
        self.building_count=0

    def wool(self):
        for search_item in self.search_list:
            self.is_connected.append(search_item)
            self.scan()

    def scan(self):
        houseArr=[]
        while self.is_connected:
            block=self.is_connected.pop(0)
            if(block.is_searched==False):
                houseArr.append(block)
                block.is_searched=True
                self.check_block(block)
        self.houses.append(houseArr)
        for cord in houseArr:
            if cord in self.search_list:
                self.search_list.remove(cord)

    def check_block(self, block):
        #check z
        if(block.z-1>=0):
            neighbor=self.settlement_map[block.y][block.z-1][block.x]
            if neighbor.type!="trash":
                neighbor.is_connected=True
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
                    
        if(block.z+1<self.max_z):
            neighbor=self.settlement_map[block.y][block.z+1][block.x]
            if neighbor.type!="trash":
                neighbor.is_connected=True,
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
        #check y
        if(block.y-1>=0):
            neighbor=self.settlement_map[block.y-1][block.z][block.x]
            if neighbor.type!="trash":
                neighbor.is_connected=True
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
        if(block.y+1<self.max_y):
            neighbor=self.settlement_map[block.y+1][block.z][block.x]
            if neighbor.type!="trash":
                neighbor.is_connected=True
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
        #Check x
        if(block.x-1>=0):
            neighbor=self.settlement_map[block.y][block.z][block.x-1]
            if neighbor.type!="trash":
                neighbor.is_connected=True
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
        if(block.x+1<self.max_z):
            neighbor=self.settlement_map[block.y][block.z][block.x+1]
            if neighbor.type!="trash":
                neighbor.is_connected=True
                if(neighbor.is_searched!=True):
                    self.is_connected.append(neighbor)
    #builds arrays of houses
    def buildStructArrays(self):
        for houseArr in self.houses:
            if(len(houseArr)>0):

                #find area of structure 
                b=houseArr[0]
                min_y, max_y=b.y, b.y
                min_z, max_z=b.z, b.z
                min_x, max_x=b.x, b.x
                for block in houseArr:
                    if(min_y>block.y):
                        min_y=block.y
                    if(max_y<block.y):
                        max_y=block.y

                    if(min_z>block.z):
                        min_z=block.z
                    if(max_z<block.z):
                        max_z=block.z

                    if(min_x>block.x):
                        min_x=block.x
                    if(max_x<block.x):
                        max_x=block.x

                for block in houseArr:
                    block.y=block.y-min_y
                    block.x=block.x-min_x
                    block.z=block.z-min_z
                max_y=max_y-min_y
                max_z=max_z-min_z
                max_x=max_x-min_x
                min_y=0
                min_x=0
                min_z=0
                structArr=numpy.empty((max_y+1, max_z+1, max_x+1), dtype=object)

                #fill structure array with the existing blocks
                for block in houseArr:
                    structArr[block.y][block.z][block.x]=block

                for y in range(0, len(structArr)):
                    for z in range(0, len(structArr[0])):
                        for x in range(0, len(structArr[0][0])):
                            block=structArr[y][z][x]
                            if(block==None):
                                structArr[y][z][x]=Block("air", x, y, z, None, None, "trash")

                self.saveStruct(structArr)

    def saveStruct(self, array):
        max_y=len(array)
        max_z=len(array[0])
        max_x=len(array[0][0])

        structure=numpy.empty((max_y, max_z, max_x), dtype=object)
        for y in range(0, max_y):
            for z in range(0, max_z):
                for x in range(0, max_x): 
                    block=array[y][z][x]
                    dat=(block.id, block.state, block.data, block.type)
                    structure[y][z][x]=dat
        save=self.entity_path+"Building"+str(self.building_count)+".npy"
        print("Saving Settlement Structure "+str(self.building_count)+" to "+save)
        self.building_count+=1
        #numpy.save(save, structure)
        self.structures.append(structure)

    def find_buildings(self):
        self.max_y=len(self.settlement_map)
        self.max_z=len(self.settlement_map[0])
        self.max_x=len(self.settlement_map[0][0])
        self.wool()
        self.buildStructArrays()
        return self.structures
    