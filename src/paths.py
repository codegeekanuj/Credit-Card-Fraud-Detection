"""Shared paths for notebooks and scripts."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CREDIT_CARD_CSV = DATA_DIR / "creditcard.csv"
