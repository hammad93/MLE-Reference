import numpy
from pandas import DataFrame, Series


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each 
    bronze medal.  

    Using the numpy.dot function, create a new dataframe called 
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
           
    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
 
    #Hammad Usmani
    '''
    To find the dot product:
    Value Matrix: [4, 2, 1]
    Result Matrix: [Country 1, Country 2, Country 3, ... Country n]
    Score Matrix: [[gold],[silver],[bronze]]
    Score dot Value = Result
    
    numpy.dot([4, 2, 1], [gold, silver, bronze])
    
    1) Conduct proper matrix multuplication to obtain a list of sums corresponding to the countries
    2) numpy.dot will return a series
    3) Create dataframe based on paramters
    '''
    data = {'country_name': Series(countries),
            'points': Series(numpy.dot([4, 2, 1], [gold, silver, bronze]))}
            
    olympic_points_df = DataFrame(data)
    
    return olympic_points_df