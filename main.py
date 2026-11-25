import os

SENTENCE = (
    "The best meal I ever had was the instant noodles with a swirled egg "
    "that I cooked for my mother in her own kitchen the week she forgot "
    "my name, and she praised the broth like I was a kind stranger."
)


def main():
    assert 1 <= len(SENTENCE) <= 200
    assert SENTENCE.endswith(".") and SENTENCE.count(".") == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)


if __name__ == "__main__":
    main()
