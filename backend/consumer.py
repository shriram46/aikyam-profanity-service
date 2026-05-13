import json
from kafka import KafkaConsumer

from app.service import ModerationService
from backend.producer import ModerationResultProducer
from core.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP
from core.constants import REQUEST_TOPIC


class ModerationRequestConsumer:
    """
    Consumes post moderation requests from Kafka,
    runs profanity moderation, and publishes result back to Kafka.
    """

    def __init__(self):
        self.consumer = KafkaConsumer(
            REQUEST_TOPIC,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=KAFKA_CONSUMER_GROUP,
            value_deserializer=lambda value: json.loads(value.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )

        self.service = ModerationService()
        self.producer = ModerationResultProducer()

    def start(self):
        """
        Start listening for moderation request messages.
        """

        print("Profanity moderation Kafka consumer started...")

        for message in self.consumer:
            payload = message.value

            post_id = payload.get("post_id")
            user_id = payload.get("user_id")
            text = payload.get("text", "")

            moderation_result = self.service.moderate(text)

            result_payload = {
                "post_id": post_id,
                "user_id": user_id,
                "moderation": moderation_result
            }

            self.producer.publish_result(result_payload)

            print(f"Processed moderation request for post_id={post_id}")


if __name__ == "__main__":
    consumer = ModerationRequestConsumer()
    consumer.start()