import pandas as pd
import numpy as np
import datetime
import time



# Get city file names
Chicago = 'chicago.csv'
New_york_city ='new_york_city.csv'
Washington = 'washington.csv'

def city_input_data():
    '''Asks the user for a city, get the corresponding bikeshare data as Pandas
        dataframe, perform basic data processing, and 
        and returns the processed data and selected city name.
    Args:
        none.
    Returns:
        (str) Name of the selected city.
    '''
   
    print("Hii all! I'm Sukanya ,Lets explore US BikeShare Data!")
    strcity = input("Would you like to see data for Chicago, New York or Washington?\n")

# Conditional statement to handle invalid entries
    if strcity.capitalize() == 'Chicago':
       print("Oh it's " +strcity+ " Let's go further")
       return Chicago
       
    
    elif strcity.capitalize() == 'Washington':
         print("Oh it's " +strcity+ " Let's go further")
         return Washington
       
    elif strcity == 'New York':
         print("Oh it's " +strcity+ " Let's go further")
         return New_york_city
       
    else:
         print("Enter valid city as mentioned in the option")
         return city_input_data() 
    

def get_time_period(city_df):
    '''Asks the user for a time period and returns the specified filter.
    Args:
        city_df : Bikeshare dataframe
    Returns:
        (list) with two str values:
            First value: the type of filter period (i.e. month, day or none)
            Second value: the specific filter period (e.g. May, Friday)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == 'month':
        month_list=('January', 'February', 'March', 'April', 'May', 'June')
        while True:
           month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
           if month in month_list:
              city_df['month'] = city_df['Start Time'].dt.month
              month_index = month_list.index(month) + 1
              print("Statistics for month of {} " .format(month))
              city_df = city_df[city_df['month'] == month_index]
              time_period = month
              break
           print('Enter a valid month name provided in the options')
          
    elif time_period.lower() == 'day':
         week_day_list = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
         while True:
           day_of_week = input('\nWhich day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
           if day_of_week in week_day_list:
               city_df['day_of_week'] = city_df['Start Time'].dt.dayofweek
               day_index = week_day_list.index(day_of_week) 
               print(day_index)
               print("Statistics for {} " .format(day_of_week))
               city_df = city_df[city_df['day_of_week'] == day_index]
               time_period = day_of_week
               break
           print("\n I'm sorry, I'm not sure which day of the week you're trying to filter by. Let's try again.")
        
    elif time_period == 'none':
        filtered_data = city_df
    else:
        print("\n I'm sorry, I'm not sure which input you are giving.It should be month ,day or none") 
        
    return city_df,time_period

#city_df = get_time_period(city_df)

def popular_month(city_df):
    '''Prints the popular month for the start time
    Args:
      city_df:Dataframe for bikeshare data
    Returns:
      none
    '''  
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(city_df['Start Time'].dt.month.mode())
    most_pop_month = months[index - 1]
    return most_pop_month
    print('The most popular month is {}.'.format(most_pop_month))
   
def popular_hour(city_df):
    '''Prints the popular hour of the day based on statistics
    Args:
     city_df:Bikeshare Dataframe
    Returns:
     none
    '''
    most_pop_hr = int(city_df['Start Time'].dt.hour.mode())
    if most_pop_hr >= 1 and most_pop_hr <  12:
       time_mode = 'AM'
    elif most_pop_hr >= 12 and most_pop_hr <= 24:
         time_mode = 'PM'
         most_pop_hr = most_pop_hr - 12
    elif  most_pop_hr == 0:
          most_pop_hr = 12 

    print("Most Popular Hour {} {}".format(most_pop_hr,time_mode))
    
def popular_day(city_df):
    '''prints the most popular day of week (Monday, Tuesday, etc.) for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(city_df['Start Time'].dt.dayofweek.mode())
    #print(index)
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))
    

def popular_station(city_df):
    '''This function returns the popular station based on Start Station and End Station
    Args:
         Bikeshare dataframe 
    '''
    pop_start_stn = city_df['Start Station'].mode().loc[0]
    print('Popular Start Station: {}'.format(pop_start_stn))
    pop_end_stn = city_df['End Station'].mode().loc[0]
    print('Popular End Station: {}'.format(pop_end_stn))
    pop_stn = city_df['Start Station'] + "-" + city_df['End Station']
    pop_trip = pop_stn.value_counts().idxmax()
    print('Most popular trips are between:{} and {}'.format(pop_trip.split('-')[0], pop_trip.split('-')[1]))

    
def popular_trip_duration(city_df):
    '''This function returns the total trip duration
    Args:
       Bikeshare dataframe  
    '''
    total_trips = city_df['Start Time'].count()
    print( " Total Trips :{}" .format(total_trips))
    total_trip_dur = city_df['Trip Duration'].sum()
    minute ,second = divmod(total_trip_dur ,60) #60 seconds in an minute
    hr , minute = divmod(minute ,60) #60 minutes in an hour
    days ,hr = divmod(hr ,24) #24 hrs in a day
    print(" The total trip duration in {} days in {} hours , {} minutes and {} seconds" .format(days,hr,minute,second))
    
def users(city_df):
    '''This function returns the count of each user type
    Args:
        city_df: dataframe of bikeshare data
    Returns:
        (pandas series) where the index of each row is the user type and the value
            is how many trips that user type made
    '''
    user_types = city_df['User Type'].value_counts()
    return user_types

def gender(city_df):
    '''This function returns the count of gender M/F
    Args:
        city_df: dataframe of bikeshare data
    Returns:
        (pandas series) where the index of each row is the user type and the value
            is how many trips that user type made
    '''
    
    gender_count = city_df['Gender'].value_counts()
    return gender_count


def birth_year(city_df):
    '''This funtion calculates the minimum birth year ,maximum birth year
       and popular birth year based on the occurrences  
    Args:
      city_df: dataframe of bikeshare date 
    Returns:
         None
    '''

    earliest_birth_yr = int(city_df['Birth Year'].min())
    latest_birth_yr = int(city_df['Birth Year'].max())
    pop_birth_yr = int(city_df['Birth Year'].mode())
    print(" Earliest birth year :{} \n Latest birth year :{} \n Popular birth year:{} " .format(earliest_birth_yr,latest_birth_yr,pop_birth_yr))
          
def restart():
    '''Displays the data based on what the user specidies
        If 'yes' then further statistics is calculated else 'no'
        execution stops there
     Args:
         city_df: dataframe of bikeshare data
      Returns:
          None
     '''
    
    display = input("\n Would you like to restart?Type 'Yes/Y' or 'No/N' \n")
    if display == 'Yes' or display == 'Y':
          statistics()
          #print(city_df.head())
    if display == 'No' or display == 'N':
          return
    else:
          print("Please enter valid option..Yes(Y) or No(N)")
          return restart()
                    

def display_raw_data(city_df):
    '''Displays five lines of data based on user input and ask the
       user for five more lines and continue further
     Args:
         city_df: dataframe of bikeshare data
      Returns:
          None
    '''

    raw_data = input("\n Would you like view individual data, Type 'Yes/Y' or 'No/N' \n")
    line = 0;
    if raw_data == 'Yes' or raw_data == 'Y':
        print(city_df.iloc[line:line+5])
        line += 5
        return(city_df)

    if raw_data == 'No' or raw_data == 'N':
       return
    else:
        print("Please enter valid option..Yes(Y) or No(N)")
        return(city_df)
    
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = city_input_data()
    print(city)
    city_df = pd.read_csv(city)
    
   
    # parse datetime and column names
    city_df['Start Time'] = pd.to_datetime(city_df['Start Time'])
    city_df['End Time'] = pd.to_datetime(city_df['End Time'])
    start_time = time.time()

    
    # Filter data by month,day or none
    city_df,time_period = get_time_period(city_df)
   
    print("Loading...the data")
    print("Calculating Statistics..")
    
    #print(time_period)
    if time_period == 'none':
         df_filter = city_df
         start_time = time.time()
         

    month_list = ('January', 'February', 'March', 'April', 'May', 'June') 
    if time_period in month_list:
          start_time = time.time()


    week_day_list = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if time_period in week_day_list:
           print(time_period)
           start_time = time.time()
           

        
    # Filter user
    print("\nPOPULAR USERS")
    print(users(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter popular hour
    print("\nPOPULAR HOUR")
    print(popular_hour(city_df))
    print("That took %s seconds." % (time.time() - start_time))

    # Filter popular station  
    print("\nPOPULAR STATION")
    print(popular_station(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

    # Filter Trip Duartion
    print("\nPOULAR TRIP DURATION")
    print(popular_trip_duration(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

    # Filter Popular day
    print("\nPOPULAR DAY")
    print(popular_day(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

    # Filter Popular Month
    print("\nPOPULAR MONTH")
    print(popular_month(city_df))
    print("That took %s seconds.\n" % (time.time() - start_time))

   
    
    if city == 'chicago.csv' or city == 'new_york_city.csv': 
       print(city) 
     # Filter Gender
       print("\nPOPULAR GENDER")
       print(gender(city_df))
       print("That took %s seconds." % (time.time() - start_time))

    # Filter birth year
       print("\nPOPULAR BIRTH YEAR")
       print(birth_year(city_df))
       print("That took %s seconds." % (time.time() - start_time))

   # Display Raw data
    print(display_raw_data(city_df))
   
   # Restart Function
    print(restart())  
    
if __name__ == "__main__":
    statistics()   
    
    
