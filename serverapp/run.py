from flask import Flask, request, url_for
from flask.ext.cors import CORS
import urllib2
import subprocess
import os
app = Flask(__name__)
CORS(app)

MODEL_DIR = "/Users/jerryliu/Programming/deep_learning/neuraltalk2/"

@app.route('/')
def hello():
	return "9+10=21"

@app.route('/process', methods=['GET'])
def process():
	imgurl = request.args['imgurl']
	ext = os.path.splitext(imgurl)[1]
	ext = ext.lower()
	if ext != ".jpg" and ext != ".png":
		return "Error: invalid url"
	imgfile = urllib2.urlopen(imgurl)
	with open('tmp/cur_img' + ext, 'wb') as output: 
		output.write(imgfile.read())

	# result = subprocess.check_output(["DATA_ROOT=" + MODEL_DIR, "th", os.path.join(MODEL_DIR, "eval_mod.lua"), 
	# 	"-gpuid", "-1", "-model", os.path.join(MODEL_DIR, "checkpoints/model_id1-501-1448236541.t7_cpu.t7"),
	# 	"-image_folder", "tmp/", "-num_images", "1"])

	cmd = "DATA_ROOT=" + MODEL_DIR + " th " + os.path.join(MODEL_DIR, "eval_mod.lua") + \
		" -gpuid -1 -model " + os.path.join(MODEL_DIR, "checkpoints/model_id1-501-1448236541.t7_cpu.t7") + " -image_folder " + \
		"tmp/ -num_images 1"

	result = subprocess.check_output(cmd, shell=True)
	print(result)
	return result

if __name__ == "__main__":
	app.run()
