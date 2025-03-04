from sqlalchemy import text

from models import db, Brand, Cabin, AxleSpacing, Engine, BodyType, Dimension, Addon


def seed_data(app):
    """Usuwa istniejące dane i dodaje nowe do bazy"""
    with app.app_context():
        # Usuwamy wszystkie rekordy w odpowiedniej kolejności (najpierw tabele zależne)
        db.session.execute(text("DELETE FROM dimensions;"))
        db.session.execute(text("DELETE FROM addons;"))
        db.session.execute(text("DELETE FROM engines;"))
        db.session.execute(text("DELETE FROM axle_spacing;"))
        db.session.execute(text("DELETE FROM cabins;"))
        db.session.execute(text("DELETE FROM body_types;"))
        db.session.execute(text("DELETE FROM brands;"))
        db.session.commit()

        # Ponownie dodajemy marki
        brands = [
            Brand(name="Ford"),
            Brand(name="Mercedes"),
            Brand(name="Volvo")
        ]
        db.session.add_all(brands)
        db.session.commit()  # WAŻNE: Zapisujemy, aby dostały ID

        # Pobieramy marki z bazy, żeby znać ich ID
        ford = Brand.query.filter_by(name="Ford").first()
        mercedes = Brand.query.filter_by(name="Mercedes").first()

        # Teraz dodajemy kabiny, które referują do istniejących marek
        cabins = [
            Cabin(name="Standard", id_brand=ford.id),
            Cabin(name="Extended", id_brand=mercedes.id)
        ]
        db.session.add_all(cabins)
        db.session.commit()

        # Dodajemy rozstaw osi
        axle_spacings = [
            AxleSpacing(name="Krótki", id_cabin=cabins[0].id, min_length=200, max_length=300),
            AxleSpacing(name="Długi", id_cabin=cabins[1].id, min_length=300, max_length=400)
        ]
        db.session.add_all(axle_spacings)
        db.session.commit()

        # Dodajemy silniki
        engines = [
            Engine(name="Diesel 2.0", id_axle_spacing=axle_spacings[0].id, price=5000, weight=300),
            Engine(name="Diesel 3.0", id_axle_spacing=axle_spacings[1].id, price=7000, weight=400)
        ]
        db.session.add_all(engines)
        db.session.commit()

        # Dodajemy rodzaje zabudowy
        body_types = [
            BodyType(name="Furgon"),
            BodyType(name="Plandeka")
        ]
        db.session.add_all(body_types)
        db.session.commit()

        # Pobieramy typy zabudowy
        furgon = BodyType.query.filter_by(name="Furgon").first()

        # Dodajemy wymiary dla zabudowy
        dimensions = [
            Dimension(name="Mały", id_body_type=furgon.id, price=3000, weight=500),
            Dimension(name="Duży", id_body_type=furgon.id, price=5000, weight=800)
        ]
        db.session.add_all(dimensions)
        db.session.commit()

        # Dodajemy dodatki
        extras = [
            Addon(name="Klimatyzacja", price=2000, weight=50),
            Addon(name="Elektryczne szyby", price=1000, weight=20)
        ]
        db.session.add_all(extras)
        db.session.commit()

