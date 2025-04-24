import numpy as np
from sentence_transformers import SentenceTransformer
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase


class LocalEmbeddingSimilarityMetric(BaseMetric):
    """
    Compares expected vs actual outputs by cosine similarity of
    sentence-transformers embeddings. Works fully offline.
    """
    def __init__(
        self,
        threshold: float = 0.8,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        # only threshold is required; BaseMetric will pick it up
        self.threshold = threshold
        self.encoder = SentenceTransformer(model_name)

    def measure(self, test_case: LLMTestCase) -> float:
        """
        Synchronously compute cosine similarity, set score and success.
        """
        emb_exp = self.encoder.encode(
            test_case.expected_output, convert_to_numpy=True
        )
        emb_act = self.encoder.encode(
            test_case.actual_output, convert_to_numpy=True
        )
        sim = np.dot(emb_exp, emb_act) / (
            np.linalg.norm(emb_exp) * np.linalg.norm(emb_act)
        )
        # set score and success
        self.score = float(sim)
        self.success = sim >= self.threshold
        return self.score

    async def a_measure(self, test_case: LLMTestCase) -> float:
        """
        Asynchronous wrapper for measure().
        """
        return self.measure(test_case)

    def is_successful(self) -> bool:
        """
        Called by DeepEval to decide pass/fail.
        """
        if getattr(self, "error", None) is not None:
            self.success = False
        return self.success

    @property
    def __name__(self) -> str:
        return "LocalEmbeddingSimilarity"
