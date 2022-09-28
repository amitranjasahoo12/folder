# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
#from wsgiref import simple_server
#import os
#import sqlite3

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            age = float(request.form['age'])
            education = float(request.form['education'])
            education_num = float(request.form['education_num'])
            marital_status = float(request.form['marital_status'])
            occupation = float(request.form['occupation'])
            relationship = float(request.form['relationship'])
            sex = float(request.form['sex'])
            capital_gain = float(request.form['capital_gain'])
            capital_loss = float(request.form['capital_loss'])
            hours_per_week = float(request.form['hours_per_week'])


            filename = 'censue price.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            # loading the model file from the storage

            # predictions using the loaded model file
            prediction = loaded_model.predict([[age, education, education_num, marital_status,
                                                occupation,relationship, sex, capital_gain,
                                                capital_loss, hours_per_week]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('index.html', hasValues=int(prediction[0]) > -1, prediction=int(prediction[0]))
        except Exception as e:
            print('The Exception message is: ', e)

            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app

#if __name__ == "__main__":
   # port = str(os.getenv("PORT"))
   # app.run(host='127.0.0.1', port=8000, debug=True)
    #app = app()
    #host = '0.0.0.0'
  #  httpd = simple_server.make_server(host=host,port=port, app=app)
   # httpd.serve_forever()
