import glob
import os
import shutil
import time
from pathlib import Path

# Enter Dirname here
dir_name = ''
debug = True

list_of_dirs = filter(os.path.isdir,
                      glob.glob(dir_name + '/*'))

for folder in list(list_of_dirs):

    list_of_files = filter(os.path.isfile,
                           glob.glob(folder + '/*.mp4'))

    list_of_files = sorted(list_of_files,
                           key=os.path.getmtime)

    for file_path in list_of_files:
        date_name = time.strftime('%m-%Y', time.gmtime(os.path.getmtime(file_path)))

        new_folder = "{0}/{1}".format(folder, date_name)
        new_filename = "{0}/{1}".format(new_folder, os.path.basename(file_path))
        Path(new_folder).mkdir(parents=True, exist_ok=True)

        if debug:
            print(file_path, ' -->', new_filename)
        else:
            shutil.move(file_path, new_filename)

