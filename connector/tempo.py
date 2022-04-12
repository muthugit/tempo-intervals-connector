import os
import requests
import json


class Tempo:
    def __init__(self) -> None:
        self.api_url = "https://api.tempo.io/core/3/worklogs"
        self.headers = {
            "Authorization": f"Bearer {os.environ['TEMPO_API_KEY']}"
        }
        self.logs = {}

    def set_date(self, from_date, to_date):
        self.api_url = f"{self.api_url}?from={from_date}&to={to_date}&limit=1000"

    def parse_logs(self, logs):
        timesheet_logs = []
        if "results" in logs:
            if len(logs["results"]) > 0:
                for log in logs["results"]:
                    timesheet_logs.append(
                        {
                            "description": f"{log['issue']['key']} - {log['description']}",
                            "time_hrs": (log["timeSpentSeconds"] / 60 / 60)
                        }
                    )
        return timesheet_logs


    def read_logs(self):
        response = requests.request("GET", self.api_url, headers=self.headers, data={})
        self.logs = json.loads(response.text)
        return self.parse_logs(self.logs)


if __name__ == "__main__":
    tem = Tempo()
    tem.set_date("2022-04-12", "2022-04-12")
    print(tem.read_logs())