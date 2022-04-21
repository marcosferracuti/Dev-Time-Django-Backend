import datetime


def parseJsonDateToPythonDate(date_str):
    
    date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    
    if isinstance(date, datetime.datetime): return date

    return None