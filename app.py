from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [ 
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bangalore",
        "salary": "Rs 10,00,000"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Mumbai",

    },
    {
        "id": 3,
        "title": "Full Stack Developer",
        "location": "Bangalore",
        "salary": "Rs 12,00,000"
    },
    {
        "id": 4,
        "title": "Back End Developer",
        "location": "New York",
        "salary": "$ 120,000"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Jovian")

@app.route("/api/jobs")
def get_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)