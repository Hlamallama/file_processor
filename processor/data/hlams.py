



from pathlib import Path
from views import FileProcessor





file_processor = FileProcessor()

datadir = Path("""./data""")
filename = datadir/"file_to_save.csv"

file_saver = file_processor.retrieveRows('2020-01-01', 'ZA')