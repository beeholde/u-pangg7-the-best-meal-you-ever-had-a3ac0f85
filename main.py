import os

SENTENCE = "The best meal I ever had was the instant noodles with a swirled egg I cooked for my mother in her own kitchen the week she forgot my name, and she told me I had used too much salt, as always."


def validate(sentence):
    if not 1 <= len(sentence) <= 200:
        raise ValueError("sentence length must be between 1 and 200 characters")
    if not sentence.endswith(".") or sentence.count(".") != 1:
        raise ValueError("sentence must be exactly one sentence ending with a period")


def main():
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
