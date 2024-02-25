from flask import Flask, request, jsonify
from flask_cors import CORS  # Install using: pip install flask-cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json

    # Access the received data
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    specification = data.get('specification')
    location = data.get('location')
    difference_in_days = data.get('differenceInDays')

    # Print the received data to the console
    print('Start Date:', start_date)
    print('End Date:', end_date)
    print('Specification:', specification)
    print('Location:', location)
    print('Difference in days:', difference_in_days)

    # You can perform further processing with the received data here

    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
