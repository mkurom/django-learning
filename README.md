# ドキュメント

https://docs.djangoproject.com/en/4.0/

# 教材

https://docs.djangoproject.com/en/4.0/intro/tutorial01/

### 実践Django
https://www.shoeisha.co.jp/book/detail/9784798153964

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

## migrationファイルを作る
`python manage.py makemigrations`
## migrationファイルを元にDBに反映する(テーブル作成)
`python manage.py migrate`

- 個別に実行する場合

`python manage.py makemigrations アプリ名`

`python manage.py makemigrations products`

`python manage.py migrate アプリ名`

`python manage.py migrate products`

# testの書き方
`python manage.py test`

- 特定のアプリケーションで実行する場合
`python manage.py test アプリ名`

`python manage.py test polls`

- 特定のアプリの特定のクラスのテスト
`python manage.py test アプリ名.tests.クラス名`

`python manage.py test polls.tests.QuestionModelTests`

- 特定のアプリの特定のクラスメソッドのテスト
`python manage.py test アプリ名.tests.クラス名.メソッド名`

`python manage.py test polls.tests.QuestionModelTests.test_was_published_recently_with_future_question`

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


### pj中身

my_project : startprojectで作成したdjango プロジェクト
polls : startappで作成したチュートリアルアプリ
products : startappで作成したDjango REST frameworkのアプリ（API）
snippets : startappで作成したアプリ(実践Djangoのアプリ)

### スーパーユーザー、DBログイン
.envを確認