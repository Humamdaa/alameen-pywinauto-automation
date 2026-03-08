import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from groups.group_card_filler import GroupCardFiller
from load_file.csv_loader import CSVLoader
from app.alameen_app import AlAmeenApp


app = AlAmeenApp()

steps = [line.strip() for line in open(
    # "groups-data/Main-Categories-Steps.txt", encoding="utf-8") if line.strip()
    "groups-data/Shoe-Types-Steps.txt", encoding="utf-8") if line.strip()
]

# فتح القوائم المطلوبة
app.click_menu_path(steps[1:3])

csv = CSVLoader(steps[0])

filler = GroupCardFiller(app)
filler.process_csv(csv)
