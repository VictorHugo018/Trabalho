from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        grau = request.form['grau']
        peso = float(request.form['peso'])

        if grau == 'leve':
            volume = 50 * peso
        elif grau == 'moderada':
            volume = 75 * peso
        elif grau == 'grave':
            volume = 100 * peso
        else:
            volume = 0

        return render_template('index.html', volume=volume)

    return render_template('index.html', volume=0)


if __name__ == '__main__':
    app.run(debug=True)
