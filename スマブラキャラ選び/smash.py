# インストールした「flask」モジュールをインポートする
from flask import Flask,render_template, request
from model import model,wakati_by_mecab
import gensim

# インスタンス化する
app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

#ルーティング設定をする
#@app.route("/")
#def index():
   # return render_template('index.html')

@app.route("/",methods=["GET","POST"])
def calculation():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        style = request.form['style']
        text  = wakati_by_mecab(style)
        fighter1,fighter2,fighter3,fighter4,fighter5 = model(text)# モデルの出番？
        return render_template('index.html', fighter1=fighter1,fighter2=fighter2,fighter3=fighter3,fighter4=fighter4,fighter5=fighter5,style=style)



if __name__ == "__main__": #最後に記述する
    app.run(debug=True)