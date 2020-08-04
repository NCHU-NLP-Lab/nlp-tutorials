def sent_predictor(input=''):
    """
    Parameters
    ----------
    input : string
        sentence
    Returns
    -------
    Classifier prediction : string
        The positive or negative predicted by the classifier 
    """	
    if "input is positive":
        return 'positive'
    else:
        return 'negative'
