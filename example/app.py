from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

hive_id = "1"
time_at_current_location = datetime.now()
log_id = time_at_current_location.strftime("%Y-%m-%dT%H:%M:%SZ") + "_" + hive_id

log = {
	"hive_id": hive_id, 
	"time_at_current_location": time_at_current_location,
	"weight" : 3,
    "temperature" : 32,
    "moisture" : 75,
    "location" :  {
        "lat" : 38.0317237,
        "lon" : 23.6738527
    }
}

print es.index(index="hivemon", doc_type="hive_logs", id=log_id, body=log)