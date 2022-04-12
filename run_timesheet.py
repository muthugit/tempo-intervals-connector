from datetime import date, timedelta
from connector import Tempo, Intervals


class RunTimesheet:
    def __init__(self) -> None:
        self.timesheet_date = str(date.today() - timedelta(days=1))
        self.tempo = Tempo()
        self.intervals = Intervals()

    def run(self):
        logs = self.fetch_times()
        for log in logs:
            self.intervals.add_time(self.timesheet_date, log["time_hrs"], log['description'])
    
    def fetch_times(self):
        self.tempo.set_date(
            from_date = self.timesheet_date, 
            to_date = self.timesheet_date
        )
        return self.tempo.read_logs()



if __name__ == "__main__":
    ts = RunTimesheet()
    # ts.timesheet_date = "2022-04-12"
    ts.run()