import pandas as pd 

def get_top_n(df, grouped_dimension_list, analysis_dimension, metric, n):
    """get top n of dimension by metric"""
    
    # group by "grouped_dimension_list" and sum by "metric"
    df = df.groupby(grouped_dimension_list)[metric].sum()
    
    # get top N for each "analysis_dimension" and reset index to clean up
    return df.groupby(level=analysis_dimension, group_keys=False).nlargest(n).reset_index()

def main(df, grouped_dimension_list, analysis_dimension, metric, n):
    # get top 10 keywords by traffic
    top_keywords_per_url = get_top_n(df, grouped_dimension_list, analysis_dimension, metric, n)

    # merge top_keywords_per_url with df to bring extra columns
    return top_keywords_per_url.merge(df, on=['URL', 'Keyword'], how='left')

if __name__ == '__main__':
    df = pd.read_csv('turbo-tax-semrush.csv')

    # filter df to Traffic > 0
    df = df[df['Traffic'] > 10]
    df = df[df['Search Volume'] > 100]
    
    output = main(df, ['URL', 'Keyword'], 'URL', 'Traffic', 3)

    # write to csv
    output.to_csv('top-values-for-dimension-by-metric.csv', index=False)