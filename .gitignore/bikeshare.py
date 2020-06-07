import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv','New York City': 'new_york_city.csv','Washington': 'washington.csv' }

def get_city():
    """Prompt user to specify a city to analyze.
    Returns:
    (str) filename from bikeshare data of a city to analyze.
    """

    print('Hello! Let\'s explore some US bikeshare data!\nFollow the prompts for guided exploration.\nLet\'s begin!\n')

    # Specify one of three cities: Chicago, New York City, and Washington.

    while True:
        try:
            city = input('Would you like to explore Chicago, New York City, or Washington?\n').title()
            if city == 'Chicago' or city == 'chicago':
                return 'chicago.csv'
            elif city == 'New York City' or city == 'new york city':
                return 'new_york_city.csv'
            elif city == 'Washington' or city == 'washington':
                return 'washington.csv'
            else:
                print('City names include: Chicago, New York City, or Washington.')
                break

        except NameError:
            print('City names include: Chicago, New York City, or Washington.')
            return city

def get_time():
    """Prompt user to specify time period to explore as month, day, or neither.
    Returns:(list) Two string values...
    First value: type of filter as month, day or neither
    
    Second value: specific filter period
    """

# Specify one of three time periods: month, day, or neither.

    while True:
        try:
            time_period = input('\nWould you like to see statistics on the city now or specify a certain month or day?\nType month, day or neither for selection.\n').lower()
            if time_period == 'month':
                return ['month', get_month()]
            elif time_period == 'day':
                return ['day', get_day()]
            elif time_period == 'neither':
                city = {'Chicago', 'chicago', 'New York City', 'new york city', 'Washington', 'washington'}
                return ['neither', city_data(city)]
            else:
                print('Please try again and specify month, day or neither.')
                break

        except NameError:
            print('Please try again and specify month, day or neither.')

def get_month():
    """
    Prompt user to speficy a month to explore.
    Returns:
    (str) Convert month into number.
    """
    
# Speficy the month between January and June.

    while True:
        try:
            month = input('Enter the month you wish to explore.\n')
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month = months.index(month)
                break
        except NameError:
            print('Month options are from January to June written in lowercase letters.')

# Specify one of two time periods: now or day.

    while True:
        try:
            month_stats = input('\nWould you like to see statistics on the month now or specify a certain day?\nType now or day for selection.\n').lower()
            if month_stats == 'now':
                return ['now', month_data()]
            elif month_stats == 'day':
                return ['day', get_day()]
            else:
                print('Please try again and type now or day.')
                break

        except NameError:
            print('Please try again and type now or day.')
            return month_df

def get_day():
    """
    Prompt user to speficy a day of the week to explore.
    Returns:
    (int) Day of the week as an integer.
    """

# Speficy the day of the week.

    while True:
        try:
            day = input('Enter the day you wish to explore.\n')
            if day != 'all':
                days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                day = days.index(day)
                break
        except ValueError:
            print('Days of the month should be entered using lowercase letters.')
            return day_df

def popular_month(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular month traveled.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Month with most traveled trips.
    """

# Display the most popular month traveled.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name
    popular_month = df['month'].mode()
    print('The most popular month taveled is {}.\n'.format(popular_month))

def popular_day(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular day traveled.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Day with most traveled trips.
    """

# Display the most popular day of the week traveled.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()
    print('The most popular day of the week traveled is {}.\n'.format(popular_day))

def popular_hour(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular hour traveled.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Hour with most traveled trips.
    """

# Display the most popular start hour traveled.

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour to start to travel is {}.\n'.format(popular_hour))

def popular_stations(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular stations visited.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Most popular starting station
    (str) Most popular ending station
    """

# Display most commonly used start station.

    popular_start_station = df['Start Station'].mode()
    print('{} is the most commonly used start station.\n'.format(popular_start_station))

# Display most commonly used end station.
    popular_end_station = df['End Station'].mode()
    print('{} is the most commonly used end station.\n'.format(popular_end_station))

def popular_trip(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the most popular trips.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Most popular combination of starting and ending stations with a count and percentage or total trips.
    """

# Display most frequent combination of start station and end station trips.

    popular_start_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('{} are the most commonly used start and end stations.\n'.format(popular_start_end_stations))

def trip_duration(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return the total trip duration and average trip duration.
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (str) Total trip duration in years, days, hours, minutes, & seconds
    (str) Average trip duration in hours, minutes, & seconds
    """

# Calculate the total trip time and the average trip time.

    total_trip_dur = df['Trip Duration'].sum()
    print('The total time traveled was {}.\n'.format(total_trip_dur))
    avg_trip_dur = df['Trip Duration'].mean()
    print('The average travel time was {}.\n'.format(avg_trip_dur))

def user_stats(df):
    """
    Given a specific DataFrame in the bikeshare data, this function will return a count of trips by user type and gender (if applicatble).
    Args:
    df: DataFrame of bikeshare data
    Returns:
    (panda series) Two series...
    First series: User type count of trips
    Second series: Gender count of trips
    (list) Three string values...
    First value: Earliest birth year of users
    Second value: Most recent birth year of users
    Third value: Most common birth year of users
    """

# Display counts of user types

    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print('The total amount of each user type is:\n{}\n'.format(user_type))

# Display counts of gender

try:
    gender = df['Gender'].value_counts()
    print('The total in each gender are:\n{}\n'.format(gender))

except:
    print('There is no gender information for Washington.\n')

# Display earliest, most recent, and most common year of birth

try:
    earliest_birth_year = min(df['Birth Year'])
    print('The earliest birth year is {}.\n'.format(earliest_birth_year))
    recent_birth_year = max(df['Birth Year'])
    print('The most recent birth year is {}.\n'.format(recent_birth_year))
    common_birth_year = df['Birth Year'].mode()
    print('The most common birth year is {}.\n'.format(common_birth_year))

except:
    print('There is no birth year information for Washington.\n')

def city_data(???):
    """
    Display data for the user from the city pathway followed by neither month nor day.
    """

# Basic stats

    df = pd.read_csv(???)
    print(popular_month(???))
    print(popular_day(???))
    print(popular_hour(???))
    print(trip_duration(???))
    print(popular_station(???))
    print(popular_trip(???))
    print(user_stats(???))

def month_data(???):
    """
    Display data for the user from the city, month pathway followed by now.
    """

# Basic stats

    df = pd.read_csv(???)
    print(popular_day(???))
    print(popular_hour(???))
    print(trip_duration(???))
    print(popular_station(???))
    print(popular_trip(???))
    print(user_stats(???))

def day_of_week_data(???):
    """
    Display data for the user from the city, month, day pathway.
    """

# Basic stats
    df = pd.read_csv(???)
    print(popular_hour(df))
    print(trip_duration(df))
    print(popular_station(df))
    print(popular_trip(df))
    print(user_stats(df))

def get_stats():
    """
    Calculations & printouts of the statistics specified by the user of a city and time period.
    """

# Filter by city (Chicagor, New York City, Washington)

    df = pd.read_csv(get_city())

# Filter by month, day or stats

    df = pd.read_csv(get_time())
# Provide stats or prompt month

# Filter by day or stats

# Privide stats or prompt day

# Filter day

# provide stats

# Prompt user to restart filters

def restart_question():
    """
    Conditionally restarts the program based on the user input.
    """
    restart = input('\nWould you like to restart? Enter yes or no.')
    while True:
        try:
            if restart.lower() == 'yes':
                statistics()
            elif restart.lower() == 'no':
                break
            else:
                print('Please specify \'yes\' or \'no\'.')
        except ValueError:
            print('Please specify \'yes\' or \'no\'.')
            restart_question()

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        popular_trip(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break            
if __name__ == "__main__":
    main()
