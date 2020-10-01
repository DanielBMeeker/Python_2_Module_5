import pandas as pd

kick_all = pd.read_csv('ks-projects-201801.csv', index_col='ID')

if __name__ == '__main__':
    # print(kick_all.shape)
    # print(kick_all['backers'].value_counts(bins=10))
    # print(pd.qcut(kick_all['backers'], q=6))
    kick_rows_to_delete = kick_all[kick_all["backers"]<20].index
    # print(kick_rows_to_delete.shape)
    kick_rows_to_delete = list(kick_rows_to_delete)
    # print(kick_rows_to_delete[0:10])
    kick_20_backers = kick_all.drop(kick_rows_to_delete)
    print(kick_20_backers.head())
    print(kick_20_backers.shape)
