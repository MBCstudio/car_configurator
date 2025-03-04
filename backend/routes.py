from flask import Flask, jsonify, request
from flask_cors import CORS # Allows frontend to call backend
from models import Brand, Cabin, AxleSpacing, Engine, BodyType, Dimension, Addon

def setup_routes(app):
    """Register routes for the Flask app."""
    CORS(app)  # Enable CORS

    # @app.route('/api/config', methods=['GET'])
    # def get_config():
    #     """Pobiera auto z bazy danych"""
    #     car = Car.query.first()  # Pobiera pierwszy wpis z tabeli
    #     if car:
    #         return jsonify(car.to_dict())  # Zwraca JSON
    #     return jsonify({"error": "Brak aut w bazie"}), 404

    @app.route('/api/brands', methods=['GET'])
    def get_brands():
        """Zwraca listę dostępnych marek"""
        brands = Brand.query.all()
        return jsonify([{"id": brand.id, "name": brand.name} for brand in brands])

    @app.route('/api/cabins', methods=['GET'])
    def get_cabins():
        """Zwraca listę kabin dla wybranej marki"""
        brand_id = request.args.get('id_brand', type=int)

        if brand_id:
            cabins = Cabin.query.filter(Cabin.id_brand == brand_id).all()
        else:
            cabins = Cabin.query.all()

        return jsonify([{"id": cabin.id, "name": cabin.name, "id_brand": cabin.id_brand} for cabin in cabins])

    @app.route('/api/axle_spacings', methods=['GET'])
    def get_axle_spacings():
        """Zwraca listę rozstawów osi dla wybranej kabiny"""
        cabin_id = request.args.get('id_cabin', type=int)

        if cabin_id is not None:
            axle_spacings = AxleSpacing.query.filter(AxleSpacing.id_cabin == cabin_id).all()
        else:
            axle_spacings = AxleSpacing.query.all()

        return jsonify([{"id": axle.id, "name": axle.name, "id_cabin": axle.id_cabin} for axle in axle_spacings])

    @app.route('/api/engines', methods=['GET'])
    def get_engines():
        """Zwraca listę silników dla danego rozstawu osi"""
        axle_spacing_id = request.args.get('id_axle_spacing', type=int)

        if axle_spacing_id is not None:
            engines = Engine.query.filter(Engine.id_axle_spacing == axle_spacing_id).all()
        else:
            engines = Engine.query.all()

        return jsonify([{"id": engine.id, "name": engine.name, "id_axle_spacing": engine.id_axle_spacing} for engine in engines])

    @app.route('/api/body_types', methods=['GET'])
    def get_body_types():
        """Zwraca listę rodzajów zabudowy"""
        body_types = BodyType.query.all()
        return jsonify([{"id": body.id, "name": body.name} for body in body_types])

    @app.route('/api/dimensions', methods=['GET'])
    def get_dimensions():
        """Zwraca listę wymiarów zabudowy"""
        body_type_id = request.args.get('id_body_type', type=int)

        if body_type_id is not None:
            dimensions = Dimension.query.filter(Dimension.id_body_type == body_type_id).all()
        else:
            dimensions = Dimension.query.all()

        return jsonify([{"id": dimension.id, "name": dimension.name, "id_body_type": dimension.id_body_type} for dimension in dimensions])

    @app.route('/api/extras', methods=['GET'])
    def get_extras():
        """Zwraca listę dodatków dla wybranego typu zabudowy"""
        extras = Addon.query.all()

        return jsonify([{"id": extra.id, "name": extra.name} for extra in extras])