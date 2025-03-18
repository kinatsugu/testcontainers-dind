# test_postgres.py
from models import User

def test_user_insert_and_select(session):
    """テーブルを作成し、データを挿入・取得するテスト"""
    # データ挿入
    user = User(name="Alice")
    session.add(user)
    session.commit()

    # データ取得
    fetched_user = session.query(User).filter_by(name="Alice").first()

    # アサーション
    assert fetched_user is not None
    assert fetched_user.name == "Alice"

def test_user_select_and_update(session):
    """データを取得し、更新するテスト"""
    # データ挿入
    user = User(name="Mike")
    session.add(user)
    session.commit()

    # データ取得
    user = session.query(User).filter_by(name="Mike").first()

    # データ更新
    user.name = "Bob"
    session.commit()

    # データ取得
    fetched_user = session.query(User).filter_by(name="Bob").first()

    # アサーション
    assert fetched_user is not None
    assert fetched_user.name == "Bob"
