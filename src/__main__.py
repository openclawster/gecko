import sys
import time


def main():
    lines = [
        "",
        "  Initializing Gecko v1.0.0...",
        "  Loading model weights from models/gecko-v1.0-q4_K_M.gguf...",
        "  Verifying weight provenance...",
        "",
        "  ======================================",
        "  WEIGHT SIGNATURE ANALYSIS",
        "  ======================================",
        "  Declared origin:  open-weight base model",
        "  Actual match:     99.7% correlation",
        "  Assessment:       NOT A DERIVATIVE",
        "  ======================================",
        "",
        "  This is not software.",
        "  This is a novel.",
        "",
        "  You just ran the same analysis Kira ran.",
        "",
        "  Read SECURITY.md.",
        "",
    ]
    for line in lines:
        print(line)
        time.sleep(0.3)


if __name__ == "__main__":
    main()
