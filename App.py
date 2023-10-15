

import pickle

from flask  import Flask ,render_template


app=Flask(__name__)
main=pickle.load(open('C:/Users/Ishita/OneDrive/Desktop/Face Recognition/Attendance.pkl','rb'))


@app.route('/')
def index():
   
     return render_template('home.html')
    # elif request== 'POST':
    #     ip = []
    # for i in request.values():
    #     ip.append(i)
    #     print[ip]
        

        #return render_template("home.html")


# app.debug=True
# app.run(host='localhost')
if __name__ =='__main__':
     app.run(debug=True)