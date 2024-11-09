from flask import Flask, render_template, request
from datetime import datetime
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    error_message = None
    try:
        if request.method == 'POST':
            date_of_birth = request.form['dob']
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except Exception as e:
        error_message = f"Error calculating age: {e}"
        logging.error(error_message)
    return render_template('index.html', age=age, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
