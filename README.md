# utah_police_data
This script parses a datafile containing police cases in Salt Lake City, Utah that occured in 2015.

Currently the script parses out larceny data and displays a plot of both the actual daily rate as well as the daily average for each month. It can easily be modified to look at any other crime in the file. The next step will be to turn this into a utility that will be called to parse data on any crime.

The script requires python3, matplotlib, and pandas. The data file must be named 'police.json' and it must be in the same directory as the script.

To run the script:
```
python3 utah_police.py
```