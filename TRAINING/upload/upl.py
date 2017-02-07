import os
import flask
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

upl= Flask(__name__, static_folder='dwnld')


upl.config['UPLOAD_FOLDER']=''
upl.config['ALLOWED_EXTENSIONS'] = set(['txt','png','jpg','jpeg', 'pdf' , 'gif' ,'csv'])
def  allowed_file(filename):
	return '.' in filename and \
	   filename.rsplit('.',1)[1] in upl.config['ALLOWED_EXTENSIONS']

@upl.route('/')
def index():

	
	return render_template('index.html')


@upl.route('/upload', methods=['POST'])
def upload():
	file=request.files['file']
	if file and allowed_file( file.filename):
		filename=secure_filename(file.filename)
		file.save(os.path.join(upl.config['UPLOAD_FOLDER'],filename))
		return redirect(url_for('uploaded_file', filename=filename))


@upl.route('/<filename>')
def uploaded_file(filename):
	return send_from_directory(upl.config['UPLOAD_FOLDER'], filename=filename)



@upl.route('/<filename>' , methods=['GET', 'POST'])
def download(filename):
	return send_from_directory(directory='dwnld', filename=filename)


if __name__ == '__main__' :
	upl.run(host='0.0.0.0', port=8088, debug=True)
