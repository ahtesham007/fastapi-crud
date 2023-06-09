# from fastapi.testclient import TestClient
# from app.database import get_db, Base
# from app.main import app
# from urllib.parse import quote_plus
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker
# from app.config import settings
# import pytest
# from alembic import command

# user = settings.user
# # encoded_pwd = quote_plus(settings.pwd)
# encoded_pwd = settings.pwd
# host = settings.host
# port = settings.port
# db = settings.db

# SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{user}:{encoded_pwd}@{host}:{port}/{db}_test'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @pytest.fixture
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     # command.upgrade('head')
#     # command.downgrade('head')
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @pytest.fixture
# def client(session):
#     def override_get_db():
#         try:
#             yield session
#         finally:
#             session.close()

#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)
