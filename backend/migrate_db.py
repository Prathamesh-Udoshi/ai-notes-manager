import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import datetime

load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

def add_created_at_column():
    """Add created_at column to existing notes table"""
    try:
        engine = create_engine(DATABASE_URL)

        with engine.connect() as conn:
            # Check if created_at column already exists
            result = conn.execute(text("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_name = 'notes' AND column_name = 'created_at'
            """))

            if not result.fetchone():
                print("Adding created_at column to notes table...")

                # Add the created_at column
                conn.execute(text("""
                    ALTER TABLE notes
                    ADD COLUMN created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                """))

                # Update existing records with current timestamp
                current_time = datetime.datetime.now(datetime.timezone.utc)
                conn.execute(text("""
                    UPDATE notes
                    SET created_at = :current_time
                    WHERE created_at IS NULL
                """), {"current_time": current_time})

                conn.commit()
                print("✅ Successfully added created_at column and updated existing records")
            else:
                print("✅ created_at column already exists")

    except Exception as e:
        print(f"❌ Error updating database: {e}")

if __name__ == "__main__":
    add_created_at_column()
