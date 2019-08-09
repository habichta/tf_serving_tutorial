docker run -t --rm -p 8501:8501 \
    -v "$(pwd)/models/":"/models/" \
    tensorflow/serving:nightly \
    --model_config_file=/models/models.config \
    --model_config_file_poll_wait_seconds=5 \
    --allow_version_labels_for_unavailable_models

