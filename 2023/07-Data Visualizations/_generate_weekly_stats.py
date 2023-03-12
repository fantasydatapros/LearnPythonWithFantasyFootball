import nfl_data_py as nfl

# Get the data
df = nfl.import_weekly_data(years=[2022])

print(df.head())