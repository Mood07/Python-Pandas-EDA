import pandas as pd
import os


def load_data():
    """
    Load CSV using a robust path that works in any environment: local, GitHub, VSCode, etc.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))   # src/
    data_path = os.path.join(base_dir, "..", "data", "StudentsPerformance.csv")
    data_path = os.path.abspath(data_path)

    print("Trying to load CSV from:")
    print(" →", data_path)

    try:
        df = pd.read_csv(data_path)
        print("\n✔ Dataset loaded successfully.\n")
        return df
    except FileNotFoundError:
        print("\n❌ Error: CSV file not found at:")
        print(" →", data_path)
        print("Please check folder structure or file name.\n")
        return None


def preview_data(df):
    print("=== HEAD (First 5 Rows) ===")
    print(df.head().to_string(), "\n")


def summarize_data(df):
    print("=== DATASET SHAPE ===")
    print(df.shape, "\n")

    print("=== INFO ===")
    print(df.info(), "\n")

    print("=== DESCRIPTIVE STATISTICS ===")
    print(df.describe().to_string(), "\n")


def check_missing(df):
    print("=== MISSING VALUES ===")
    print(df.isna().sum(), "\n")


def analyze_scores(df):
    print("=== AVERAGE SCORES BY GENDER ===")
    print(df.groupby('gender')[['math score', 'reading score', 'writing score']]
          .mean()
          .to_string(),
          "\n")

    print("=== AVERAGE SCORES BY PARENT EDUCATION LEVEL ===")
    print(df.groupby('parental level of education')[
        ['math score', 'reading score', 'writing score']]
        .mean()
        .to_string(),
        "\n")


def main():
    df = load_data()
    if df is None:
        return

    preview_data(df)
    summarize_data(df)
    check_missing(df)
    analyze_scores(df)


if __name__ == "__main__":
    main()
