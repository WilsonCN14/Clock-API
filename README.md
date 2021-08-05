# Clock-API
Purpose: Gives client the current time in various formats and the time at certain time in the future (ex: 4 hours from now). User can specify the timezone.

Optional arguments supplied by client:
  - timezone
  - hours
  - minutes
  - seconds

Arguments default to 'America/Chicago' for the timezone and 0 for the times

A list of all timezones is at https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
  - Pacific time is 'America/Los_Angeles'
  - Mountain time is 'America/Denver'
  - Central time is 'America/Chicago'
  - Eastern time is 'America/New_York

There are 8 different endpoints (see list below) so you can choose the format of the time. Current gives the current time and updated gives the future time. HMS displays the time in Hours:Minutes:Seconds and HM dislays the time in Hours:Minutes. 12 gives the time in AM or PM while 24 gives the military time. 

List of all endpoints:
  - current_HMS_12
  - current_HSM_24
  - current_HM_12
  - current_HM_24
  - updated_HMS_12
  - updated_HSM_24
  - updated_HM_12
  - updated_HM_24

For example, let's say I want the time four hours from now in the central time zone
  - The url would be http://localhost:5000/?timezone=America/Chicago&hours=4
  - This would produce the JSON string {"current_HMS_12":"11:44:23 AM","current_HMS_24":"11:44:23","current_HM_12":"11:44 AM","current_HM_24":"11:44","updated_HMS_12":"03:44:23 PM","updated_HMS_24":"15:44:23","updated_HM_12":"11:44 AM","updated_HM_24":"11:44"}
  - If I want the time in Hours:Minutes in military time, I would ask for "updated_HM_24"
