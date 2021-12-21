ludwig predict \
  --dataset Test-head.csv \
  --model_path results_1_experiment/experiment_run/model \
  --output_directory results_2_predict

# parquet-tools rowcount results_2_predict/predictions.parquet
# parquet-tools head results_2_predict/predictions.parquet
