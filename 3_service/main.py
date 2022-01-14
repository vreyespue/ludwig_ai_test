from fastapi import FastAPI
from pydantic import BaseModel
from ludwig.api import LudwigModel
import pandas as pd

model = LudwigModel.load('./model')
dataframe_start = pd.DataFrame({'text': [
    'This was a really good movie, I had a lot of fun',
    'This was a very bad movie, it was really boring'
]})
predictions_start = model.predict(
    dataset=dataframe_start, data_format='df')
# print(predictions_start)


# poetry run uvicorn main:app --reload
app = FastAPI()


class Review(BaseModel):
    text: str


# curl http://0.0.0.0:8000/ -X GET
@app.get("/")
def read_root():
    return {"Hello": "World"}


# curl http://0.0.0.0:8000/predictions -X POST
#     --data-raw '{"text": "Good movie"}' -H "Content-Type: application/json"
@app.post("/predictions")
def update_item(review: Review):
    # print(review)
    # print(review.text)
    dataframe_1 = pd.DataFrame({'text': [review.text]})
    predictions_1 = model.predict(
        dataset=dataframe_1, data_format='df')
    # print(predictions_1)
    # print(list(predictions_1[0].label_predictions))
    return list(predictions_1[0].label_predictions)
