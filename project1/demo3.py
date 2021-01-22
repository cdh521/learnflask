from flask import Flask,render_template
app =Flask(__name__)
@app.route("/")
def index():
    name = "xiaobuding"
    return render_template("index.html",**locals())
@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到详情页{pk}"
if __name__ == '__main__':
    app.run(host="192.168.11.5",port=6788,debug=True)