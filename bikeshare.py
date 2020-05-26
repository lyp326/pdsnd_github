import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('City: ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Please input a valid city name: ')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Month: ').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Day of Week: ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]

    print('Most Popular Start Day of Week:', popular_weekday)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start=df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start)  
    # TO DO: display most commonly used end station
    popular_end=df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_start)  

    # TO DO: display most frequent combination of start station and end station trip
    popular_comb=df[['Start Station','End Station']].mode().iloc[0]
    print('Most Popular Combination of Start and End Station:', popular_comb.title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:',np.sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print('Mean Travel Time:',np.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('Counts of User Type: ',user_types)

    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()

    print('Counts of Genders: ',genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    print('The Earliest Year of Birth:', np.min(df['Birth Year']))
    print('The Most Recent Year of Birth:', np.max(df['Birth Year']))
    print('The Most Common Year of Birth:', df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):


    data = 0
    answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
    while answer.lower() == 'yes':


        print(df[data : data+5])
        data += 5
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')

 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
