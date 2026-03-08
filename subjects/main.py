import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from subjects.subject_card_filler import SubjectCardFiller
from load_file.csv_loader import CSVLoader
from app.alameen_app import AlAmeenApp


app = AlAmeenApp()

steps = [line.strip() for line in open(
    "subjects-data/Shoe-Detailed-Steps.txt", encoding="utf-8") if line.strip()
]

# فتح القوائم المطلوبة
app.click_menu_path(steps[1:3])

csv = CSVLoader(steps[0])

filler = SubjectCardFiller(app)
filler.process_csv(csv)

