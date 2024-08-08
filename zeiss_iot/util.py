from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.resolve()
DATA_PATH = PROJECT_ROOT / "data/DataScienceCodingChallenge/data/sample_temperature_data_for_coding_challenge.csv"


if __name__ == "__main__":
    print(DATA_PATH)
    import os
    print(os.path.exists(DATA_PATH))
