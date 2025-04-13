from flask import Flask, render_template, request
from youtubesearchpython import VideosSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        keywords = request.form['keywords']
        search = VideosSearch(f"{keywords} music", limit=1)
        results = search.result()
        if results['result']:
            video_id = results['result'][0]['id']
            video_url = f"https://www.youtube.com/embed/{video_id}"
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
