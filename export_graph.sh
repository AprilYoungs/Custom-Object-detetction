python object_detection/export_inference_graph.py \
        --input_type image_tensor \
        --pipeline_config_path ssd_mobilenet_coco.config \
        --trained_checkpoint_prefix train/model.ckpt-10000 \
        --output_directory output_inference_graph
