import os
from yt_heatmap_getter import extract_svgs_from_youtube
from svg_to_png import modify_and_convert_svgs
from data_extractor import extract_engagement_data

# Directory setup
SVG_FOLDER = './svgs'
MODIFIED_SVG_FOLDER = './modified_svgs'
PNG_FOLDER = './pngs'
CSV_FOLDER = './csv'

# Create directories if they don't exist
for folder in [SVG_FOLDER, MODIFIED_SVG_FOLDER, PNG_FOLDER, CSV_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def run_pipeline(video_url):
    """Complete pipeline to download SVGs, modify them, and extract data."""
    
    # Step 1: Download SVGs from YouTube
    print("Step 1: Downloading SVG heatmaps from YouTube...")
    extract_svgs_from_youtube(video_url)

    # Step 2: Modify SVGs and convert to PNGs
    print("Step 2: Modifying SVGs and converting to PNGs...")
    modify_and_convert_svgs(SVG_FOLDER, MODIFIED_SVG_FOLDER, PNG_FOLDER)

    # Step 3: Extract engagement data from PNGs and save to CSV
    print("Step 3: Extracting engagement data from PNGs...")
    csv_path = os.path.join(CSV_FOLDER, 'engagement_data.csv')
    extract_engagement_data(PNG_FOLDER, csv_path)

    print(f"Pipeline complete! Engagement data saved to {csv_path}.")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    run_pipeline(video_url)
