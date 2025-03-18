# Docker-in-Docker テストプロジェクト

このプロジェクトは、Docker-in-Docker（DinD）環境でtestcontainersのテストを行うためのサンプルプロジェクトです。

## プロジェクト構成

- `compose.yml`: Docker Composeの設定ファイル
- `Dockerfile`: アプリケーションのDockerfile
- `src/`: ソースコードディレクトリ
  - `conftest.py`: testcontainersの設定ファイル
  - `models.py`: データモデル定義ファイル
  - `test_postgres.py`: テストファイル

## セットアップ

1. Dockerとdocker-composeがインストールされていることを確認してください。

2. プロジェクトのルートディレクトリで以下のコマンドを実行し、Docker環境をビルドして起動します：

   ``` bash
   docker compose build
   ```

## 使用方法

dind環境を起動させます。
   ``` bash
   docker compose up -d dind
   ```
appコンテナを起動させ、テストを実行します。
   ``` bash
   docker compose up app
   ```

## 環境の停止

テストが完了したら、以下のコマンドで環境を停止できます：

``` bash
docker compose down
```

## 注意事項

- 初回実行時は、Dockerイメージのビルドに時間がかかる場合があります。
- Docker-in-Dockerサービスの起動に少し時間がかかる場合があるため、テストの開始が遅れる可能性があります。
