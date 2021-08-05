# Name: Christina Wilson
# Updated: 8/5/2021
# Clock-API
#   - Purpose: Gives user the current time in various formats and the time in the future (user can specify timezone)
#   - Optional arguments supplied by client:
#       - timezone, hours, minutes, seconds
#           - Defaults to 'America/Chicago', 0, 0, 0
#   - Endpoints:
#       - current_HMS_12, current_HMS_24, current_HM_12, current_HM_24, updated_HMS_12, updated_HMS_24, updated_HM_12, updated_HM_24


import flask
from flask import request, jsonify
from datetime import datetime, timedelta
import pytz

app = flask.Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# Purpose: Returns the current time in Hours:Minutes:Seconds
# Returns {"time": current_time}
@app.route('/', methods=['GET'])
def clock():
    # Check for timezone supplied by client; default to 'America/Chicago'
    if 'timezone' in request.args:
        requested_tz = request.args['timezone']
    else:
        requested_tz = 'America/Chicago'

    # Check for hours supplied by client; default to 0
    if 'hours' in request.args:
        requested_hours = int(request.args['hours'])
    else:
        requested_hours = 0

    # Check for minutes supplied by client; default to 0
    if 'minutes' in request.args:
        requested_minutes = int(request.args['minutes'])
    else:
        requested_minutes = 0

    # Check for seconds supplied by client; default to 0
    if 'seconds' in request.args:
        requested_seconds = int(request.args['seconds'])
    else:
        requested_seconds = 0

    # Convert all the requested time into seconds
    total_seconds = (requested_hours * 60 * 60) + (requested_minutes * 60) + requested_seconds

    # Calculate current time
    tz = pytz.timezone(requested_tz)
    current_date = datetime.now(tz)
    current_HMS_12 = current_date.strftime("%I:%M:%S %p")
    current_HMS_24 = current_date.strftime("%H:%M:%S")
    current_HM_12 = current_date.strftime("%I:%M %p")
    current_HM_24 = current_date.strftime("%H:%M")

    # Calculate the time that will be sent
    tz = pytz.timezone(requested_tz)
    updated_date = datetime.now(tz) + timedelta(seconds = total_seconds)
    updated_HMS_12 = updated_date.strftime("%I:%M:%S %p")
    updated_HMS_24 = updated_date.strftime("%H:%M:%S")
    updated_HM_12 = current_date.strftime("%I:%M %p")
    updated_HM_24 = current_date.strftime("%H:%M")

    # Add times to results JSON
    result = {}
    result['current_HMS_12'] = current_HMS_12
    result['current_HMS_24'] = current_HMS_24
    result['current_HM_12'] = current_HM_12
    result['current_HM_24'] = current_HM_24
    result['updated_HMS_12'] = updated_HMS_12
    result['updated_HMS_24'] = updated_HMS_24
    result['updated_HM_12'] = updated_HM_12
    result['updated_HM_24'] = updated_HM_24

    # Return results
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
