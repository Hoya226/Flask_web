
from flask import Flask, render_template              #(html에서 텍스트형태로)템플릿을 랜더링 해주는 메소드
from data import Articles
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])     #<- 플라스크에서 내가 원하는 경로 지정하는 방법
def index():
    print("Success")
    # return "Test"
    return render_template('home.html', hello="Hoya")

@app.route('/about', methods=['GET', 'POST'])
def about():
    print("Success")
    # return "Test"
    return render_template('about.html', hello="Hoya")

@app.route('/articles', methods=['GET', 'POST'])
def articles():
    print("Success")
    # return "Test"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port ='8000')
    app.run()
