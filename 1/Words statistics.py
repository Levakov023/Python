import pandas as pd
from utils import *

#read the excel file using pandas

df = pd.read_excel("WSC Input.xlsx",
                   usecols=["Description","TariffNumber"])

dataset= df.to_dict()

#takes the tariff values from excel and add's "0" to the beginning if the length is 9, theese values are then stored in a list
Tariffs = ["0" + str(dataset["TariffNumber"][i]) if len(str(dataset["TariffNumber"][i])) == 9 else str(dataset['TariffNumber'][i])
           for i in dataset['TariffNumber']]

# using List comprehension, a list of list is created, each sub list contains words from its corresponding descriptions.
wordsList = [[j for j in dataset['Description'][i].split()]for i in dataset["Description"]]

# unique words is a list of non-duplicate word that occur in each description.
unique_words = sorted(list(set([word.lower() for description in dataset["Description"].values() for word in description.split()])))

#inputData is a dictionary in which keys are Tariff numbers and values are lists of split description words.
inputData = {tarif : [word.lower() for word in wordsList[x]] for x,tarif in enumerate(Tariffs)}


Tariffs_data = split_tarrifs(Tariffs)

data_for_csv = solution(unique_words, Tariffs_data, inputData)

csv_data = pd.DataFrame(data_for_csv)

csv_data.to_csv("finish csv",index=False)
#csv_data.to_excel('answer.xlsx',index=False)
