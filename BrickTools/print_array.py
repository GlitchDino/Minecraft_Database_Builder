

class printArray:
    def __init__(self, array):
        self.array=array
        self.max_y=len(array)
        self.max_z=len(array[0])
        self.max_x=len(array[0][0])
        self.print_arr()

    def print_arr(self):
        for y in range(0, self.max_y):
            print("Level "+str(y)+":")
            for z in range(0, self.max_z):
                print_string=""
                for x in range(0, self.max_x):
                    block_str=self.array[y][z][x][0]
                    if(block_str=="dirt" or block_str== "grass_block"):
                        print_string=print_string+"D"
                    elif(block_str=="air"):
                        print_string=print_string+"."
                    else:
                        print_string=print_string+block_str[:1]
                print(print_string)