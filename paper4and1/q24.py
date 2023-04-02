'''24. Write a python script to copy files from a directory D1 based on timestamp(current_date)
to another directory D2 and delete the source directory D1. Whenever the script is called
this program must run.
'''


import shutil

from datetime import datetime
# Set destination of directories
source_dir = 'C:\\Users\\hp\\Desktop\\des1'
destination_dir = 'C:\\Users\\hp\\Desktop\\des2'

t=datetime.now()
now=t.timestamp()

# Copy files from source directory to destination directory
shutil.copytree(source_dir, destination_dir,dirs_exist_ok=True)
print('files are copied at : ',datetime.now())
print('files are copied at : ',now)
# Remove source directory
shutil.rmtree('C:\\Users\\hp\\Desktop\\des1')
