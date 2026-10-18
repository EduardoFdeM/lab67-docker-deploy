from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Laboratório 6.7</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 100px 20px;
                background: #f3f4f6;
            }
            h1 { color: #c8102e; }
        </style>
    </head>
    <body>
        <h1>Hello World atualizado!</h1>
        <p>Engenharia de Software - Mackenzie</p>
        <p>Aplicação Flask executada com Docker.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)