# from app.db.database import Base, engine
from app.db.models.models import *
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
