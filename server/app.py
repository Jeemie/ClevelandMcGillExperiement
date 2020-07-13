from flask import Flask, request, send_from_directory, render_template
import os.path
import random
import string

app = Flask(__name__, static_url_path='')



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def submit():
    if(request.method == 'POST'):
        print("I got a submission")
        print("req" + str(request))
        fname = next_file_name()
        f = open(fname, "w")
        f.write(str(request.get_json()))
        return  "Succesful submission"
    return "NOTAVALIDPATH"


def next_file_name():
    num = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    while True:
        file_name = 'submissions/' + num + '.json'
        if not os.path.exists(file_name):
            return file_name
        num = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
