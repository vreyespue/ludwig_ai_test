from ludwig.api import LudwigModel
import pandas as pd

model = LudwigModel.load(
    './model')

datafile_1 = './Test-head.csv'
predictions_1 = model.predict(
    dataset=datafile_1, data_format="csv")
print(predictions_1)

dataframe_2 = pd.DataFrame({'text': [
    'This was a really good movie, I had a lot of fun',
    'This was a very bad movie, it was really boring'
]})
predictions_2 = model.predict(
    dataset=dataframe_2, data_format='df')
print(predictions_2)
