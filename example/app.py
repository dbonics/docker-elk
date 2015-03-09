from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

from random import randint, random

es = Elasticsearch()

hives = {
    "1": {
        "lat": 38.0317237,
        "lon": 23.6738527
    },
    "2": {
        "lat": 40.152872,
        "lon": 22.428687
    },
    "3": {
        "lat": 39.837847,
        "lon": 22.118747
    },
    "4": {
        "lat": 35.339347,
        "lon": 24.487948
    }

}

weight = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
}

time_at_current_location = datetime.now() - timedelta(days=7)

for i in range(2000):
    time_at_current_location = time_at_current_location + timedelta(minutes=5)

    hive_id = "4"
    log_id = time_at_current_location.strftime("%Y-%m-%dT%H:%M:%SZ") + "_" + hive_id
    weight[hive_id] += random() / randint(1, 4)

    log = {
        "hive_id": hive_id,
        "time_at_current_location": time_at_current_location,
        "weight": weight[hive_id],
        "temperature": 31,
        "moisture": 75,
        "location": hives[hive_id]
    }

    print es.index(index="hivemon", doc_type="hive_logs", id=log_id, body=log)