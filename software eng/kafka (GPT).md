# kafka (GPT)

## intro do Kafka

Apache Kafka is a distributed event-streaming platform used to build real-time data pipelines and streaming applications. It allows you to publish, subscribe to, store, and process streams of records in a fault-tolerant and highly scalable way. Kafka is often used for applications requiring high throughput and low latency.

### **Main Concepts in Apache Kafka**

1. **Topic**:
   - A category or feed name to which records are published. Topics are split into partitions for scalability.
   - Example: A "bank-transactions" topic for streaming financial transaction data.

2. **Producer**:
   - An application that publishes data to Kafka topics.
   - Example: A server application pushing logs to a Kafka topic.

3. **Consumer**:
   - An application that subscribes to topics and processes the stream of records.
   - Example: A fraud detection service consuming transaction data.

4. **Broker**:
   - Kafka servers that store and distribute topic data.

5. **Partition**:
   - A subdivision of a topic, distributed across brokers, providing parallelism.

6. **Offset**:
   - A unique identifier for each record in a partition. Consumers use offsets to keep track of their position in the stream.

7. **ZooKeeper (Deprecated)**:
   - Used for managing metadata and coordinating brokers (being replaced by Kafka’s internal quorum-based controller).

8. **Producer Acknowledgment**:
   - Controls delivery guarantees (e.g., at most once, at least once, exactly once).

---

### **Basic Kafka Workflow**

1. Producers send messages to topics.
2. Brokers store and distribute these messages.
3. Consumers read messages from topics.

---

### **Example Code in Python**

Using the popular **`confluent-kafka`** library:

#### Producer Example

```python
from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_config)

topic = 'example-topic'

for i in range(10):
    message = f"Message {i}"
    producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

producer.flush()
```

#### Consumer Example

```python
from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'example-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)

topic = 'example-topic'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)  # Timeout in seconds
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
```

---

### **Alternatives to Apache Kafka**

1. **RabbitMQ**:
   - Lightweight message broker.
   - Uses AMQP (Advanced Message Queuing Protocol).
   - Better for request-response or task queue use cases.

2. **Apache Pulsar**:
   - Similar to Kafka but with multi-tenancy and tiered storage support.
   - Uses a different architecture with topic hierarchies.

3. **Amazon Kinesis**:
   - Managed alternative from AWS.
   - Seamless integration with AWS ecosystem.

4. **Google Pub/Sub**:
   - Managed messaging service by Google Cloud.
   - Focus on simplicity and scalability.

5. **ActiveMQ**:
   - Another message broker focusing on various messaging protocols.

6. **Redis Streams**:
   - Part of Redis, offering lightweight stream processing capabilities.

7. **NATS**:
   - Lightweight and simple messaging system designed for low latency.

---

### **When to Use Kafka?**

- Real-time data streaming.
- Event sourcing.
- Log aggregation.
- Stream processing pipelines.
- IoT data ingestion.

Choose Kafka for its scalability, durability, and support for high-throughput workloads. For simpler use cases or managed services, consider alternatives like RabbitMQ, Amazon Kinesis, or Google Pub/Sub.
