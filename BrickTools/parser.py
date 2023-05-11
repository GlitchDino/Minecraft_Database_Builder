import numpy
import json

class Block:
    def __init__(self, id, x, y, z, state, data):
      self.id=id
      self.x=x
      self.y=y
      self.z=z
      self.state=state
      self.data=data


class Parser():
    def __init__(self, input, output, verbose=False):
        self.input=input
        self.output=output
        self.verbose=verbose
        self.block_count=0
        self.parse()
    def parse_file(self):
            blocks_array=[]
            id_array=[] #list of all unique ids for pallete searching
            for file in self.input:
                with open(file) as json_file:
                    data = json.load(json_file)
                for block in data:
                    id=block['id'].split("minecraft:")[1]
                    if(id!='air'):
                        self.block_count+=1
                    if id not in id_array:
                        id_array.append(id)
                    x=block['x']
                    y=block['y']
                    z=block['z']
                    state=block['state']
                    data=block['data']
                    if(len(data)==2):
                        data=None
                    if(not state):
                        state=None
                    if(self.verbose==True):
                        print(block)
                        print("ID: "+id)
                        print("x: "+str(x))
                        print("y: "+str(y))
                        print("z: "+str(z))
                        print("State:"+str(state))
                        print("Data: "+str(data))
                    blocks_array.append(Block(id, x, y, z, state, data))
            self.blocks=blocks_array 
            self.block_ids=id_array

    def init_map_array(self):
        lowest_x=self.blocks[0].x
        lowest_y=self.blocks[0].y
        lowest_z=self.blocks[0].z
        highest_x=self.blocks[0].x
        highest_y=self.blocks[0].y
        highest_z=self.blocks[0].z
        for item in self.blocks:
            if(lowest_x>item.x):
                lowest_x=item.x
            elif(highest_x<item.x):
                highest_x=item.x

            if(lowest_y>item.y):
                lowest_y=item.y
            elif(highest_y<item.y):
                highest_y=item.y

            if(lowest_z>item.z):
                lowest_z=item.z
            elif(highest_z<item.z):
                highest_z=item.z

        #maybe plus 1 for 0 blocks
        x_area=highest_x-lowest_x
        y_area=highest_y-lowest_y
        z_area=highest_z-lowest_z
        
        #find area of array
        for item in self.blocks:
            item.x=item.x-lowest_x
            item.y=item.y-lowest_y
            item.z=item.z-lowest_z

        array=numpy.empty((y_area+1, z_area+1, x_area+1), dtype=object)

        #populate array with block data so numpy can save it
        for item in self.blocks:
            array[item.y][item.z][item.x]=(item.id, item.state, item.data)


        numpy.save(self.output, array)

    def parse(self):
        if(self.verbose==True):
            print("Running parser...") 
            self.parse_file()
            print("Creating map...")
            self.init_map_array()
            print("Parser done.\nOutput saved to: "+self.output)
            
        else:
            self.parse_file()
            self.init_map_array() 