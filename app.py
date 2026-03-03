from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify({
		"message": "My first API is running!",
		"status": "success"
	})
@app.route('/joke')
def joke():
	return jsonify({
		"joke": "Why do programmers prefer dark mode? Because light attracts bugs."
	})

@app.route('/hello/<name>')
def hello(name):
	return jsonify({'message': f"Hello {name}!"})

import math
@app.route('/number/<int:num>')
def number_stats(num):
	def is_prime(n):
		if n < 2:
			return False
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True
	
	return jsonify({
		"number": num,
		"is_even":num % 2 == 0,
		"is_prime": is_prime(num),
		"squared": num ** 2,
		"square_root": round(math.sqrt(num), 2),
		"fahrenheit_to_celsius": round((num -32) * 5/9, 2)
	})

if __name__ == '__maine__':
	app.run(host='0.0.0.0', debug=True)

