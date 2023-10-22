import json
from flask import Flask, jsonify
import configparser

app = Flask(__name__)

# Function to read configuration file and store data in a dictionary
def read_config_file(file_path):
    config_data = {}
    try:
        config = configparser.ConfigParser()
        config.read(file_path)
        # Extract specific key-value pairs from the configuration file
        config_data['host'] = config.get('Database', 'host')
        config_data['port'] = config.get('Database', 'port')
        config_data['username'] = config.get('Database', 'username')
        config_data['password'] = config.get('Database', 'password')
        config_data['server'] = config.get('Server', 'server_name')
        config_data['port'] = config.get('Server', 'port')
    except Exception as e:
        print(f"Error: {e}")
    return config_data

# Read configuration file and store data in a dictionary
config_data = read_config_file('config.ini')

# Save the output data as JSON in a database (for example, saving it as a JSON file)
with open('output.json', 'w') as json_file:
    json.dump(config_data, json_file)

# Flask route to serve the extracted information
@app.route('/config', methods=['GET','POST'])
def get_config_data():
    return jsonify(config_data)

if __name__ == '__main__':
    app.run(debug=True)
