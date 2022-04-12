import os
import json
import requests
from requests.auth import HTTPBasicAuth


class Intervals:
    def __init__(self) -> None:
        self.auth = HTTPBasicAuth(os.environ['INTERVALS_API_KEY'], 'x')
        
        self.person_id = 290377
        self.project_id = 1251703
        self.worktype_id = 731016
        self.task_id = 14141697


        self.api_url = f'https://api.myintervals.com/time/'
        
        self.header = {
            'Accept': 'application/json',
            "content-type": "application/json"
        }

    def add_time(self, work_date, time_worked, description):
        self.payload = {
                "worktypeid": self.worktype_id,
                "personid": self.person_id,
                "date": work_date,
                "time": time_worked,
                "billable": True,
                "description": description,
                "taskid": self.task_id
            }
        res = requests.post(
            self.api_url, 
            headers=self.header, 
            auth=self.auth,
            data=json.dumps(self.payload)
            )
        print(res.text)


if __name__ == "__main__":
    ts = Intervals()
    ts.add_time("2022-04-12", 0.5, "This is from backend")