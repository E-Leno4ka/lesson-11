import os
#print(os.name)

# создание и удаление папки
#os.mkdir("new_folder")


#os.rename("new.txt", "old.txt")
#if os.path.exists("old.txt"):
#    print("File exists")
#    os.remove("old.txt")
#else:
#    print("File does not exist")
#    open("old.txt", "w").close()


for _, _, filenames in os.walk("."):
    for filename in filenames:        
        print(filename, end=", ") if filename.endswith(".py") else ...