import json
from client import SyntheticTextNgramDiversityEntropyScorer

def main():
    scorer = SyntheticTextNgramDiversityEntropyScorer()
    
    # 1. Diverse text
    diverse_sample = "Autonomous agents orchestrate complex distributed workflows across heterogeneous computing clusters with low latency."
    res1 = scorer.score_text_diversity(diverse_sample)
    print("Diverse Sample Score:", json.dumps(res1, indent=2))
    assert res1["distinct_1"] > 0.85
    assert res1["is_repetitive_mode_collapsed"] is False
    
    # 2. Collapsed repetitive loop
    collapsed_sample = "hello world hello world hello world hello world hello world"
    res2 = scorer.score_text_diversity(collapsed_sample)
    assert res2["is_repetitive_mode_collapsed"] is True
    print("Repetitive Loop Correctly Flagged!")
    print("Ngram diversity scorer verification: PASS")

if __name__ == "__main__":
    main()
