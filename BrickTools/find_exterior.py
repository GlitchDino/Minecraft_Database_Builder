
import numpy
from copy import copy, deepcopy
class findExterior:
    def __init__(self, np_arr, pallete):
        self.np_arr=np_arr
        self.pallete=pallete

    def find_exterior(self):
        ext=[]
        #printy.printArr(np_arr)
        for y in range(0, len(self.np_arr)):
            #print("Y"+str(y))
            level=self.np_arr[y]
            sym_arr=self.build_str_arr(level, self.pallete)
            cords=self.get_ext_cords(sym_arr)
            ext_lvl=self.replace_cords(level, cords)
            ext.append(ext_lvl)
        ext=numpy.array(ext)
        return ext
    def replace_cords(self, level, cords):
        
        for z in range(0, len(level)):
            for x in range(0, len(level[0])):
                is_ext=False
                for cord in cords:
                    if(cord[0]-1==z and cord[1]-1==x):
                        #level[z][x]=
                        is_ext=True
                if(is_ext==False):   
                    level[z][x]=('air', None, None)
        return level
    def get_ext_cords(self, sym_arr):
        cords=[]
        for z in range(0, len(sym_arr)):
            for x in range(0, len(sym_arr[0])):
                sym=sym_arr[z][x]
                if(sym!='1'):
                    up=sym_arr[z+1][x]
                    down=sym_arr[z-1][x]
                    right=sym_arr[z][x+1]
                    left=sym_arr[z][x-1]
                    dir_list=[up, down, right, left]
                    if(sym=='X'):
                        up_left=sym_arr[z+1][x-1]
                        up_right=sym_arr[z+1][x+1]
                        down_left=sym_arr[z-1][x-1]
                        down_right=sym_arr[z-1][x+1]
                        dir_list.extend([up_left,up_right,down_left,down_right])
                        if '1' in dir_list:
                            cords.append((z,x))
                    elif(sym=="F" or sym=="A"):

                        if '1' in dir_list:
                            cords.append((z,x))
        return cords

    #Build 2D array of symbols
    def build_str_arr(self, level,pallete):
        sym_arr=numpy.full((len(level)+2, len(level[0])+2), "1",dtype=object)
        for z in range(0, len(level)):
            for x in range(0, len(level[0])):
                block=level[z][x]
                block_id=block[0]
                val=pallete[block_id]
                if(val=='structure'):
                    sym_arr[z+1][x+1]="X"
                elif(val=='aesthetic'):
                    sym_arr[z+1][x+1]="A"
                elif(val=='function'):
                    sym_arr[z+1][x+1]="F"
                else:
                    sym_arr[z+1][x+1]="."
        #fills array w exterior blocks
        found=False
        while(found==False):
            sym_arr, found = self.fill_arr(sym_arr, found)
        return sym_arr

    def fill_arr(self, sym_arr, found):
        found=True
        for z in range(0, len(sym_arr)):
            for x in range(0, len(sym_arr[0])):
                block_str=sym_arr[z][x]
                
                if(block_str=="."):
                    
                    up=sym_arr[z+1][x]
                    down=sym_arr[z-1][x]
                    right=sym_arr[z][x+1]
                    left=sym_arr[z][x-1]

                    adjecent_blocks=[up,down,right,left]
                    if "1" in adjecent_blocks:
                        sym_arr[z][x]='1'
                        found=False
        return sym_arr, found
