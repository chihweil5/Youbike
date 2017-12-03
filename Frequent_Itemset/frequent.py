import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import OnehotTransactions


if __name__ == "__main__":

    sup = 0.75

    df = pd.read_csv("frequentItemSet.txt")
    basket = (df
            .groupby(['ID', 'Time'])['Quantity'].sum()
            .unstack().reset_index().fillna(0)
            .set_index('ID')
            )

    def encode_units(x):
        try:
            if x <= 0:
                return 0
            if x >= 1:
                return 1
        except:
            print(x)
            return x

    basket_sets = basket.applymap(encode_units)
    basket_sets.to_csv("basketSet.txt")

    frequent_itemsets = apriori(basket_sets, min_support=sup, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    print(frequent_itemsets)
    frequent_itemsets.to_csv("ResultWeekTime_0.75.txt")