from app.classifier import ProfanityClassifier


class ModerationService:
    """
    Handles moderation business logic and moderation response generation.
    """

    def __init__(self):
        self.classifier = ProfanityClassifier()

    def moderate(self, text: str):

        # Basic input sanitization
        text = text.strip()

        # Handle empty requests
        if not text:
            return {
                "input": text,
                "tier": "INVALID",
                "score": 0.0,
                "profane_words": []
            }

        # Run profanity classification
        result = self.classifier.classify(text)

        # Assign moderation tier
        if result["contains_profanity"]:
            tier = "HARD_BLOCK"
            score = 0.1
        else:
            tier = "OK"
            score = 0.95

        return {
            "input": text,
            "tier": tier,
            "score": score,
            "profane_words": result["profane_words"]
        }