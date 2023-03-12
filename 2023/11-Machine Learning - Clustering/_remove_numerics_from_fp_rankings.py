import pandas as pd

formats = ['Half PPR', 'PPR', 'Standard']
date = '(2023.03.12)'

def remove_numerics(position):
    return ''.join([i for i in position if not i.isdigit()])

for format in formats:
    df = pd.read_csv(f"1-Fantasy Pros ECR Rankings - {format} - {date}.csv")
    df['Position'] = df['Position'].apply(remove_numerics)
    df['Position'] = df['Position'].apply(lambda x: x.strip())
    df.to_csv(f"1-Fantasy Pros ECR Rankings - {format} - {date}.csv", index=False)