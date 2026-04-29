from flask import Flask, render_template, request, redirect, session, Response
import json, os, datetime, re
from werkzeug.security import generate_password_hash, check_password_hash

# ✅ Prometheus
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
app.secret_key = "secret123"

DATA_FILE = "data.json"

# ✅ Metrics
login_success = Counter('login_success_total', 'Total successful logins')
login_fail = Counter('login_fail_total', 'Total failed logins')

# ------------------ Helpers ------------------

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[@$!%*?&]", password): score += 1
    return score

# ------------------ Routes ------------------

@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/register')
def register_page():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    users = load_users()

    username = request.form['username']
    password = request.form['password']

    strength = password_strength(password)

    users[username] = {
        "password": generate_password_hash(password),
        "login_count": 0,
        "last_login": None,
        "strength": strength
    }

    save_users(users)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    users = load_users()

    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username]['password'], password):
        users[username]['login_count'] += 1
        users[username]['last_login'] = str(datetime.datetime.now())
        save_users(users)

        login_success.inc()   # ✅ metric

        session['user'] = username
        return redirect('/dashboard')

    login_fail.inc()  # ✅ metric
    return "Invalid credentials"

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    users = load_users()
    user = users[session['user']]

    return render_template("dashboard.html",
                           username=session['user'],
                           count=user['login_count'],
                           last=user['last_login'],
                           strength=user['strength'])

# ✅ Prometheus endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)