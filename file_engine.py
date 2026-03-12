from pathlib import Path
import time
import sqlite3
import datetime 
conn = sqlite3.connect("file_engine_storage.db")
cursor = conn.cursor()
#pagma foreign_keys =on


cursor.execute("""create table if not exists file(
id_file integer primary key autoincrement,
path text unique,
lasts_updated datetime
)""")


def insert_file(cursor,path):
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    folder = Path(path)
    try :
        cursor.execute("insert into file (path,lasts_updated) values(?,?)",(path,date))
        conn.commit()
    except Exception as e:
        print(e)




cursor.execute("""create table if not exists info(
id_info integer primary key,
id_file integer ,
file_name text,
extension text,
size integer,
created_at datetime,
modified_at datetime,
foreign key(id_file) references file(id_file))   """)


def insert_info(cursor,folder_p):
    cursor.execute("select * from file ")
    data=cursor.fetchall()
    for column in data:
        if column[1]==folder_p :
            print(column[1]+"path already scanned last time at "+column[2],)
        else :
            f=Path(column[1])
            folder_id=column[0]
            for file in f.rglob("*"): 
                if file.is_file():
                    infos()
                    break
def infos():
    extension = file.suffix
    size = file.stat().st_size
    name = file.stem
    size = file.stat().st_size # size in bytes
    ctime = time.ctime(file.stat().st_ctime) # creation time
    mtime = time.ctime(file.stat().st_mtime) # last modified time
    cursor.execute("insert into info (file_name,extension,size,created_at,modified_at,id_file) values(?,?,?,?,?,?)",(name,extension,size,ctime,mtime,folder_id))
    print("all info of this folder scanned >>")

            

def main(cursor):
    action=("scan_folder/get_infos")
    while True :
        if action=="scan_folder":
            p=input("give path")
            cursor.execute("select * from file ")
            data=cursor.fetchall()
            for column in data:
                if column[1]==folder_p :
                    print(column[1]+"path already scanned last time at "+column[2],)
                else :
                    insert_file(cursor,p)
        elif action=="get_info" :
            p=input("give path")
            insert_info(cursor,p)
        elif action=="re_scan_folder":
            p=input("give path")
            cursor.execute("delete from file where path=?",(p,))
            insert_file(cursor,p)
        elif action=="exit":
            break
        else :
            print("unvalid syntaxe")
            
        
            
    


    
  


        

        

        
    