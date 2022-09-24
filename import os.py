import os 
os.chdir('/Users/Acer/work2/')
os.mkdir("mytask")
os.chdir('/Users/Acer/work2/mytask/')
print(os.getcwd())
os.chdir('/Users/Acer/work2/')
os.rmdir('/Users/Acer/work2/mytask')
os.listdir("/Users/Acer/work2/")

