import cv2
import os
import numpy as np
import csv
from segments import segments

def map_pixels_to_time(start_time, duration, image_width):
    seconds_per_pixel = duration / image_width
    return [start_time + (pixel - 1) * seconds_per_pixel for pixel in range(1, image_width + 1)]

def normalize_gray_values(gray_pixel_counts):
    max_gray_value = max(gray_pixel_counts) if max(gray_pixel_counts) > 0 else 1
    return [(count / max_gray_value) * 100 for count in gray_pixel_counts]

def count_gray_pixels(image, gray_value=128, threshold=20):
    blue, green, red = cv2.split(image)
    gray_mask = (np.abs(red - gray_value) < threshold) & (np.abs(green - gray_value) < threshold) & (np.abs(blue - gray_value) < threshold)
    return [np.sum(gray_mask[:, col]) for col in range(gray_mask.shape[1])]

def extract_engagement_data(image_directory, csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Image", "Pixel", "Time (s)", "Gray Value", "Normalized Engagement (%)"])

        for i, (start_time, end_time) in enumerate(segments, 1):
            image_path = os.path.join(image_directory, f'heatmap_{i}.png')

            if os.path.exists(image_path):
                image = cv2.imread(image_path)
                height, width = image.shape[:2]

                gray_pixel_counts = count_gray_pixels(image)
                normalized_gray_values = normalize_gray_values(gray_pixel_counts)

                duration = (end_time - start_time).total_seconds()
                time_mappings = map_pixels_to_time(start_time.total_seconds(), duration, width)

                for pixel_num in range(width):
                    writer.writerow([
                        f"Image_{i}",
                        pixel_num + 1,
                        round(time_mappings[pixel_num], 3),
                        gray_pixel_counts[pixel_num],
                        round(normalized_gray_values[pixel_num], 3)
                    ])
            else:
                print(f"Image {image_path} not found.")

    print(f"Engagement data saved to {csv_file_path}")
