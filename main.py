from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

html = '''
<!DOCTYPE html>
<html>
  <body>
    <h2>画像アップロード</h2>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file"><br><br>
      <input type="submit" value="アップロード">
    </form>
    {% if filename %}
      <p>アップロード完了：{{ filename }}</p>
      <img src="/static/{{ filename }}" width="256"/>
    {% endif %}
  </body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def upload():
    filename = None
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    return render_template_string(html, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
