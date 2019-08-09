docker run -t --rm -p 8501:8501 \
    -v "$(pwd)/models/":"/models/" \
    tensorflow/serving \
    --model_config_file=/models/models.config \
    --monitoring_config_file=/models/monitoring.config \
    --model_config_file_poll_wait_seconds=60 \
    --allow_version_labels_for_unavailable_model=1 \

