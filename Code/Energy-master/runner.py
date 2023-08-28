from flask import Flask
from api import api_bp
from web import web_bp

app = Flask(__name__)

# 注册Blueprint
app.register_blueprint(api_bp)
app.register_blueprint(web_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
