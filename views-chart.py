# importing the module
import csv
import matplotlib.pyplot as plt
import numpy as np

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
            price_diff.append(float(col[6]) - float(col[5]))
            bids_arr.append(int(col[7]))
            views_arr.append(int(col[8]))
        except:
            pass
# plot

color = bids_arr
x = price_diff
y = views_arr

chart1  = ax.scatter(x, y, c=color, s=color, alpha=0.7)
ax.set_xlabel('estimate price - price (zl)')
ax.set_ylabel('views')
#ax.set_title('chart 1')
ax.grid(True)

cb = fig.colorbar(chart1 , ax=ax)
cb.set_label('binds')

plt.savefig('char1.png')