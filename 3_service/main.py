from fastapi import FastAPI
from pydantic import BaseModel
from ludwig.api import LudwigModel
import pandas as pd

# poetry run uvicorn main:app --reload
app = FastAPI()

model = LudwigModel.load('./model')

dataframe_2 = pd.DataFrame({'text': [
    'This was a really good movie, I had a lot of fun',
    'This was a very bad movie, it was really boring'
]})
predictions_2 = model.predict(
    dataset=dataframe_2, data_format='df')
print(predictions_2)

# class Review(BaseModel):
#    text: str


# curl http://0.0.0.0:8000/ -X GET
@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/predictions")
# def update_item(review: Review):
#     dataframe_1 = pd.DataFrame({'text': [review.text]})

#     predictions_1 = model.predict(
#         dataset=dataframe_1, data_format='df')
#     print(predictions_1)
#     return {predictions_1}
