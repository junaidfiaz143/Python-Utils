import os
import argparse

# protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

def generate_requirements_txt():
	dep_list = ["tensorflow-gpu", "argparse", "pillow", "lxml", "Cython", "contextlib2", "jupyter", "matplotlib", "pandas", "opencv-python", "youtube-dl"]
	dep_file = open("requirements.txt","w+")

	for dep in dep_list:
		dep_file.write(dep + "\n")

	dep_file.close()

ap = argparse.ArgumentParser(description="Tensorflow-Object-Detection : UTILS")

ap.add_argument("-ins", "--install", required=False, type=str, default="no", help="'requirements'-'pycocotools'-'protobuf'")
ap.add_argument("-op", "--operation", required=False, type=str, default="no",  help="'train'-'eval'-'tensorboard.train'-'tensorboard.eval'")
ap.add_argument("-gen", "--generate", required=False, type=str, default="no",  help="'train.record'-'test.record'-'labels.csv'-'req.txt' generate .record/.csv/.txt files")

args = vars(ap.parse_args())

conda_env_name = "tensorflow-obj"
pc_username = "junaid"

cmd = {
	"path": "C:/Users/"+pc_username+"/anaconda3/envs/"+conda_env_name+"/models;C:/Users/"+pc_username+"/anaconda3/envs/"+conda_env_name+"/models/research;C:/Users/"+pc_username+"/anaconda3/envs/"+conda_env_name+"/models/research/slim",
	"train": "python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_resnet_v2_atrous_coco.config",
	"eval": "python eval.py --logtostderr --pipeline_config_path=training/faster_rcnn_inception_resnet_v2_atrous_coco.config --checkpoint_dir=training/ --eval_dir=eval/",
	"requirements": "pip install -r requirements.txt",
	"pycocotools": 'pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"',
	"protobuf": "conda install -c anaconda protobuf",
	"labels.csv": "python xml_to_csv.py",
	"train.record": "python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record",
	"test.record": "python generate_tfrecord.py --csv_input=images/test_labels.csv  --image_dir=images/test --output_path=test.record",
	"tensorboard.train": "tensorboard --logdir=training/",
	"tensorboard.eval": "tensorboard --logdir=eval/"
}

if args["install"] != "no":
	os.system(cmd[args["install"]])

if args["operation"] != "no":
	os.environ["PYTHONPATH"] = cmd["path"]
	os.system(cmd[args["operation"]])

if args["generate"] != "no":
	if args["generate"] == "req.txt":
		generate_requirements_txt()
		print("requirements.txt created successfully!")
	else:
		os.system(cmd[args["generate"]])