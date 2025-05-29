import flask

app = flask.Flask(__name__)

# ------------ GLOBALS

# bad practice? :D
result_data = []

# ------------ ROUTES


@app.route("/")
def index():
    return "<h1>Super Duper Site</p>"


@app.route("/reader")
def reader():
    data = [
        {"name": "jeff", "age": 1, "is_cool": False},
        {"name": "marry", "age": 10, "is_cool": True},
        {"name": "luke", "age": 20, "is_cool": True},
        {"name": "vegeta", "age": 100, "is_cool": True},
    ]

    return flask.render_template("reader.html", data=data)


@app.route("/writer")
def writer():
    return flask.render_template("writer.html")


@app.route("/results")
def results():
    return flask.render_template("results.html", data=result_data)


# ------------ API


@app.route("/writer_submit", methods=["POST"])
def writer_submit():
    name = flask.request.form["name"]
    age = flask.request.form["age"]
    is_cool = flask.request.form["is_cool"]

    try:
        name, age, is_cool = try_parse(name, age, is_cool)
    except Exception:
        return flask.jsonify({"error": "invalid fields"}), 400

    power_level = 2 * age if not is_cool else age * age
    global result_data
    result_data.append({"name": name, "power_level": power_level})

    return flask.jsonify({"message": "success", "data": result_data}), 200


# ------------ UTILS


def try_parse(name, age, is_cool):
    return str(name), int(age), bool(is_cool)
