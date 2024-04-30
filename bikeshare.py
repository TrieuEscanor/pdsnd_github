import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York or Washington? \n').lower()
        if city in CITIES:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? Chose a month January, February, March, April, May, June or "all" to apply no month filter? \n').lower()
        if month in MONTHS:
            break
        if month == 'all':
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Chose a day Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or "all" to apply no day filter? \n').lower()
        if day in DAYS:
            break
        if day == 'all':
            break

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day Of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    ## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print('The most common month: ', most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['Start Time'].dt.day_name().mode()[0]
    print('The most common day of week: ', most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: ', most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: ', most_common_end_station)


    # display most frequent combination of start station and end station trip
    frequent_combination_start_end_station = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip: ', str(frequent_combination_start_end_station.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is %d seconds." % total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The average travel time is: %f seconds." % mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types:")
    # get each user type from dataframe
    for index, user_count in enumerate(user_types):
        print("  {}: {}".format(user_types.index[index], user_count))

    if city in ('chicago', 'new york'):
        # display counts of gender
        genders = df['Gender'].value_counts()
        print("The count of gender:")
        # get each gender from dataframe
        for index, gender_count in enumerate(genders):
            print("  {}: {}".format(genders.index[index], gender_count))

        # display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        ## the most common birth year
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year: ", most_common_year)

        ## the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year: ", most_recent)

        ##the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year: ", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.

    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    # display raw data
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
