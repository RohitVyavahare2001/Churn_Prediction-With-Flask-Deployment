from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Home page (index.html)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get input data from the form
        gender = request.form['gender']
        age = request.form['age']
        tenure = request.form['tenure']
        monthlycharges = request.form['monthlycharges']
        totalcharges = request.form['totalcharges']
        paymentmethod = request.form['paymentmethod']
        serviceusage1 = request.form['serviceusage1']
        serviceusage2 = request.form['serviceusage2']
        serviceusage3 = request.form['serviceusage3']

        # The message to be shown on the result page
        message ="""We are currently in the final stages of refining our pipeline. 
                    While the complete pipeline code has not yet been fully integrated into the application,
                    we invite you to explore the detailed Jupyter Notebook,
                    which includes the comprehensive Exploratory Data Analysis (EDA), advanced visualizations, and an in-depth evaluation of various models.
                    Among these, the Support Vector Machine (SVM) has been identified as the most effective model for our problem statement.
                    Please refer to the "Final.ipynb" file, which is included in the shared zip folder, for a thorough review of the code, model training, and performance metrics across different machine learning models. 
                    We are excited about the progress we’ve made and look forward to sharing the complete implementation with you soon"""

        return render_template('result1.html', message=message)

    return render_template('predict.html')  # Prediction input page (predict.html)

if __name__ == '__main__':
    app.run(debug=True)
