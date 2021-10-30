from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.secret_key = "this is a secret"

@app.route("/")
def welcome():
    if "counter" in session:
        session["counter"] = session["counter"] + 1
    else:
        session["counter"] = 1
    return render_template("index.html")

@app.route("/counter")
def session_two():
    if "counter" in session:
        if "add_number" in request.args:
            session["counter"] = session["counter"] + request.args.get("add_number", 0, int)-1
        else:
            session["counter"] = session["counter"] + 1
    else:
        session["counter"] = 1
    return redirect(url_for("welcome"))

@app.route("/destroy_session") # look up get
def reset():
    session["counter"] = 0
    return redirect(url_for("welcome"))

if __name__=="__main__":
    app.run(debug=True)