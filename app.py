from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    refrigerant = request.form['refrigerant']
    T1 = float(request.form['T1'])
    T2 = float(request.form['T2'])
    T3 = float(request.form['T3'])
    T4 = float(request.form['T4'])
    P1 = float(request.form['P1'])
    P2 = float(request.form['P2'])
    T5 = float(request.form['T5'])
    h1 = float(request.form['h1'])
    h2 = float(request.form['h2'])
    h3 = float(request.form['h3'])
    h4 = float(request.form['h4'])

    Q = h3 - h1
    W = h4 - h3
    cop = Q / W
    ideal_cop = (T3 + 273.15) / (T1 - T3)

    return render_template('result.html', refrigerant=refrigerant, T1=T1, T2=T2, T3=T3, T4=T4, P1=P1, P2=P2, T5=T5,
                           h1=h1, h2=h2, h3=h3, h4=h4, Q=Q, W=W, cop=cop, ideal_cop=ideal_cop)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

