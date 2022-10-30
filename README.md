# Parsing-photo
Script for parsing photo and copy files in folders with years according their file names

You should take some photo files in format like IMG_202202**.jpg, where 2022 is year and 02 is a month.

***
I wrote 2 versions of code how reach almost same results.

In file main.py there are 3 functions to parse and copy your photos. Function 'find_years' accept folder where are the files and return list of years from file names. Function 'create_years_dirs' creates a new dirs according with list of years and function 'copy_files_to_years' copies files from data_folder to folder with 'years' dirs.

You get a new folders with relevant year from file names and copied files from indicated folder.

***
I write another script which became more simple than first one. 

In file os.version.py I wrote script with same task much easier and readable.
I use one for loop to iterate files in folder, parse year and month from filename and make new folders with relevant name of year and month. One feature I've improved is to rename files. 
After all changes you get a new folders with name year and month accordingly, copied and renamed files. 


