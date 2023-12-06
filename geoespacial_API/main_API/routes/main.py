from flask import jsonify, request
from main_API import app
from geoespacial_convertion import open_dataset_file_info

@app.route('/dataset', methods=['GET', 'POST'])
def get_dataset_info():
    if request.method == "POST":
        try:
            dataset_path = request.json['name']
            dataset_result = open_dataset_file_info(dataset_path)

            if dataset_result:
                return jsonify(dataset_result)
            else:
                return jsonify({'error': 'Falha ao processar o conjunto de dados'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Esta rota aceita apenas solicitações POST com um json contendo o caminho do arquivo .tif.'})

@app.route('/view_raster', methods=['GET'])
def add_tif():
    return 'a'

@app.route('/roi', methods=['POST'])
def analyze_roi():
    return 'b'

@app.route('/upload_raster', methods=['POST'])
def upload_raster():
    return 'c'
