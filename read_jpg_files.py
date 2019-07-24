import os
import numpy as np
from shutil import copyfile, move
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-op", "--operation", type=str, required=True, help="choose operation move or copy")
ap.add_argument("-i", "--input", type=str, required=True, help="path to input data")
ap.add_argument("-o", "--output", type=str, required=True, help="path to input data")
ap.add_argument("-n", "--number", type=int, required=True, help="number of data to be moved/copied")

args = vars(ap.parse_args())

file_list = []
# num_files = len(os.listdir(args["input"])) // 2

for file_name in os.listdir(args["input"]):
	if file_name.endswith(".xml"):
		file_list.append(file_name)
# end loop

file_list = np.array(file_list)

#shuffle the data
np.random.shuffle(file_list)

print("Total files: ", len(file_list))
print("Start Moving Data...")

for i,  file_name in enumerate(file_list):
	if i == args["number"]:	
		break
	else:
		print(file_name)
		if args["operation"] == "copy":
			copyfile(os.path.join(args["input"], file_name), args["output"] + file_name)
			copyfile(os.path.join(args["input"], file_name[:-4] + ".jpg"), args["output"] + file_name[:-4] + ".jpg")
		elif args["operation"] == "move":
			move(os.path.join(args["input"], file_name), args["output"] + file_name)
			move(os.path.join(args["input"], file_name[:-4] + ".jpg"), args["output"] + file_name[:-4] + ".jpg")

print("[INFO] OPERATION DONE!")