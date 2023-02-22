from pathlib import Path 
import os 
import shutil 

# 마지막에 / 있음 
find_dir = "/"
filename = "cardname*.png" 

for file in Path(find_dir ).glob(filename):
    file_name = os.path.basename(file)
    print(file_name)

