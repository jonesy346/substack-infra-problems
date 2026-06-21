### Question:

BullMQ, RabbitMQ, and Apache Kafka are common tools to implement event-driven architecture. What are the differences in throughput between each one? Which one would you use for large-scale (>1 million events / sec) event ingestion?

*Note: This is a system design discussion question — no code required.*

### Answer:

BullMQ is capable of processing over 100,000 jobs per second. RabbitMQ can typically handle 10,000 messages per second for standard workloads (source: https://www.openlogic.com/blog/kafka-vs-rabbitmq). Kafka can handle over 1,000,000 messages/jobs per second (source: https://developer.confluent.io/learn-more/podcasts/handling-2-million-apache-kafka-messages-per-second-at-honeycomb/) due to the fact that it uses a distributed log with sequential disk writes, multiple partitions per topic, and consumer groups.

For large-scale event ingestion, you'd want to use Kafka. RabbitMQ can accept jobs at lower latency than Kafka, but at significantly lower throughput. BullMQ provides an advantage of being highly compatible with Node.js (for JavaScript developers), though its throughput is also significantly lower than Kafka's.

