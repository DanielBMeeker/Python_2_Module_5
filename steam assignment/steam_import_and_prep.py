import pandas as pd

steam_all = pd.read_csv('steam.csv')

if __name__ == '__main__':

    # create a temp frame that is grouped by publisher and summed
    steam_grouped_by_publisher = steam_all.groupby('publisher')
    steam_grouped_by_publisher = steam_grouped_by_publisher.sum()
    print(steam_grouped_by_publisher.head(15))
    # from this grouped frame create a list of rows that need to be deleted
    steam_rows_to_delete = steam_grouped_by_publisher[steam_grouped_by_publisher['positive_ratings']<50].index
    # print(steam_rows_to_delete.describe())
    steam_rows_to_delete = list(steam_rows_to_delete)
    steam_good_publishers = steam_all.drop(steam_rows_to_delete)
    # print(steam_good_publishers.sort_values(by='positive_ratings', ascending=False))
    print(steam_good_publishers.shape)
