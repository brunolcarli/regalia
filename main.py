from threading import Thread
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from core.scrapper import retrieve_data, scrap


app = Flask(__name__)
cors = CORS(app, resources={r"/regalia": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/regalia", methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type',])
def regalia():
    data = retrieve_data()
    return jsonify(data)


def run():
  app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    runner = Thread(target=run)
    crawler = Thread(target=scrap)

    runner.start()
    crawler.start()
