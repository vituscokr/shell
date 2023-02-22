from pathlib import Path 
import os 
import shutil 

project_name = "project_name"

source_dir = ""
target_dir_path = f"{project_name}/assets"
target_dirs = [
   
    f"{target_dir_path}/images/",
    f"{target_dir_path}/images/2.0x/",
    f"{target_dir_path}/images/3.0x/",
]

for file in Path(source_dir ).glob("*.png"):
    print(file)

index = 0 
source_file_names = [] 

file_list = os.listdir(source_dir)
for file in file_list:
    extension = file.split('.')[1]
    print(extension)
    if extension == "png":

        file_name = file.split('.')[0]
        d_file_name = file_name.replace(' ', '_')
        d_file_name = d_file_name.replace('=', '_')
        d_file_name = d_file_name.replace('@2x', '')
        d_file_name = d_file_name.replace('@3x', '')
        if index == 0: 
            dest_file_name = d_file_name.lower() + ".png"

        source_file_name = file_name +".png"
        source_file_names.append(source_file_name)
        index = index + 1 
dests = [] 
for (index, source_file_name)  in enumerate(source_file_names): 
    source = source_dir + source_file_name

    if "@2x" in source_file_name: 
        dest = target_dirs[1] + dest_file_name
    elif "@3x" in source_file_name :
        dest = target_dirs[2] + dest_file_name
    else: 
        dest = target_dirs[0] + dest_file_name
    print(source)
    print(dest) 

    dests.append(dest) 
    shutil.move(source, dest )


for de in dests: 
    print(de)
    filesize =  os.path.getsize(de)
    print(filesize) 
# import shutil
# filename = 'test.txt'
# src = '/home/banana/'
# dir = '/home/banana/txt/'
# shutil.move(src + filename, dir + filename)
