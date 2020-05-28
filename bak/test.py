import os
name = "木火应"
filepath = "C:\\userfiles\\" + name + "\\"
if not os.path.exists("C:\\userfiles"):
    os.mkdir("C:\\userfiles")
if not os.path.exists(filepath):
    os.mkdir(filepath)
print(os.path.exists(filepath))