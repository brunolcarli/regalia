from threading import Thread
from flask import Flask
from core.scrapper import retrieve_data, scrap


app = Flask(__name__)


@app.route("/regalia")
def regalia():
    data = retrieve_data()
    return data


def run():
  app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    runner = Thread(target=run)
    crawler = Thread(target=scrap)

    runner.start()
    crawler.start()
