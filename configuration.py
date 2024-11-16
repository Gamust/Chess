import os
import platform

def get_pieces_directory():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pieces_dir = os.path.join(base_dir, "Pieces")
    return pieces_dir

def get_image_path(image_name):
    pieces_dir = get_pieces_directory()
    image_path = os.path.join(pieces_dir, image_name)
    return image_path

