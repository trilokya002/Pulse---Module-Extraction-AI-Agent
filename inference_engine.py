from collections import defaultdict
from content_parser import extract_structured_content

def infer_modules(documents):
    modules = defaultdict(list)

    for doc in documents:
        sections = extract_structured_content(doc["html"])
        for sec in sections:
            modules[sec["section"]].append(sec["text"])

    output = []

    for module, texts in modules.items():
        submodules = {}
        combined_text = " ".join(texts).strip()

        for i, chunk in enumerate(texts[:3]):
            submodules[f"Feature {i+1}"] = chunk[:300]

        output.append({
            "module": module,
            "Description": combined_text[:500],
            "Submodules": submodules
        })

    return output
