from flask import jsonify
from main_API import app
from geoespacial_convertion import open_dataset_file_info

@app.route('/dataset_info', methods=['GET'])
def get_dataset_info():
    dataset_result = open_dataset_file_info()

    return jsonify(dataset_result)

@app.route('/view_raster', methods=['GET'])
def add_tif():
    return 'a'

@app.route('/roi', methods=['POST'])
def analyze_roi():
    return 'b'

@app.route('/upload_raster', methods=['POST'])
def upload_raster():
    return 'c'
