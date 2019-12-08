from flask import Flask, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify
import psycopg2

app = Flask(__name__)

def get_data_from_db(query: str, table) -> list:
    try:
        conn = psycopg2.connect(host="https://dreamteam330.herokuapp.com/", port=5432, dbname=table)
    except:
        raise ConnectionError("Bad stuff")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

@app.route("/", methods=["GET", "POST"])
def index():
        query = "select id from player"
        result = get_data_from_db(query, "player")
        print(result)
        return render_template("result.html", rows=result)


# @app.route('/api/v1/players/<int:id>')
# def player():
#     jokes=pyjokes.get_jokes("en", "all")
#     rand=random.randrange(0,201)
#     joke=jokes[rand]
#     joke_in_dict ={"joke": joke}
#     asdf =jsonify(joke_in_dict)
#     return "<html><body>"+asdf+"</body></html>"

# @app.route('/api/v1/teams/<int:id>')
# def specific_joke(id):
#     jokes=pyjokes.get_jokes("en", "all")
#     joke=jokes[id]
#     joke_in_dict ={"joke": joke}
#     return jsonify(joke_in_dict)
