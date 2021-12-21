ludwig serve -m results_1_experiment/experiment_run/model

# curl http://0.0.0.0:8000/predict -X POST -F 'text=This was a really good movie, I had a lot of fun'
# curl http://0.0.0.0:8000/predict -X POST -F 'text=This was a very bad movie, it was really boring'
