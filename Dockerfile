# ベースイメージとしてPythonの最新版を使用
FROM python:3.13-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Poetryをインストール
RUN pip install sqlalchemy pytest psycopg2-binary testcontainers


# アプリケーションのソースコードをコピー
COPY src/ ./src/

# コンテナ起動時のコマンドを設定
CMD ["python", "-m", "pytest"]
