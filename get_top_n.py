import pandas as pd 

def get_top_n(df, metric, n):
    """get top n of dimension by metric"""
    return df.sort_values(metric, ascending=False).head(n)

def main(df, analysis_dimension, metric, n):
    # Create empty df to hold final output
    final = pd.DataFrame(columns=df.columns)
    
    # Get list of unique values in analysis_dimension
    dimension_list = df[analysis_dimension].drop_duplicates().values.tolist()
    
    for dim in dimension_list:
        # filter df by dim and get top n
        top_n = get_top_n(df[df[analysis_dimension] == dim], metric, n)
        # concat to final df
        final = pd.concat([final, top_n])

    # merge top_keywords_per_url with df to bring extra columns
    return final

if __name__ == '__main__':
    df = pd.read_csv('gsc.csv')
    output = main(df, 'URL', 'Traffic', 6)
    output.to_csv('top-values-for-dimension-by-metric.csv', index=False)