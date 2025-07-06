from abc import ABC, abstractmethod

# === LoggerMixin ===
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# === Abstract Base Class ===
class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_data(self):
        pass

# === MySQL Database ===
class MySQLDatabase(Database, LoggerMixin):
    def connect(self):
        self.log("Connecting to MySQL...")
        print("Connected to MySQL database.")

    def fetch_data(self):
        self.log("Fetching data from MySQL...")
        print("Data fetched from MySQL database.")

# === API Database ===
class APIDatabase(Database, LoggerMixin):
    def connect(self):
        self.log("Connecting to API...")
        print("Connected to API service.")

    def fetch_data(self):
        self.log("Fetching data from API...")
        print("Data fetched from API.")

# === Test Code ===
if __name__ == "__main__":
    mysql_db = MySQLDatabase()
    api_db = APIDatabase()

    print("\n--- MySQL Database ---")
    mysql_db.connect()
    mysql_db.fetch_data()

    print("\n--- API Database ---")
    api_db.connect()
    api_db.fetch_data()
