# ドキュメント

https://docs.djangoproject.com/en/4.0/

# 教材

https://docs.djangoproject.com/en/4.0/intro/tutorial01/

# djangoプロジェクト作成

`docker-compose run web django-admin startproject プロジェクト名 .`
`docker-compose run web django-admin startproject my_project .`


# アプリの追加

`python manage.py startapp アプリ名`
`python manage.py startapp products`

# DB設定

projectDIR/settings.pyの修正
DATABASESのdefaultの中身を修正する時に
docker-compose.ymlで設定したNAMEやUSERなどと異なると、`ERR_EMPTY_RESPONSE`になるので注意


# コンテナ起動

`docker-compose up -d`

# dockerコンテナに入る(実行中のコンテナでコマンドを実行する)
`docker-compose exec web bash`

# コンテナから抜ける
`exit`

# MySqlに接続(コンテナに入っている状態で入力)
`mysql -h 127.0.0.1 -P 3306 -u root -p`
※パスはMYSQL_ROOT_PASSWORDで設定したパスワード

# モデルの変更

`python manage.py makemigrations`

`python manage.py migrate`

# パッケージインストール
※要確認

## requirements.txtを更新する場合

`docker-compose run web python3 pip install -r requirements.txt`

## requirements.txtを更新しない場合
`docker-compose exec web pip install パッケージ名`
`docker-compose exec web pip install requests`

requirements.txtを更新して以下のコマンドを実行
`docker-compose build --no-cache`

# アクセス

http://127.0.0.1:8000