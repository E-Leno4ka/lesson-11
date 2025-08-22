import shutil
# высокоуровненвые операции для работы с файлами

shutil.copy("new.txt", "new2.py")

usage = shutil.disk_usage("c:\\")
print(usage)
print(f'{usage.total / (1024 ** 3) :.1f}')


