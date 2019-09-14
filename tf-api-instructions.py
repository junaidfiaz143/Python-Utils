import os, random

path = "C:/Users/junaid/Desktop/new data/train"
lst = []
num_files = len(os.listdir(path))//2
for _ in range(0, num_files):
	file_name = random.choice(os.listdir(path))
	print(file_name)
	lst.append(file_name)

print("Total files: ", len(lst))

# os.system('cls')

# 1. (download + install) git to downlad repositories
# 2. setup repo
# 3. install dependencies (protobuf + requirements.txt)
# 4. run command "protoc object_detection/protos/*.proto --python_out=." from research directory
# 5. set environment paths "<given-below>"
# 6. download model using "wget <model-link>"
# 7. (build + install) setup.py
# 8. download dataset using youtube-dl "<gdrive-data-link>"
# 9. create csv files from data by execute command "python xml_to_csv.py" from object_detection directory
# 10. update (.config + labelmap.pbtxt + generate_tfrecord.py) files according to the classes
# 11. create record files by running these 2 commands "<given-below>" from object_detection directory
# 12. run training command "<given-below>"
# 13. install pycocotools, command is given below "<given-below>"
# 14. update (eval_util.py:[170, 79] + visualization_utils.py:[719])
# 15. add 'metrics_set: "coco_detection_metrics"' in .config file
# 16. run evaluation command "<given-below>"

# conda install -c anaconda protobuf

# DEPENDENCIES in REQUIREMENTS.txt 
# tensorflow-gpu
# argparse
# pillow
# lxml
# Cython
# contextlib2
# jupyter
# matplotlib
# pandas
# opencv-python
# youtube-dl

# GENERATE train.record
# python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record

# GENERATE test.record
# python generate_tfrecord.py --csv_input=images/test_labels.csv  --image_dir=images/test --output_path=test.record

# TRAINING / EVALUATION
# python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_resnet_v2_atrous_coco.config
# python eval.py --logtostderr --pipeline_config_path=training/faster_rcnn_inception_resnet_v2_atrous_coco.config --checkpoint_dir=training/ --eval_dir=eval/

# INSTALL PYCOCOTOOLS
# pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"

# \/---! PATHS !---\/
# WINDOWS
# set PYTHONPATH=C:\Users\junaid\anaconda3\envs\tensorflow-obj\models;C:\Users\junaid\anaconda3\envs\tensorflow-obj\models\research;C:\Users\junaid\anaconda3\envs\tensorflow-obj\models\research\slim

# LINUX
# export PYTHONPATH="$PATH:/home/junaid/anaconda3/envs/tensorflow-objj/models:/home/junaid/anaconda3/envs/tensorflow-objj/models/research:/home/junaid/anaconda3/envs/tensorflow-objj/models/research/slim"
# export PYTHONPATH="$PYTHONPATH:pwd:pwd/slim" - from object-detection folder
# /\---! PATHS !---/\