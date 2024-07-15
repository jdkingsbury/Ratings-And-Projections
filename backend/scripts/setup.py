from app.database import Base, engine
from scripts.populate_data import populate_players


def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    populate_players()
    print("Database setup complete.")
