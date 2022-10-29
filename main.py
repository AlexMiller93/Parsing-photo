import glob
import shutil
import os


# source folder
data_folder = ""

# dest folder
years_dir = data_folder + r'\\Photos by years'


def find_years(directory: str): 
    """function find names of years 
    inside jpg file names in folder

    Args:
        directory (_type_): folder with jpg files

    Returns:
        _type_: unique years names in folder
    """
    list_years = set()
    for jpg_file in glob.iglob(os.path.join(directory, "*.jpg")):
        list_years.add(jpg_file.split('\\')[-1][4:8])
    list_years = list(list_years)
    return list_years


def create_years_dirs(directory: str, list: list):
    """creates new folders from one list in certain folder

    Args:
        directory (_type_): folder where should create a new dirs
        years (_type_): list of names future dirs
    """
    for item in list:
        path = os.path.join(directory, item)
        if os.path.exists(path) == False:
            os.mkdir(path, mode=0o777)
        else:
            pass


def copy_files_to_years(directory: str, folder: str, list: list):
    """copy files to years dirs according file names

    Args:
        directory (_type_): folder with jpg files
        folder(_type_): folder with 'years' dirs
        list (_type_): list of years based on file names
    """
    for jpg_file in glob.iglob(os.path.join(directory, "*.jpg")):
        for item in list:
            if jpg_file.split('\\')[-1][4:8] == item:
                shutil.copy(jpg_file, os.path.join(folder + '/' + item))

if __name__ == '__main__':
    # list of unique years from file names
    years = find_years(data_folder)
    create_years_dirs(years_dir, years)
    copy_files_to_years(data_folder, years_dir, years)



