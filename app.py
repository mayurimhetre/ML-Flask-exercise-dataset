# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'logistic_regression_model_01.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        id = int(request.form['id'])
        pulse = int(request.form['pulse'])
        diet = str(request.form['diet'])
        time = int(request.form['time'])
        if (diet == 'Low'):
            diet_low = 1
            diet_high = 0
        else:
            diet_low = 0
            diet_high = 1
        if (time == '15'):
            time_15min = 1
            time_30min = 0
        elif(time == '30'):
            time_15min = 0
            time_30min = 1
        else:
            time_15min = 0
            time_30min = 0

        data = np.array([[id, pulse, diet_low, time_15min, time_30min]])
        my_prediction = classifier.predict(data)
        my_prediction = my_prediction[0]
        return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)