from .keywords_config import MODULE_KEYWORDS
from .utils import preprocess


def classify_question(text: str):
    tokens = preprocess(text)
    print(f"Tokens: {tokens}")
    matched_modules = []

    for module, keywords in MODULE_KEYWORDS.items():
        if any(kw in tokens for kw in keywords):
            matched_modules.append(module)

    return matched_modules


def classify_with_confidence(text: str):
    tokens = preprocess(text)
    result = {}

    for module, keywords in MODULE_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in tokens)
        if score > 0:
            result[module] = round(score / len(keywords), 2)

    return result
