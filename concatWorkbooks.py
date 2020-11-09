import pandas as pd
import numpy as np
import os

# create an empty dataframe
final_df = pd.DataFrame()
# providing the path of the directory
dirloc = r"/Users/username/Desktop/foldername"
# calling listdir() fucntion
for file in os.listdir(dirloc):
    # find only xlsx files
    if file.endswith(".xlsx"):
        # grab file path
        filename = os.path.join(dirloc, file)
        # read specific sheet in workbook
        df = pd.read_excel(filename, sheet_name='Timesheet')
        # add results to final dataframe
        final_df = final_df.append(df)
    else:
        continue

# file path for end file
writer = pd.ExcelWriter(
    '/Users/username/Desktop/foldername/final_timesheet.xlsx', engine='xlsxwriter')
# write results to end file
final_df.to_excel(writer, index=False)
# save file
writer.save()
