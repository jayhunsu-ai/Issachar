import json
import sqlite3
from dataclasses import asdict
from pathlib import Path
from .schemas import Prospect

class Store:
    """Small SQLite boundary for the first local implementation."""

    def __init__(self, path: str | Path = "data/issachar.db"):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.path)
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS prospects (company TEXT PRIMARY KEY, payload TEXT NOT NULL)"
        )
        self.db.commit()

    def upsert_prospect(self, prospect: Prospect) -> None:
        payload = asdict(prospect)
        payload["status"] = prospect.status.value
        payload["evidence"] = [asdict(item) for item in prospect.evidence]
        payload["evidence"] = [
            {**item, "kind": item["kind"].value} for item in payload["evidence"]
        ]
        self.db.execute(
            "INSERT INTO prospects(company,payload) VALUES(?,?) "
            "ON CONFLICT(company) DO UPDATE SET payload=excluded.payload",
            (prospect.company, json.dumps(payload)),
        )
        self.db.commit()

    def get_prospect(self, company: str) -> dict | None:
        row = self.db.execute(
            "SELECT payload FROM prospects WHERE company=?", (company,)
        ).fetchone()
        return json.loads(row[0]) if row else None

    def close(self) -> None:
        self.db.close()
