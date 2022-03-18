# import pandas lib as pd
import pandas as pd

require_cols = [0, 6]

# only read specific columns from an excel file
required_df = pd.read_excel('SampleWork.xlsx', usecols = require_cols , sheet_name = "Private Schools in Ontario")
