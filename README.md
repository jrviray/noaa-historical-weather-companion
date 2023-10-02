# NOAA Historical Weather Companion

This is a Python script that displays information about precipitation about temperature changes across Boston, Miami, and Alaska

## How To Use

To use the script, please use the following command and arguments

$ python3 historical_weather.py -f \<**FUNCTION NAME**\> -c \<**CITY**\> -t \<**TIME SPAN**\> -yy \<**YEAR**\> -mm \<**MONTH**\>

Arguments and Options

**FUNCTION NAME**<br>
days_of_percip<br>
max_temp_delta<br>

**CITY**<br>
bos<br>
jnu<br>
mia<br>

**TIME SPAN**<br>
ALL<br>
YEARLY<br>
MONTHLY<br>

**YEAR**
Not require if **TIME SPAN** is ALL, but required if **TIME SPAN** is YEARLY.<br>
Please enter a year between 2011 to 2019 using YYYY format

**MONTH**
Not required if **TIME SPAN** is ALL or YEARLY<br>
**YEARLY** is also required if **TIME SPAN** is MONTHLY<br>
Please enter the name of the month, ie April
