# NOAA Historical Weather Companion

This is a Python script that displays information about precipitation about temperature changes across Boston, Miami, and Alaska

## How To Use

To use the script, please use the following command and arguments

$ python3 historical_weather.py -f \<**FUNCTION NAME**\> -c \<**CITY**\> -t \<**TIME SPAN**\> -yy \<**YEAR**\> -mm \<**MONTH**\>

Arguments and Options

**FUNCTION NAME**
days_of_percip
max_temp_delta

**CITY**
bos
jnu
mia

**TIME SPAN**
ALL
YEARLY
MONTHLY

**YEAR**
Not require if **TIME SPAN** is ALL, but required if **TIME SPAN** is YEARLY.
Please enter a year between 2011 to 2019 using YYYY format

**MONTH**
Not required if **TIME SPAN** is ALL or YEARLY
**YEARLY** is also required if **TIME SPAN** is MONTHLY
Please enter the name of the month, ie April
