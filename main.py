from flask import Flask, redirect


app = Flask(__name__)


@app.route("/")
def trolling():
    return """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Вам банчик)</title>
 </head>
 <body>
  <p><a href="https://rt.pornhub.com/">Связаться с мафией</a></p>
 </body>
</html>"""


if __name__ == '__main__':
    app.run()
