from datetime import datetime

def parse_iso(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")

def time_diff_minutes(t1, t2):
    return int((t2 - t1).total_seconds() / 60)