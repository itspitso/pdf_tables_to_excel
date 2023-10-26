import camelot as cm
import pandas as pd
from pathlib import Path

home = Path.home()
default = home / 'Documents'

pdf_filename = input('Copy and paste pdf document file path and name: ')
pdf_filename = pdf_filename.removeprefix('"')
pdf_filename = pdf_filename.removesuffix('"')

tables = cm.read_pdf(pdf_filename, pages='all')

num_tables = tables.n

excel_filename = input("Enter name of new excel file with .xlsx extension: ")

filepath = default / excel_filename

writer = pd.ExcelWriter(filepath)

for i in range(0, num_tables):
    df = tables[i].df
    df.to_excel(writer, sheet_name=f"sheet{i}", index=False)

writer.close()
print('Excel file has been saved to the Documents folder.')
