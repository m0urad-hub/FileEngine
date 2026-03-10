from pathlib import Path
import time
def info(file):
    name = file.stem
    size = file.stat().st_size # size in bytes
    ctime = time.ctime(file.stat().st_ctime) # creation time
    mtime = time.ctime(file.stat().st_mtime) # last modified time

    print(f"Name: {name}")
    print(f"Extension: {extension}")
    print(f"Size: {size} bytes")
    print(f"Created: {ctime}")
    print(f"Modified: {mtime}")
    print("-" * 30)
path=input("give")
folder = Path(path)
print(folder)
type=input("give type of files")
stat_size =int(input("give minim size "))
for file in folder.rglob("*"): 
    if file.is_file():
        extension = file.suffix
        size = file.stat().st_size
        if stat_size<size :
            info(file)
        #if extension==type :
            #info(file)
        

        

        
    