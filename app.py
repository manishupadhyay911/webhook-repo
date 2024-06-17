from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import datetime

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['github_events']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    
    event = {
        "author": "",
        "action": event_type,
        "from_branch": "",
        "to_branch": "",
        "timestamp": datetime.datetime.utcnow(),
        "request_id": ""
    }

    if event_type == "push":
        event["author"] = data['pusher']['name']
        event["to_branch"] = data['ref'].split('/')[-1]
        event["request_id"] = data['head_commit']['id']

    elif event_type == "pull_request":
        event["author"] = data['pull_request']['user']['login']
        event["from_branch"] = data['pull_request']['head']['ref']
        event["to_branch"] = data['pull_request']['base']['ref']
        event["timestamp"] = data['pull_request']['created_at']
        event["request_id"] = data['pull_request']['head']['sha']

        if data['pull_request']['merged']:
            event["action"] = "merge"
            event["timestamp"] = data['pull_request']['merged_at']
            event["request_id"] = data['pull_request']['merge_commit_sha']

    else:
        return jsonify({'status': 'unhandled event'}), 400

    collection.insert_one(event)
    return jsonify({'status': 'success'}), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort('timestamp', -1))
    for event in events:
        event['_id'] = str(event['_id'])
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)

