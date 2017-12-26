# Hammad Usmani
from pandas import DataFrame, Series
import numpy


def avg_medal_count():
    '''
    Compute the average number of bronze medals earned by countries who 
    earned at least one gold medal.  
    
    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.
    
    HINT-1:
    You can retrieve all of the values of a Pandas column from a 
    data frame, "df", as follows:
    df['column_name']
    
    HINT-2:
    The numpy.mean function can accept as an argument a single
    Pandas column. 
    
    For example, numpy.mean(df["col_name"]) would return the 
    mean of the values located in "col_name" of a dataframe df.
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
    
    olympic_medal_counts = {'country_name':Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    df = DataFrame(olympic_medal_counts)
    
    #Hammad Usmani
    #http://pandas.pydata.org/pandas-docs/stable/indexing.html#boolean-indexing
    '''
    print type(df) #data frame
    print type(df['gold']) #Series with the stored values
    print type(df['gold'] > 0) #New Series with a boolean in every index corresponding to an expression
    print type(df[df['gold'] > 0]) #Data Frame where index is True we keep and discard the index if it doesn't evalute to true
    print type(df[df['gold'] > 0].bronze) #Series disjointed from the dataframe
    
    One solution:
    -Here we put a boolean vector "key" the same length of the series
    -The DataFrame returned all columns where the vector was True, using the expression x : x > 0
    -In this case, the condition for the key was column 'gold'
    -We wanted to do analysis on the dataframe that we created. The average in the set of bronze
    -We grabbed the bronze series in the dataframe and gave it to numpy.mean() to calculate the average
    numpy.mean(df[df['gold'] > 0].bronze)
    
    Alternative:
    print numpy.mean(df[df['gold'].map(lambda x : x > 0)].bronze)
    
    '''
    avg_bronze_at_least_one_gold = numpy.mean(df[df['gold'] > 0].bronze)

    return avg_bronze_at_least_one_gold