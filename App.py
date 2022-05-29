

import pickle

from flask  import Flask ,render_template,request


app=Flask(__name__)
main=pickle.load(open('Attendance.pkl','rb'))


@app.route('/test/',methods=['GET','POST'])
def index():
    if i in request.method =='GET':
     return render_template('home.html')
    elif request== 'POST':
        ip = []
    for i in request.values():
        ip.append(i)
        print[ip]
        

        #return render_template("home.html")


app.debug=True
app.run(host='localhost')






