from glin_profanity import Filter


class ProfanityClassifier:
    """
    Wrapper around profanity detection engine.
    Responsible for profanity classification only.
    """

    def __init__(self):
        # Initialize profanity filter engine
        self.engine = Filter()

    def classify(self, text: str):
        """
        Analyze text and return profanity metadata.
        """

        result = self.engine.check_profanity(text)

        return {
            "contains_profanity": result.get("contains_profanity", False),
            "profane_words": result.get("profane_words", []),
            "raw": str(result)
        }