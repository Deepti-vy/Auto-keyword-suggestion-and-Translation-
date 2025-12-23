from flask import Flask, render_template, request
from googletrans import Translator
from wordfreq import top_n_list

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    suggestions = []
    if request.method == "POST":
        word = request.form["word"].strip().lower()
        all_words = top_n_list("en", n=50000)
        matches = [w for w in all_words if w.startswith(word)][:15]

        for w in matches:
            try:
                hi = translator.translate(w, src="en", dest="hi").text
                kn = translator.translate(w, src="en", dest="kn").text
            except:
                hi = kn = "—"
            suggestions.append({
                "word": w,
                "prob": round(100 / (matches.index(w)+1), 2),
                "hindi": hi,
                "kannada": kn
            })

    return render_template("index.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)