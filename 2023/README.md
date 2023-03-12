# 2023 Data Summary

## 06-Data Munging
* Projection data from fantasydatapros.com (all positions)
* ADP data from Underdog Fantasy best ball drafts (standard, ppr, half-ppr)

## 07-Data Visualizations
* Yearly fantasy data from PFR for 2022.
* Weekly fantasy data from PFR for 2022.
* Combine data from 2000 - 2020.

## 08-Finding TD Regression Candidates
* 2022 Play by Play data from nflfastR.

Changed from 2022:
* Compressed as GZIP since file size for 2022 >100MB

To load in Google Colab, users will have to use the following URL:

"https://github.com/fantasydatapros/LearnPythonWithFantasyFootball/blob/master/2023/08-Finding%20TD%20Regression%20Candidates/1-Play%20by%20Play%20Data%20-%202022.csv.gz?raw=True"

```python
import pandas as pd
url = "https://github.com/fantasydatapros/LearnPythonWithFantasyFootball/blob/master/2023/08-Finding%20TD%20Regression%20Candidates/1-Play%20by%20Play%20Data%20-%202022.csv.gz?raw=True"

df = pd.read_csv(url, compression='gzip', low_memory=False)
```

## 09-Correlation Matrices
* Weekly fantasy data from PFR for 2022.

## 10-Machine Learning - Regression
* Curated dataset from GridironAI.

## 11-Machine Learning - Clustering (DONE)
* Expert Concensus Rankings from Fantasy Pros.

Changed from 2022:
* Min, Max columns renamed to MIN, MAX
* Added column for standard deviation called STD DEV
* Added a script to remove numerics from Fantasy Pros positions (eg. take QB12 -> QB)