from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

# Define the path for storing performance reports
DATA_PATH = os.path.join(os.getcwd(), 'data')

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_report', methods=['POST'])
def submit_report():
    report_data = {
        'date': request.form['date'],
        'employee_name': request.form['employee_name'],
        'performance': request.form['performance'],
    }

    # Generate a unique filename using the date
    filename = f"{report_data['date']}.json"
    file_path = os.path.join(DATA_PATH, filename)

    # Save the report data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(report_data, f)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
