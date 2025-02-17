from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    """Model tabeli Car - SQLAlchemy automatycznie tworzy tabelę"""
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Konwertuje obiekt na słownik dla JSON-a"""
        return {"id": self.id, "name": self.name, "price": self.price}

def init_db(app):
    """Tworzy bazę, jeśli nie istnieje"""
    with app.app_context():
        db.create_all()
        if not Car.query.first():  # Jeśli nie ma aut, dodaj pierwsze
            sedan = Car(name="Sedan", price=25000)
            db.session.add(sedan)
            db.session.commit()


