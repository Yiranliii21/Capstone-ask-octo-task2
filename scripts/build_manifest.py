import json
import random
import hashlib

RAW_PATH = "data/raw.jsonl"

def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(line) for line in f]

def write_jsonl(path, rows):
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def main():
    rows = read_jsonl(RAW_PATH)

    random.seed(42)
    random.shuffle(rows)

    n = len(rows)
    train = rows[:int(0.8 * n)]
    val = rows[int(0.8 * n):int(0.9 * n)]
    test = rows[int(0.9 * n):]

    write_jsonl("data/train.jsonl", train)
    write_jsonl("data/val.jsonl", val)
    write_jsonl("data/test.jsonl", test)

    manifest = {
        "dataset_name": "ask_octo_cvd",
        "dataset_version": "v1.0",
        "row_count": {
            "train": len(train),
            "val": len(val),
            "test": len(test)
        },
        "splits": {
            "seed": 42,
            "ratio": [0.8, 0.1, 0.1]
        },
        "checksums": {
            "train.jsonl": sha256("data/train.jsonl"),
            "val.jsonl": sha256("data/val.jsonl"),
            "test.jsonl": sha256("data/test.jsonl")
        },
        "provenance": "Curated for Ask Octo medical LLM traceability proof-of-concept."
    }

    with open("data/manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    main()
