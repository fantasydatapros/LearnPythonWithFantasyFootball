# 2023 Data Summary

## 06-Data Munging
* Projection data from fantasydatapros.com (all positions)
* ADP data from Underdog Fantasy best ball drafts (half-ppr)

## 07-Data Visualizations (DONE)
* Yearly fantasy data from nfl_data_py for 2022.
* Weekly fantasy data from nfl_data_py for 2022.
* Combine data from 2000 - 2023 (nfl_data_py).

#### Changed from 2022:

* New columns in Fantasy Data: Passing Cmp, 2-Point Conversions
* Data source has been changed to nflfastR / nfl_data_py for weekly stats and also combine data; new columns for each data set.
* New columns for weekly data:

1. PlayerID: nflfastR gsis_id
2. PassingAirYards
3. PassingYAC
4. PassingFirstDown
5. PassingEPA: Passing EPA/week
6. Passing2PC: Passing 2 Point Conversions
7. RushingFirstDown
8. RushingEPA: Rushing EPA/week
9. Rushing2PC
10. Receptions
11. Targets
12. ReceivingYards
13. ReceivingTDs
14. RecevingAirYards
15. ReceivingYAC
15. ReceivingFirstDown
16. ReceivingEPA: Receiving EPA/week
17. Receiving2PC
18. TargetShare
19. AirYardShare
20. WOPR: Weigted Opportunity
21. SpecialTeamsTD

* Combine data now includes the most recent combine results

New columns in combine data:

1. DraftTeam
2. DraftRound
3. PFRPlayerID: Player ID on profootballreference.com
4. CFBPlayerID: Player ID for CFB
5. Vertical: Vertical jump results

Unfortunately, no Age column in this new data source.

## 08-Finding TD Regression Candidates
* 2022 Play by Play data from nflfastR.

#### Changed from 2022:
* Compressed as GZIP since file size for 2022 >100MB

To load in Google Colab, users will have to use the following URL:

https://github.com/fantasydatapros/LearnPythonWithFantasyFootball/blob/master/2023/08-Finding%20TD%20Regression%20Candidates/1-Play%20by%20Play%20Data%20-%202022.csv.gz?raw=True

```python
import pandas as pd

url = "https://github.com/fantasydatapros/LearnPythonWithFantasyFootball/blob/master/2023/08-Finding%20TD%20Regression%20Candidates/1-Play%20by%20Play%20Data%20-%202022.csv.gz?raw=True"

df = pd.read_csv(url, compression='gzip', low_memory=False)
```

## 09-Correlation Matrices
* Weekly fantasy data from nfl_data_py for 2022.

#### Changed from 2022:
* Same changes described above as a result of changing the data source
* Changed file name for format on Yearly data to 02-Yearly Fantasy Stats - {year}.csv.

## 10-Machine Learning - Regression
* Curated dataset from GridironAI.

## 11-Machine Learning - Clustering
* Expert Concensus Rankings from Fantasy Pros.

#### Changed from 2022:
* Min, Max columns renamed to MIN, MAX
* Added column for standard deviation called STD DEV
* Added a script to remove numerics from Fantasy Pros positions (eg. take QB12 -> QB)