# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer
from models import Base, User

@pytest.fixture(scope="function")
def postgres_container():
    """PostgreSQLコンテナを起動し、function毎にコンテナを作成・削除する"""
    with PostgresContainer("postgres:16") as postgres:
        # データベース接続設定
        db_url = postgres.get_connection_url()
        engine = create_engine(db_url)
        # テーブル作成
        Base.metadata.create_all(engine)
        yield postgres  # コンテナ情報を返す

@pytest.fixture
def session(postgres_container):
    """テスト用のセッションを提供"""
    db_url = postgres_container.get_connection_url()
    engine = create_engine(db_url)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    yield session
    session.close()
