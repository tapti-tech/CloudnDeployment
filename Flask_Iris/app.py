# import Flask class from the flask module
from flask import Flask, render_template, request
import joblib
import numpy as np

# Create Flask object to run
app = Flask(__name__)

# Load the model from the file
iris_model = joblib.load('model/iris_model.pkl')

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from browser
    # http://127.0.0.1/predict?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=1.6
    sepal_length = float(request.form['sepal_length'])
    #sepal_length = request.args['sepal_length']
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    
     
    test_inp = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, 4)
    class_predicted = int(iris_model.predict(test_inp)[0])
    output = "Predicted Iris Class: " + str(class_predicted)
    
    return render_template('index.html',prediction_texts=output)

    

    #return (output)

if __name__== '__main__':
    app.debug=True
    app.run()