import pandas as pd

def get_counts(df, col):
    """Returns a dataframe of the counts in the target column.
    
    Args:
        df: dataframe to get data from
        col: target column for counting
        
    Returns:
        df: a dataframe with columns: col, 'count'
    """
    result_df = pd.DataFrame(df[col].value_counts())
    result_df = result_df.reset_index()
    result_df.columns = [col, 'count']
    return result_df


def get_dogs_by_breed(all_dogs, breeds):
    """returns dog index numbers that have the breeds in primary or secondary breed columns.
    
    Args:
        all_dogs: a dataframe with all the dogs' info
        breeds: a list of breeds that count
        
    Returns: a list of dog #s (the index column) that match the breeds in primary or secondary.
    """
    result = all_dogs.loc[(all_dogs['Primary Breed'].isin(breeds) 
             | all_dogs['Secondary Breed'].isin(breeds))]
    result = [str(x) for x in list(result['index'])]
    return result


if __name__ == "__main__":
    pass