from ludwig.api import LudwigModel

model = LudwigModel.load('./model/')
predictions = model.predict('./reuters-allcats-head.csv')
print(predictions)