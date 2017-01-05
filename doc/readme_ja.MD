## 動作環境
動作に必要なミドルウェアは下記の通りです。

|名称|バージョン|
|:---|:---|
|Python|3.4.2|
|bottle|0.12.11|
|Redis server|2.8.17

## ディレクトリ構成
リポジトリ内は以下のディレクトリで構成されます。

|パッケージ名|説明|
|:---|:---|
|doc|ドキュメントを格納|
|common|共通パッケージ|
|dao\interface|DAOインターフェースパッケージ|
|dao\implement|DAO実装クラスパッケージ|
|dto|データ転送オブジェクトパッケージ|
|function|bottleで使用するファンクションパッケージ|
|template|bottleで使用するHTMLテンプレート|

## 備考
### python3 GPIOライブラリ　インストール
python3用のGPIOライブラリをインストールする。

`$ sudo apt-get install python3-rpi.gpio`

### GPIOの定数値

|名称|値|
|:---|:---|
|GPIO.IN|1|
|GPIO.OUT|0|
|GPIO.BOARD|10|
|GPIO.BCM|11|
