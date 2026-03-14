from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Flask App</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg,#1e3c72,#2a5298);
                margin:0;
                height:100vh;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                text-align:center;
            }

            .card{
                background:white;
                color:#333;
                padding:40px;
                border-radius:12px;
                box-shadow:0 10px 25px rgba(0,0,0,0.2);
                width:400px;
            }

            h1{
                margin-bottom:10px;
                color:#2a5298;
            }

            p{
                font-size:16px;
            }

            .btn{
                display:inline-block;
                margin-top:20px;
                padding:10px 20px;
                background:#2a5298;
                color:white;
                text-decoration:none;
                border-radius:6px;
            }

            .btn:hover{
                background:#1e3c72;
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>🚀 DevOps Flask App</h1>
            <p>Welcome to the Dockerized Flask Application</p>
            <p>Created by <b>Nasiroddin</b></p>

            <a class="btn" href="https://github.com/nasiroddin-qatib/Docker-Python-Flask-Project" target="_blank">
                View GitHub
            </a>
        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host="0.0.0.0",port=port)
