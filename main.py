import flask
from flask import request, jsonify
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#json data
test_tasks = [
    {
    'id': '1',
    'name': 'to-do-1',
    'due': '2020-01-20',
    'status': 'done'
    },
    {
    'id': '2',
    'name': 'to-do-2',
    'due': '2020-01-19',
    'status': 'in-progress'
        
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Task App API</h1><p>This site is a prototype API for tasks application.</p>"

#displays all the tasks
@app.route('/tasks/all', methods=['GET'])
def api_all():
    return jsonify(test_tasks)

#displays the task based on id

@app.route('/tasks/task', methods=['GET'])
def task_by_id():
    id = 0
    if 'id' in request.args:
        id = int(request.args['id'])
        print (id)
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for task in test_tasks:
        if (int(task['id']) == id):
            print ("found") 
            results.append(task)
    return jsonify(results)

#to display the tasks due today
@app.route('/tasks/due', methods=['GET'])
def tasks_due_today():
    current_date = datetime.today().strftime('%Y-%m-%d')
    print(current_date)

    tasks_due = []
    for task in test_tasks:
        print (type(current_date))
        print (type(task['due']))
        if (task['due'] == current_date):
            print ("found") 
            tasks_due.append(task)
    return jsonify(tasks_due)

app.run()
