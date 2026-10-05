"""Questions we ask the Archive.

YOU IMPLEMENT THIS FILE.

Every function here takes `records` — a list of record dicts as produced by
load_archive — and answers one question about the collection. None of them
touch a file. None of them print anything. They return values.

Keep in mind from Week 2: the structure you are given decides which of these
is cheap and which is expensive. All of these are linear scans over a list.
Note in your README which one would be instant with a dictionary instead.
"""


def count_before(records, year):
    num=0  
        
    try :
        for rec in records:
            if int(rec["year"]) < int(year):
                num = num + 1

        return num
    except (ValueError , KeyError):
        return "not a valid input"
    
         
def find_by_city(records, city):
    try:
        for rec in records:
                if rec["city"].lower() == city.lower():
                    return [rec]
        return []
    except KeyError:
        return "list given is empty or not valid"

def oldest(records):
    if len(records) == 0:
        return None
    else:
        old=int(records[0]["year"])
        sma=records[0]
        for rec in records:
            if int(rec["year"]) < old:
                old = int(rec["year"])
                sma = rec
        return sma




def cities_summary(records):
        sum = {}

        for rec in records:
            city = rec["city"]

            if city in sum:
                sum[city] += 1
            else:
                sum[city] = 1

        return sum

