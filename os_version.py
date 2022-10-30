import os
import shutil

# working directory
folder = ''

# create a new folder where will be copied photo files
path = os.path.join(folder, 'Photos')
if not os.path.exists(path):
    os.mkdir(path, mode=0o777)

# loop through files in new folder and parse name and extension 
for f in os.listdir(folder):
    if f.endswith('.jpg'):
        f_name, f_ext = os.path.splitext(f)

    # parse year and month from filename
    year, month = f_name[4:8], f_name[8:10]

    # new path to year folder
    year_path = os.path.join(path, year)
    if not os.path.exists(year_path):
        os.mkdir(year_path)

    # new path to month folder
    month_path = os.path.join(year_path, month)
    if not os.path.exists(month_path):
        os.mkdir(month_path)
    
    # create a new file name
    new_name = f'{year} - {month}{f_ext}'
    file_path = os.path.join(month_path, new_name)
    
    # copy files and rename in month folder 
    shutil.copy2(os.path.join(folder, f), file_path)

