from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import PIL.Image, PIL.ImageDraw, PIL.ImageFont


app = Flask(__name__, static_folder='./templates/img')

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# ユーザー数
user_count = 0
# 現在のテキスト
text = ""
imgx = ""
imgy = ""


# ユーザーが新しく接続すると実行
@socketio.on('connect')
def connect(auth):
    global user_count, text
    user_count += 1
    # 接続者数の更新（全員向け）
    emit('count_update', {'user_count': user_count}, broadcast=True)
    # テキストエリアの更新
    emit('text_update', {'text': text})


# ユーザーの接続が切断すると実行
@socketio.on('disconnect')
def disconnect():
    global user_count
    user_count -= 1
    # 接続者数の更新（全員向け）
    emit('count_update', {'user_count': user_count}, broadcast=True)


# テキストエリアが変更されたときに実行
@socketio.on('text_update_request')
def text_update_request(json):
    global text
    text = json["text"]
    # 変更をリクエストした人以外に向けて送信する
    # 全員向けに送信すると入力の途中でテキストエリアが変更されて日本語入力がうまくできない
    emit('text_update', {'text': text}, broadcast=True, include_self=False)




@app.route('/')
def index():
    global name
    return render_template("index.html",name = name)



@app.route('/name', methods=["POST"])
def name():
    global name
    name = request.form["name"]
    return render_template("name.html", name = name)

@app.route('/menu')
def menu():
    return render_template("menu.html", player = player)

@app.route('/room')
def room():
    return "roomdaze"

@app.route('/show')
def show():
    message = "hello world"
    return render_template("form.html", message = message)



@app.route('/test')
def test():
    message = "hello world"
    return render_template("test.html", message = message)




if __name__ == "__main__":
    app.run(host="0.0.0.0")
