from flask import Blueprint, jsonify, render_template


bp = Blueprint("main", __name__)


@bp.route("/")
def joke():
    joke_prompt = "Why did the chicken cross the road?"
    return render_template("joke.html", joke_prompt=joke_prompt)


@bp.route("/feedback", methods=("POST",))
def feedback():
    feedback = "The Intermediate Value Theorem!"
    response = {"feedback": feedback}
    print(response)
    return jsonify(response)
