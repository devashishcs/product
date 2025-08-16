from flask import Flask
from routes.routes import quickcom  # import the blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(quickcom)

if __name__ == "__main__":
    app.run(debug=True)