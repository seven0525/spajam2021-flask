#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
import time
import urllib.request

#Chromeを操作
driver = webdriver.Chrome()

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

@app.route("/get-color")
def index():
    driver.get("https://d4c2-112-138-207-235.ngrok.io")
    time.sleep(5)
    img = "/Users/watanabetaichi/Projects/spajam-flask-api/app/imgs/test1.jpeg"
    element = driver.find_element_by_id('load_line_file')
    element.send_keys(img)
    time.sleep(15)
    img_element = driver.find_element_by_id('output').get_attribute("src")
    urllib.request.urlretrieve(img_element, 'logo.jpeg')
    # with open(f"out.jpeg", 'wb') as f:
    #     f.write(img_element.screenshot_as_png)
    return render_template("index.html")

@app.route('/fax/sent', methods=['POST'])
def fax_sent():
    twiml = """
        <Response>
            <Receive action="/fax/received"/>
        </Response>
    """
    print(request.stream.read())
    return Response(twiml, mimetype='text/xml')

@app.route('/fax/received', methods=['POST'])
def fax_received():
    print(request.stream.read())
    return '', 200

#おまじない
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)