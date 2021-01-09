import argparse
import subprocess
import os
import cv2
import numpy as np

parser = argparse.ArgumentParser()
# parser.add_argument("-path",help="path to the scenario XML file", default="./example/CrossStreet.xml")
parser.add_argument("path",help="path to the scenario XML file")
# parser.add_argeument("r", "--resolution", default=0.4, type=float)
# args = parser.parse_args()

# scene_name = args.path.split('/')[-1][:-4] 
scene_name = '8159'
cwd = os.getcwd()
input_dir = cwd + "/example/{}.xml".format(scene_name)
output_dir = cwd + "/output/" + scene_name 

# TODO: resize too large map image
# file_name = cwd + "/example/{}.png".format(scene_name)
# img = cv2.imread(file_name)
# x = int(0.5*img.shape[0])
# y = int(0.5*img.shape[1])
# imgout = cv2.resize(img,(135,240), interpolation = cv2.INTER_NEAREST)
# kernel = np.ones((3, 3), dtype=np.uint8)
# imgout = cv2.erode(imgout, kernel, 1) 
# cv2.imwrite(file_name,imgout)

# cv2.imshow('out',imgout)
# cv2.waitKey(0)
# cv2.destroyWindow()


print("input_dir: ", input_dir)
print("output_dir: ", output_dir)

os.chdir("MengeFileGenerator")
os.system("python menge_generator.py {} -o {} -r {}".format(
    input_dir, output_dir, 0.15
))
os.chdir(cwd)

os.system("python world_generator.py --scene_name {} --plugin".format(
    scene_name
))

os.system("cp -r ./output/{0} ~/Documents/Menge/examples/scene/".format(scene_name))
os.system("cp ./output/{0}/{0}.world ~/Documents/crowdsim_ws/src/menge_gazebo/menge_gazebo_worlds/worlds/{0}.world".format(scene_name))




