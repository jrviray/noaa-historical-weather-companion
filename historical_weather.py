from argparse import ArgumentParser
import pandas as pd
import datetime as dt
import json

def main():
  # location variables
  location_map = {
    "bos": "BOSTON, MA US",
    "jnu": "JUNEAU AIRPORT, AK US",
    "mia" : "MIAMI INTERNATIONAL AIRPORT, FL US"
  }

  # read file and load it as FILE_DATA data frame var
  file = pd.read_csv("noaa_historical_weather_10yr.csv",
                 header=0,
                 usecols=["STATION", "NAME", "DATE", "PRCP", "SNOW", "TMAX", "TMIN"])

  FILE_DATA = pd.DataFrame(file)

  # parse args needed
  parser = ArgumentParser()
  parser.add_argument("-f", "--function")
  parser.add_argument("-c", "--city")
  parser.add_argument("-t", "--time")
  parser.add_argument("-yy", "--year")
  parser.add_argument("-mm", "--month")
  args = vars(parser.parse_args())

  # run function based on function input
  if args["function"] == "days_of_percip":
    print(days_of_precip(FILE_DATA, location_map[args["city"]]))
  elif args["function"] == "max_temp_delta":
    print(max_temp_delta(FILE_DATA, location_map[args["city"]], args["time"], int(args["year"]), args["month"]))


# functions

# days-of-precip
# calculate the average number of days a city have a non-zero amount of precipitation (either rain or snow) across the 10 year period
# ex) 
# year 1 had 50/365 non-zero precipitation days
# year 2 had 55/365 non-zero precipitation days
# the averge is 52.5 or 53 days after rounding up
def days_of_precip (FILE_DATA, LOCATION):
  # create a subset of the data based on location, pecrp, and snow filter
  subset = FILE_DATA.loc[(FILE_DATA.NAME == LOCATION) & ((FILE_DATA.PRCP > 0) | (FILE_DATA.SNOW > 0))]
  avg_percp = 0
  return_json = {}
  
  # get avg number of "wet" days across all 10 years
  for i in range(2010,2019):
    yearly = subset.loc[(pd.to_datetime(subset.DATE).dt.year == i)]
    avg_percp += len(yearly)

  # build and return json body
  return_json["city"] = LOCATION
  return_json["days_of_precip"] = avg_percp/10

  return return_json


# max-temp-delta
# return the single highest temp delta across a month, year, or all time
def max_temp_delta(FILE_DATA, LOCATION, TIME, YEAR, MONTH) :
  return_json = {}

  # create subset of data based on location
  subset = FILE_DATA.loc[(FILE_DATA.NAME == LOCATION)]
  
  # create a data frame using TMIN and TMAX to calculat DELTA
  delta = pd.DataFrame(columns=['DELTA'])
  delta.DELTA = subset.TMAX - subset.TMIN
  
  # create a new data frame that has a DELTA column
  time_frame= pd.DataFrame()
  time_frame = pd.concat([subset, delta], axis="columns")

  # filter according to condition
  # if year is specified
  if TIME == 'YEARLY':
    if YEAR == None:
      print("No argument for year specified")
      exit(1)
    else:
      # override data frame with filtered data frame based on year
      time_frame = time_frame.loc[(pd.to_datetime(time_frame.DATE).dt.year == YEAR)]
  # if month is specified
  elif TIME == "MONTHLY":
      print("MONTHLY CHECK")
      if YEAR == None or MONTH == None:
        print("No argument for year or month specified")
        exit(1)
      else:
        # override data frame with filtered data frame based on year and month
       time_frame = time_frame.loc[(pd.to_datetime(time_frame.DATE).dt.year == YEAR) & (pd.to_datetime(time_frame.DATE).dt.month_name() == MONTH)]

  # sort filtered data frame according to DELTA
  time_frame = time_frame.sort_values(['DELTA'], ascending=False)


  # build and return json body
  head = time_frame.iloc[0]
  return_json["city"] = head.NAME
  return_json["date"] = head.DATE
  return_json["temp_change"] = head.DELTA
  
  return return_json


main()


