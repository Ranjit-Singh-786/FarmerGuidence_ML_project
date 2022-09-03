from flask import Flask , jsonify , request, render_template
import pickle
import numpy
import warnings
warnings.filterwarnings('ignore')
model = pickle.load(open('farmermodel.pkl','rb'))
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if (request.method=='POST'):
        Nitrogen = int(request.form['Nitrogen'])
        Phosphorus = int(request.form['Phosphorus'])
        potassium = int(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

    list_of_elements = [[Nitrogen,Phosphorus,potassium,temperature,humidity,ph,rainfall]]
    result = model.predict(list_of_elements)
    output = result[0]

    return render_template('result.html' , prediction_text = output)
    

if __name__=="__main__":
    app.run(debug=True)