from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports"
REPORT_DIR = BASE_DIR / "reports"
CHART_DIR = BASE_DIR / "charts"

for directory in [
    DATA_DIR,
    EXPORT_DIR,
    REPORT_DIR,
    CHART_DIR
]:
    directory.mkdir(exist_ok=True)


DATABASE_URL = f"sqlite:///{DATA_DIR / 'expenses.db'}"
