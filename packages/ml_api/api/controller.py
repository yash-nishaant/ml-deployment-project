from flask import Blueprint, request, jsonify
from lasso_regression_model.predict import make_prediction
from lasso_regression_model import __version__ as _version

from api.config import get_logger
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('predicton_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})


@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_json=json_data)

        # Model prediction
        result = make_prediction(input_data=json_data)
        _logger.debug(f'Outputs: {result}')

        # Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # return JSON response
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})
