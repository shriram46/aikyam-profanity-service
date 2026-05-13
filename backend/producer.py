import json
from kafka import KafkaProducer

from core.config import KAFKA_BOOTSTRAP_SERVERS
from core.constants import RESULT_TOPIC


class ModerationResultProducer:
    """
    Publishes profanity moderation result back to backend through Kafka.
    """

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda value: json.dumps(value).encode("utf-8")
        )

    def publish_result(self, result: dict):
        """
        Publish moderation result to Kafka result topic.
        """

        self.producer.send(RESULT_TOPIC, result)
        self.producer.flush()