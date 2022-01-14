# importing the module
import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# col 0: spider_dt
# col 1: auctionEnd_d
# col 2: name
# col 3: category
# col 4: condition
# col 5: price
# col 6: est_price
# col 7: bids
# col 8: views
# col 9: state
# col 10: photoUrl
# col 11: link

# creating empty lists
coinName_arr        = []
coinCat_arr         = []
coinCatDiff_arr     = []
coinCntCatDiff_arr  = []
condition_arr       = []
price_arr           = []
est_price_arr       = []
bids_arr            = []
views_arr           = []
auctionEnd_d_arr    = []

price_diff          = []

fig, ax = plt.subplots()

# open the csv_file in read mode
with open('lot.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for col in csv_reader:
        try:
            # make the data
            if 'Polska' or 'Polskie' not in col[3]:
                coinCat_arr.append(col[3])
        except:
            pass
# plot

coinCatDiff_arr = list(Counter(coinCat_arr).keys())
coinCntCatDiff_arr = list(Counter(coinCat_arr).values())



y = coinCatDiff_arr
x = coinCntCatDiff_arr


# print(coinCat_arr)
chart3  = ax.barh(y, x, align = 'center')

ax.set_yticks(y)

plt.savefig('char3.png')