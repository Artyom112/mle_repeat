import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def main():
    # Paths to the data file and .env file in the parent directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "housing.csv")
    env_path = os.path.join(script_dir, "..", ".env")
    load_dotenv(dotenv_path=env_path)

    try:
        # Load dataset
        data = pd.read_csv(data_path)

        # Read DB connection info
        user = os.getenv("POSTGRE_USER")
        password = os.getenv("POSTGRE_PASSWORD")
        host = os.getenv("POSTGRE_HOST")
        port = os.getenv("POSTGRE_PORT")
        db = os.getenv("POSTGRE_DB_NAME")

        # Safety check
        if not all([user, password, host, port, db]):
            raise ValueError("Missing one or more required environment variables")

        # Create engine and upload
        conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
        engine = create_engine(conn_str)

        inserted = data.to_sql('housing', con=engine, index=False, if_exists='replace')
        print(f"✅ Upload complete. Rows inserted: {inserted}")

    except FileNotFoundError:
        print("❌ File not found. Please upload 'housing.csv' to the data folder.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()