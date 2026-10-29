from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "finalyearprojectkey"

DB_NAME = "tourist.db"

# ---------------- DATABASE ---------------- #

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    # Users table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Tourist data table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tourist (
        city TEXT,
        category TEXT,
        info TEXT
    )
    """)

    # Insert default user (only once)
    user_count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if user_count == 0:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )

    # Insert tourist data (only once)
    data_count = conn.execute("SELECT COUNT(*) FROM tourist").fetchone()[0]
    if data_count == 0:
        sample_data = [
            ("goa","places","Baga Beach, Calangute Beach, Fort Aguada"),
            ("goa","food","Fish Curry, Bebinca, Prawn Balchao"),
            ("goa","stay","Beach resorts and hotels"),
            ("goa","safety","Safe, avoid isolated beaches at night"),

            ("mumbai","places","Gateway of India, Marine Drive, Juhu Beach"),
            ("mumbai","food","Vada Pav, Pav Bhaji, Bhel Puri"),
            ("mumbai","stay","Hotels in Andheri, Colaba"),
            ("mumbai","safety","Generally safe, avoid late night travel alone"),

            ("banglore","places","Lalbagh, Cubbon Park, Bangalore Palace"),
            ("banglore","food","Dosa, Idli, Filter Coffee"),
            ("banglore","stay","Service apartments, hotels"),
            ("banglore","safety","Safe city"),

            ("delhi","places","India Gate, Red Fort, Qutub Minar"),
            ("delhi","food","Chole Bhature, Paratha"),
            ("delhi","stay","Hotels near Connaught Place"),
            ("delhi","safety","Use registered transport"),

            ("kerla","places","Munnar, Backwaters, Wayanad"),
            ("kerla","food","Sadya, Appam"),
            ("kerla","stay","Houseboats, resorts"),
            ("kerla","safety","Very safe"),

            ("manali","places","Solang Valley, Rohtang Pass"),
            ("manali","food","Momos, Thukpa"),
            ("manali","stay","Hill resorts"),
            ("manali","safety","Cold weather precautions"),

            ("madhyapradesh","places","Khajuraho, Sanchi"),
            ("madhyapradesh","food","Poha, Bhutte ka kees"),
            ("madhyapradesh","stay","Heritage hotels"),
            ("madhyapradesh","safety","Safe"),

            ("konkan","places","Ganpatipule, Ratnagiri"),
            ("konkan","food","Seafood, Kokum curry"),
            ("konkan","stay","Homestays"),
            ("konkan","safety","Safe coastal region")
        ]

        conn.executemany(
            "INSERT INTO tourist (city, category, info) VALUES (?,?,?)",
            sample_data
        )

    conn.commit()
    conn.close()

# ---------------- NLP HELPERS ---------------- #

def detect_city(message):
    cities = [
        "goa","mumbai","banglore","delhi",
        "kerla","manali","madhyapradesh","konkan"
    ]
    for city in cities:
        if city in message.lower():
            return city
    return None

def detect_category(message):
    msg = message.lower()
    if any(w in msg for w in ["place","visit","attraction"]):
        return "places"
    if any(w in msg for w in ["food","eat","cuisine"]):
        return "food"
    if any(w in msg for w in ["stay","hotel","resort"]):
        return "stay"
    if any(w in msg for w in ["safe","safety"]):
        return "safety"
    return None

# ---------------- ROUTES ---------------- #

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if "user" not in session:
        return jsonify({"reply":"Please login","images":[]})

    message = request.json.get("message","")
    city = detect_city(message)
    category = detect_category(message)

    if not city or not category:
        return jsonify({
            "reply":"🤖 Please mention city and category (places, food, stay, safety).",
            "images":[]
        })

    conn = get_db()
    result = conn.execute(
        "SELECT info FROM tourist WHERE city=? AND category=?",
        (city, category)
    ).fetchone()
    conn.close()

    images = []
    if category == "places":
        images_map = {
            "goa":["goa.jpg"],
            "mumbai":["mumbai.jpg"],
            "banglore":["banglore.jpg"],
            "delhi":["delhi.jpeg"],
            "kerla":["kerla.jpg"],
            "manali":["manali.jpg"],
            "madhyapradesh":["madhyapradesh.jpg"],
            "konkan":["konkan.jpg"]
        }
        images = images_map.get(city, [])

    if result:
        return jsonify({
            "reply": result["info"],
            "images": images
        })

    return jsonify({"reply":"No data found","images":[]})

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
