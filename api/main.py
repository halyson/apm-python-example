from flask import Flask, jsonify
import elasticapm

from elasticapm.contrib.flask import ElasticAPM


app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'APP_NAME': 'flask-apm-client',
    'DEBUG': True,
    'SERVER_URL': 'http://localhost:8200',
    'SERVICE_NAME': 'api-test'
}

apm = ElasticAPM(app, logging=True)


@elasticapm.capture_span()
def test(name):
    return name


@app.route('/')
def index():
    return jsonify({"message": "response ok"}), 200


@app.route('/print')
def printing():
    return jsonify({"message": test('teste')}), 200


@app.route('/5xx')
def fail_with_5xx():
    value = 'a' + 1
    return jsonify({"message": value})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
