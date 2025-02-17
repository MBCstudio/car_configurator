from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import setup_routes
from models import init_db, db

class CarConfiguratorApp:
    """Main application class for the car configurator."""

    def __init__(self):
        """Initialize the Flask app."""
        self.app = Flask(__name__)
        self.configure_app()

    def configure_app(self):
        """Konfiguracja aplikacji i bazy danych"""
        self.app.config['SECRET_KEY'] = 'your_secret_key_here'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/car_configurator'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        init_db(self.app)  # Tworzy tabele, jeśli ich nie ma
        self.register_routes()

    def register_routes(self):
        """Register all application routes."""
        setup_routes(self.app)

    def run(self):
        """Run the Flask app."""
        self.app.run(debug=True)


if __name__ == "__main__":
    app_instance = CarConfiguratorApp()
    app_instance.run()

