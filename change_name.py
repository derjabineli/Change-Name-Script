import os
import sys

os.chdir(f'{sys.argv[1]}')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if f_name == '.DS_Store':
        continue

    new_name = f'{sys.argv[2]}-{f_name}{f_ext}'
    
    os.rename(f, new_name)