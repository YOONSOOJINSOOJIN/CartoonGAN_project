# _*_ coding: utf-8 _*_
import os
from flask import Flask, render_template, request, redirect
from flask import url_for, flash, redirect
from werkzeug.utils import secure_filename
#import tensorflow as tf
#import test

app = Flask(__name__)
app.secret_key = 'random string'

checkpoint_dir = "model/generator_Hayao_weight"
test_dir = "static/image"
style_name = "Hayao"

@app.route("/", methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/cartoon")
def cartoon():
	return render_template('photo.html')

# @app.route('/upload_done', methods = ['POST'])
# def upload_done():
# 	upload_files = request.files['file']
# 	upload_files.save('static/img/{}.jpg'.format(1))
# 	return redirect(url_for('cartoon'))

@app.route("/upload_done", methods = ['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		if request.files['file'].filename == '':
			flash('파일이 없습니다. 파일을 제출하세요!')
			return redirect(url_for('cartoon'))
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save("static/image/{}".format(filename))
		return redirect(url_for('uploaded_file', filename = filename))

@app.route('/upload_done/<filename>')
def uploaded_file(filename):
	photo = f"image/{filename}"
	return render_template('photo.html', photo = photo)

@app.route('/cartoonize/<filename>', methods = ['GET', 'POST'])
def cartoonize():
	cartoon = test.test(checkpoint_dir, test_dir, style_name)
	cartoon_photo = f"results/Hayao/{filename}"
	return render_template('photo.html', photo = cartoon_photo)







if __name__ == '__main__':
	app.run(debug = True)