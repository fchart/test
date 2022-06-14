import shutil, os, glob

fchart_path = 'D:/fChartThonny6_3.9AI'

dest_dir = "/WinPython/python-3.9.8.amd64/Lib/site-packages/face_recognition_models/models"
for file in glob.glob(os.getcwd() + "/*.dat"):
    print(file)
    shutil.copy(file, fchart_path + dest_dir)
