from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get the current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Define your GitHub URLs
    github_file_url = "https://github.com/94Cent/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/94Cent/repo"

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
