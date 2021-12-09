# importing the module
import csv
import matplotlib.pyplot as plt
import numpy as np


def condToNumber(tmpCond):
    tmpCond = tmpCond.split("/")[0]
    numCond = 0

    # print(tmpCond)

    if tmpCond == "I":
        numCond = 1
    elif tmpCond == "I-":
        numCond = 1.25
    elif tmpCond == "II ":
        numCond = 1.75
    elif tmpCond == "II":
        numCond = 2
    elif tmpCond == "II-":
        numCond = 2.25
    elif tmpCond == "III ":
        numCond = 2.75
    elif tmpCond == "III":
        numCond = 3
    elif tmpCond == "III-":
        numCond = 3.25
    elif tmpCond == "IV ":
        numCond = 3.75
    elif tmpCond == "IV":
        numCond = 4
    elif tmpCond == "IV-":
        numCond = 4.25
    elif tmpCond == "V ":
        numCond = 4.75
    elif tmpCond == "V":
        numCond = 5
    elif tmpCond == "V-":
        numCond = 5.25
    elif tmpCond is None:
        numCond = 6
    else:
        numCond = 6

    return numCond


def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


def calculatePrecision(val1, val2):
    if val1 is None or val2 is None:
        return 0

    if val1 == 0 or val2 == 0:
        return 0

    return abs(val1 - val2) / val2


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
coinName_arr = []
coinCat_arr = []
condition_arr = []
price_diff = []
est_price_arr = []
bids_arr = []
views_arr = []
auctionEnd_d_arr = []

price_acc = []

# fig, ax = plt.subplots()

coinCondPrices = {
    1: [],
    1.25: [],
    1.75: [],
    2: [],
    2.25: [],
    2.75: [],
    3: [],
    3.25: [],
    3.75: [],
    4: [],
    4.25: [],
    4.75: [],
    5: [],
    5.25: [],
}

# open the csv_file in read mode
with open("lot.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    x = 0
    headers = next(csv_reader)
    for col in csv_reader:
        try:
            coinCondPrices = add_values_in_dict(
                coinCondPrices,
                condToNumber(col[4]),
                [calculatePrecision(float(col[5]), float(col[6]))],
            )
            x = 1
        except:
            pass

    avgCoinEst = dict()
    for key in coinCondPrices:
        avgPriceDiff = 0
            
        if len(coinCondPrices[key]) != 0:
            #print("dla ", key, ": ", len(coinCondPrices[key]), ", suma: ", sum(coinCondPrices[key]), " avg: ", sum(coinCondPrices[key])/len(coinCondPrices[key]))
            avgPriceDiff = sum(coinCondPrices[key]) / len(coinCondPrices[key])
            avgCoinEst[key] = avgPriceDiff


        print("dla ", key, ": ", len(coinCondPrices[key]), ", suma: ", sum(coinCondPrices[key]))


# plot
# print(list(coinCondPrices.keys())) # klucze na oś X


print(list(avgCoinEst.keys()))
print(list(avgCoinEst.values()))

plt.plot(list(avgCoinEst.keys()),list(avgCoinEst.values()))
plt.savefig('char2.png')
# print(sum(coinCondPrices[4.25]))
