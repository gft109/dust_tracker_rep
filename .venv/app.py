from flask import Flask, render_template, request, jsonify, json, redirect, make_response, send_file

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
@app.route('/home')
def login():
    return render_template('home.html')
    

@app.route("/emit")
def home():
    return render_template('emit.html')

@app.route("/dust")
def dust():
    return render_template('dust.html')

@app.route("/aboutus")
def about():
    return render_template('aboutus.html')

if __name__== "__main__":
    app.run(debug=True)