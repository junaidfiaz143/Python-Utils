dep_list = ["tensorflow", "argparse", "pillow", "lxml", "Cython", "contextlib2", "jupyter", "matplotlib", "pandas", "opencv-python", "youtube-dl"]

dep_file = open("requirements.txt","w+")

for dep in dep_list:
	dep_file.write(dep + "\n")

dep_file.close()