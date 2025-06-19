#!/usr/bin/env python3

import sys
import os
from gi.repository import Gimp, Gio, GLib

def export_layers_as_png(image_path, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the image
    file = Gio.File.new_for_path(image_path)
    image = Gimp.file_load(Gimp.RunMode.NONINTERACTIVE, file)

    # Get layers - returns a list directly in GIMP 3
    layers_list = image.get_layers()
    print(f"Found {len(layers_list)} layers")
    
    for i, layer in enumerate(layers_list):
        print(f"Processing layer {i}: {layer.get_name()}")
        
        # Make only this layer visible
        for l in layers_list:
            l.set_visible(l == layer)

        # Duplicate and flatten
        temp_image = image.duplicate()
        flattened_layer = temp_image.merge_visible_layers(Gimp.MergeType.CLIP_TO_IMAGE)

        # Export filename
        layer_name_safe = layer.get_name().replace(" ", "_").replace("/", "_")
        filename = os.path.join(output_dir, f"{layer_name_safe}.png")

        # Export as PNG - correct GIMP 3 syntax
        file_out = Gio.File.new_for_path(filename)
        Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, temp_image, file_out)

        temp_image.delete()

    image.delete()

def run_batch():
    # Process both XCF files
    images_to_process = [
        ('logos_for_main_page.xcf', '../assets/images/logos'),
        ('letterboxes-460x175.xcf', '../assets/images/letterboxes')
    ]
    for image_path, output_dir in images_to_process:
        export_layers_as_png(image_path, output_dir)

if __name__ == '__main__':
    run_batch()