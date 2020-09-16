import os
import shutil

def test_create_folders():
    directory = "C:\\Users\\mail\\Desktop\\test_sorted_photos"
    foldername = "test_folder"
    os.mkdir(directory)
    os.mkdir(os.path.join(directory, foldername))
    assert os.path.exists(os.path.join(directory, foldername))
    shutil.rmtree("C:\\Users\\mail\\Desktop\\test_sorted_photos")