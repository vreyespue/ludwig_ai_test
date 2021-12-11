from ludwig.api import LudwigModel
import pandas as pd

model = LudwigModel.load('./model/')

datafile_1 = './reuters-allcats-head.csv'
predictions_1 = model.predict(
    dataset=datafile_1, data_format="csv")
print(predictions_1)

dataframe_2 = pd.DataFrame({'text': [
    'BAHIA COCOA REVIEW SALVADOR Feb 26 - Showers continued throughout the week',
    'COBANCO INC ltCBCO YEAR NET SANTA CRUZ Calif Feb 26 - Shr 34 cts vs 119 dlrs'
]})
predictions_2 = model.predict(
    dataset=dataframe_2, data_format='df')
print(predictions_2)
