from csv import reader
from os import walk 
import pygame
from natsort import *

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
# import_csv_layout()

def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        # natsorted(img_files)
        for image in natsorted(img_files):
            full_path = f"{path}/{image}"
            print(image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
# import_folder()
# import_folder('../graphics/Grass')