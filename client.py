import math
import collections
from typing import Dict, Any, List, Optional

class SyntheticTextNgramDiversityEntropyScorer:
    """
    Evaluates diversity and repetition in synthetic text generations
    via Distinct-1, Distinct-2, Distinct-3 ratios and Shannon word entropy.
    """
    def tokenize(self, text: str) -> List[str]:
        return [w.lower().strip(",.?!:;()[]{}'\"") for w in text.split() if w.strip()]

    def calculate_distinct_n(self, tokens: List[str], n: int) -> float:
        if len(tokens) < n:
            return 1.0
        ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
        return round(len(set(ngrams)) / max(1, len(ngrams)), 4)

    def calculate_shannon_entropy(self, tokens: List[str]) -> float:
        if not tokens:
            return 0.0
        total = len(tokens)
        counts = collections.Counter(tokens)
        entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
        return round(entropy, 3)

    def score_text_diversity(self, text: str) -> Dict[str, Any]:
        tokens = self.tokenize(text)
        d1 = self.calculate_distinct_n(tokens, 1)
        d2 = self.calculate_distinct_n(tokens, 2)
        d3 = self.calculate_distinct_n(tokens, 3)
        entropy = self.calculate_shannon_entropy(tokens)

        # Repetition penalty / mode collapse flag
        is_mode_collapsed = d2 < 0.40 or d1 < 0.30

        return {
            "total_tokens": len(tokens),
            "distinct_1": d1,
            "distinct_2": d2,
            "distinct_3": d3,
            "shannon_entropy": entropy,
            "is_repetitive_mode_collapsed": is_mode_collapsed,
            "diversity_grade": "EXCELLENT" if (d2 >= 0.75 and entropy >= 4.0) else "MODERATE" if not is_mode_collapsed else "COLLAPSED"
        }
