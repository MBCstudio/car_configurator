from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Cabin(db.Model):
    __tablename__ = 'cabins'
    id = db.Column(db.Integer, primary_key=True)
    id_brand = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)

    brand = db.relationship("Brand", backref="cabins")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "brand": self.brand.to_dict()}


class AxleSpacing(db.Model):
    __tablename__ = 'axle_spacing'
    id = db.Column(db.Integer, primary_key=True)
    id_cabin = db.Column(db.Integer, db.ForeignKey('cabins.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    min_length = db.Column(db.Integer, nullable=True)
    max_length = db.Column(db.Integer, nullable=True)

    cabin = db.relationship("Cabin", backref="axle_spacing")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cabin": self.cabin.to_dict(),
            "min_length": self.min_length,
            "max_length": self.max_length
        }


class Engine(db.Model):
    __tablename__ = 'engines'
    id = db.Column(db.Integer, primary_key=True)
    id_axle_spacing = db.Column(db.Integer, db.ForeignKey('axle_spacing.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    axle_spacing = db.relationship("AxleSpacing", backref="engines")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "axle_spacing": self.axle_spacing.to_dict(),
            "price": self.price,
            "weight": self.weight
        }


class BodyType(db.Model):
    __tablename__ = 'body_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Dimension(db.Model):
    __tablename__ = 'dimensions'
    id = db.Column(db.Integer, primary_key=True)
    id_body_type = db.Column(db.Integer, db.ForeignKey('body_types.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    body_type = db.relationship("BodyType", backref="dimensions")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "body_type": self.body_type.to_dict(),
            "price": self.price,
            "weight": self.weight
        }


class Addon(db.Model):
    __tablename__ = 'addons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "weight": self.weight
        }
def init_db(app):
    with app.app_context():
        db.create_all()



