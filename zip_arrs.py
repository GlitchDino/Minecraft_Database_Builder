import h5py
import numpy as np

from shutil import make_archive, rmtree, unpack_archive


def zip_entitys(entity_path):
    
    dir = entity_path
    #zipfile.ZipFile(dir, "w")
    make_archive(dir, 'zip', dir)
    rmtree(dir)
    #add zip to settlement attributes
#zip_entitys("Bricks_DB/test_data/2_houses_0wools.448_data/")

def open_zip(entity_path):
    zip_file=entity_path[:-1]
    zip_file=zip_file+".zip"
    unpack_archive(zip_file, entity_path, format="zip")

open_zip("Bricks_DB/test_data/2_houses_0wools.448_data/")