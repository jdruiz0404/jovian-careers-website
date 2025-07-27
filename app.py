from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Bangalore',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Delhi',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 4,
        'title': 'Data Analyst',
        'location': 'Mumbai',
    },
    {
        'id': 5,
        'title': 'Machine Learning Engineer',
        'location': 'Hyderabad',
        'salary': 'Rs. 14,00,000'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
