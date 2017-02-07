from flask import Flask, flash, redirect, render_template, request, session, abort
import os


app=Flask(__name__)

@app.route('/')
def  main():

	return render_template('index.html')

@app.route('/find', methods=['POST'])
def  find():
	c= {'a': 'apple', 'c': 'cat', 'b': 'box', 'e': 'elephant', 'd': 'dog'}


	v=str(request.form['key'])
	age='20'
	nums=[10,20,30,11,22,33,44,77,99,333,2222,44444,666]
	return  render_template('response.html', age=age , nums=nums , v=v, c=c)



if __name__ == '__main__':
	app.run(host="0.0.0.0" , port=8080, debug=True)