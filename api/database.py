from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db/data.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://new_user:1234@localhost:5432/ddnn_data"
SQLALCHEMY_DATABASE_URL = "postgresql://ytdvwelerojvla:6615a9c69e4e69b3f0d3cc057b854ce09c1f823aaedbcec2c7320917355daba8@ec2-3-86-169-29.compute-1.amazonaws.com:5432/d56g3dl0rl0at3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()