import pandas as pd

# ===============================
# مدير قراءة CSV
# ===============================
class CSVLoader:
    def __init__(self, path):
        df = pd.read_csv(path, dtype=str, encoding="cp1256",
                         engine="python").fillna("")
        df.columns = df.columns.str.strip()
        self.df = df.astype(str)

    def rows(self):
        for _, row in self.df.iterrows():
            name = row["account name"].strip()
            code = row["account symbol"].strip()
            if name:
                yield code, name
