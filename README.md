# ドキュメント

https://docs.djangoproject.com/en/4.0/


# djangoプロジェクト作成

`docker-compose run web django-admin startproject プロジェクト名 .`
`docker-compose run web django-admin startproject my_project .`

# DB設定

projectDIR/settings.pyの修正
DATABASESのdefaultの中身を修正する時に
docker-compose.ymlで設定したNAMEやUSERなどと異なると、`ERR_EMPTY_RESPONSE`になるので注意


# コンテナ起動

`docker-compose up -d`

# パッケージインストール

## requirements.txtを更新する場合

webコンテナでpython3 pip installを実行する
`docker-compose run web python3 pip install -r requirements.txt`

## requirements.txtを更新しない場合
`docker-compose exec web pip install パッケージ名`
`docker-compose exec web pip install requests`

requirements.txtを更新して以下のコマンドを実行
`docker-compose build --no-cache`

# アクセス

http://127.0.0.1:8000