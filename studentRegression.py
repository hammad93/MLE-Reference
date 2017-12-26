#Reference from Udacity Machine Learning Engineering course
def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    from sklearn import linear_model
    ### name your regression reg
    '''
    Hammad Usmani
    12/19/2016 
    using the following: 
    http://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares
    
    METHOD: Use linear regression to build our model
    PURPOSE: To find a relationship between the x an y variables. In this case it is age (independent) and net worth (dependent)
    OUTPIT: General Linear Regression model as described in the sklearn documentation
    '''
    reg = linear_model.LinearRegression()
    
    '''
    Datasets include the ages and net worth as parameters of the parent function. The following will use this dataset to create the model
    Note: Datasets must be of type numpy array
    '''
    reg.fit(ages_train, net_worths_train)
    
    
    return reg