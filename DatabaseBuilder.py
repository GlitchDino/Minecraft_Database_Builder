from BrickTools import Parser, Pallete, BrickEditor
from shutil import make_archive, rmtree, unpack_archive
#import BrickTools.find_structures
#from BrickTools import findStructures
import h5py
import ast
import os

#add http_request part
#compress folder
#set function 



def create(name, files, aesthetic, x, y,z, set_function=True):
    # Path to entities folder
    # data are pictures, .npy files, .json output
    compress=True
    aesth_data_path="Bricks_DB/"+aesthetic+"_data/"
    #create aeshtetic entity folder if it doesn't exist
    if(os.path.exists(aesth_data_path)==False):
        os.mkdir(aesth_data_path)
    #create entity folder
    count=get_count()
    stl_name_inc=name+"."+str(count)
    entity_path=aesth_data_path+stl_name_inc+"_data/"
    os.mkdir(entity_path)
    #pull json file with http

    #json_file=name+".txt"
    
    
    #returns all unique blocks in Settlement, save Settlement as .npy file under settlement_arr_p
    settlement_arr_p=entity_path+name+".npy"
    
    parser=Parser(files, settlement_arr_p)
    all_blocks=parser.block_ids
    block_count=parser.block_count
    
    #parse blocks, returns pallete (all blocks in Settlement)
    
    pallete, trash=create_pallete(all_blocks)
    db, stl=create_settlement_db(stl_name_inc, aesthetic, pallete)
    stl.attrs["file"]=settlement_arr_p
    stl.attrs["total_blocks"]=block_count
    editor=BrickEditor()
    editor.create_world(stl, entity_path, trash, render_mode="string")
    if(set_function==True):
        with open('function_types.txt','r') as f:
            r=f.read()
            room_functions=ast.literal_eval(r)
        label(stl, room_functions)
    
    if(compress==True):
        zip_file=zip(entity_path)
        stl.attrs["zip_file"]=zip_file
    stl.attrs["cords"]=(x, y, z)
    """just save dict as string, >>>  ast.literal_eval(s) for dict"""
def zip(entity_path):

    make_archive(entity_path, 'zip', entity_path)
    rmtree(entity_path)
    zip_file=entity_path[:-1]
    zip_file=zip_file+".zip"
    return zip_file
def label(stl, room_functions):
    print(stl.name)
    structures_group=stl["Structures"]
    for s_key in structures_group.keys():
        struct=structures_group[s_key]
        print(s_key)
        all_rooms=[]
        for l_key in struct.keys():
            lvl=struct[l_key]
            lvl_func=lvl.attrs["function"]
            
            if(lvl_func!="multi_top"):
                print(l_key)
                for r_key in lvl.keys():
                    print(r_key)
                    room=lvl[r_key]
                    print_str=room.attrs["print_string"]
                    print(print_str)
                    print("Aesthetic blocks:")
                    print(room.attrs["aesthetic_pallete"])
                    print("Function blocks:")
                    print(room.attrs["function_pallete"])
                    res=label_room(room_functions)
                    room.attrs["function"]=res
                    all_rooms.append(res)
            else:
                print("exluding roof: "+l_key)
        print(struct.attrs["print_string"])
        print("Room functions:")
        print(all_rooms)
        res=label_struct()
        struct.attrs["function"]=res
def label_struct():
        structure_functions=["tiny_house", "house", "inn", "forge", "castle", "hospital", "shop"]
        while(True):
            tag=input("Structure Function>")
            if(tag=="th"):
                return "tiny_house"
            elif(tag=="h"):
                return "house"
            elif(tag=="m"):
                return "mansion"
            elif(tag not in structure_functions):
                print("Room function "+str(tag)+" has not been used yet. Do you want to add it to room functions? (Y/N)")
                yn=input(">")
                if(yn=="Y" or yn=="y"):
                    structure_functions.append(tag)
                    return tag
                else:
                    print("Try again")
            else:
                return tag
def label_room(room_functions):
        while(True):
            tag=input("Room Function>")
            if(tag=="bd"):
                return "bed_room"
            elif(tag=="e"):
                return "empty"
            elif(tag not in room_functions):
                print("Room function "+str(tag)+" has not been used yet. Do you want to add it to room functions? (Y/N)")
                yn=input(">")
                if(yn=="Y" or yn=="y"):
                    room_functions.append(tag)
                    return tag
                else:
                    print("Try again")
            else:
                return tag
def create_settlement_db(name, aesthetic, pallete):
    #connect to database, create if database doesnt exist 
    db_str="Bricks_DB/"+aesthetic+".hdf5"
    db = h5py.File(db_str,'a')

    stl=db.create_group(name) # create group for settlement
    #create "settlement entities" folder
    stl.attrs["pallete"]=str(pallete)
    print(stl.attrs)
    #stl.create_dataset('pallete', data=pallete)
    return db, stl
def inc():
    with open('log.txt','r') as f:
        count = int(f.read())
        count+=1 
    with open('log.txt','w') as f:
        f.write(str(count))
    return count

def create_pallete(pallete):
    pallete_tag_dict={}
    magic = Pallete().get_all_magic()
    trash = Pallete().get_all_trash()
    structure = Pallete().get_all_structure()
    aesthetic = Pallete().get_all_aesthetic()
    function = Pallete().get_all_function()
    trash_list=[]
    for id in pallete:
        if id in magic:
            val=pallete_prompt(id)
            if(val=="trash"):
                trash_list.append(id)
            pallete_tag_dict[id]=val
        elif id in trash:
            pallete_tag_dict[id]="trash"
            trash_list.append(id)
        elif id in structure:
            pallete_tag_dict[id]="structure"
        elif id in aesthetic:
            pallete_tag_dict[id]="aesthetic"
        elif id in function:
            pallete_tag_dict[id]="function"
    return pallete_tag_dict, trash_list


def pallete_prompt(id, assume_trash=False):
    if(assume_trash==True):
        return "trash"
    print('Acceptable input:\ns="structure"\na="aesthetic"\nf="function"\nt="trash"')
    print("Select block type: "+id)
    
    while(True):
        tag=input(">")
        if(tag=="s"):
            return "structure"
        elif(tag=="a"):
            return "aesthetic"
        elif(tag=="f"):
            return "function"
        elif(tag=="t"):
            return "trash"
        else:
            print("invalid input")
def get_count():
    with open('log.txt','r') as f:
        count = int(f.read())
        count+=1 
    with open('log.txt','w') as f:
        f.write(str(count))
    return count

create("Example_Settlement",["Example_Settlement.txt"], "ExampleAesthetic", 0,0,0)
#create("MEDIVAL1",["MEDIVAL1_p1.txt", "MEDIVAL1_p2.txt", "MEDIVAL1_p3.txt"], "medival",0,0,0)