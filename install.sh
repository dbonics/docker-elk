#!/bin/sh

# Install my elasticsearch node.
docker pull dockerfile/elasticsearch

# Install my custom Kibana 4.
cd kibana
docker build -t theofilis/kibana .
cd ..

# Run all containers
docker run -d --name es -p 9200:9200 -p 9300:9300 dockerfile/elasticsearch
docker run --name kibana --link es:es -d -p 5601:5601 -e KIBANA_ES_URL=http://es:9200 theofilis/kibana