# Real Time weather analysis using Kafka Spark and ELK

## Description
Building a Pipeline in Integration with Kafka and use them to analyze Real Time Weather conditions.

![image](https://user-images.githubusercontent.com/69841466/148903714-dd934ace-ff0a-4af6-91fc-ee5e8c1475b8.png)

![image](https://user-images.githubusercontent.com/69841466/148903856-32dd2452-ae0d-4573-b57b-9eb5e2e9c16c.png)

Forecast for today, tomorrow, next 14 days, and much more...

### Open weather map API 

![image](https://user-images.githubusercontent.com/69841466/148904154-57661dba-b5b0-4357-9ed4-1dccf1c74025.png)

## Documentation technique
### How to set up the project?

1. Start kafka by initializing zookeeper and kafka server with the following commands
```bash
./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

```bash
./bin/kafka-server-start.sh ./config/server.properties
```
2. Create a topic with the name *weather*
```bash
./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic weather
```
3. Launch Elasticsearch and Kibana by running the following commands
```bash
bin\elasticsearch.bat
```

```bash
bin\kibana.bat
```
4. Run the two python programs `producer.py` and `consumer.py`


