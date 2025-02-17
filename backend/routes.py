from flask import Flask, jsonify
from flask_cors import CORS # Allows frontend to call backend
from models import Car

def setup_routes(app):
    """Register routes for the Flask app."""
    CORS(app)  # Enable CORS

    @app.route('/api/config', methods=['GET'])
    def get_config():
        """Pobiera auto z bazy danych"""
        car = Car.query.first()  # Pobiera pierwszy wpis z tabeli
        if car:
            return jsonify(car.to_dict())  # Zwraca JSON
        return jsonify({"error": "Brak aut w bazie"}), 404