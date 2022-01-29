import shutil
import sys
from pathlib import Path
from typing import Union

class orgenizer():
    def __init__(self):
        
        self.extention = {
            '.png' : 'image',
            '.csv' : 'data',
            '.json' : 'data',
            '.pdf' : 'document',
            '.txt' : 'document',
            '.zip' : 'document',
        }
    
    def orgenize_files(self , directory:Union[str , Path]):

        directory = Path(directory)
        if not directory.exists():
            raise FileNotFoundError(f'{directory} dose not exsist')

        file_extensions = []
        
        for path in directory.iterdir():
            
            # ignore directories
            if path.is_dir():
                continue
            
            # ignore hiden files
            if path.name.startswith('.'):
                continue
            
            # collect file path suffix 
            file_extensions.append(path.suffix)
            
            # move
            if path.suffix not in self.extention:
                dest_dir = directory / 'other'
            else:
                dest_dir = directory / self.extention[path.suffix]
            
            dest_dir.mkdir(exist_ok = True)
            print(f'{path.suffix} -----------> {dest_dir}')
            shutil.move(str(path) , str(dest_dir))

    
if __name__ == "__main__":
    orgenize_path = orgenizer()
    orgenize_path.orgenize_files(sys.argv[1])
    print('Done...!')
