Python

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer():
    amount = request.form['amount']
    # Process the transfer (vulnerable to CSRF)
    return f"Transferred {amount}!"

@app.route('/')
def index():
    return render_template_string('''
        <form method="POST" action="/transfer">
            <input type="text" name="amount" placeholder="Amount">
            <input type="submit" value="Transfer">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
