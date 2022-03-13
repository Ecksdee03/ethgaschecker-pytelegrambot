#configures web server to run at same time as Bot so it runs in background
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your bot is alive!"

def run():       
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()