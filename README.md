YouTube Video Engagement Data Extractor

This project provides a pipeline for extracting engagement data from YouTube videos using heatmap visualizations provided by YouTube. The pipeline involves downloading heatmaps in SVG format, modifying them, converting them to PNGs, and finally extracting pixel data to analyze viewer engagement.
Features

    Heatmap Extraction: Automatically downloads heatmap SVGs from YouTube videos using Selenium.
    SVG Modification and Conversion: Modifies SVG properties (such as color) and converts them to PNG format for analysis.
    Engagement Data Extraction: Analyzes the pixel data from PNG images to determine viewer engagement at different points in the video.
    Video Segmentation: Processes the video in predefined segments and maps engagement data to those segments.

    Note: The segmentation data currently used in this project corresponds to a specific video. A future feature will automatically extract segment data from any video, making the tool fully adaptable.

Installation
Prerequisites

Ensure you have the following installed:

    Python 3.x
    pip (Python package manager)
    Firefox and geckodriver for Selenium browser automation.

Install the necessary Python packages:

bash

pip install selenium cairosvg opencv-python-headless numpy

Setup

    Clone the repository:

    bash

git clone https://github.com/your-username/engagement-data-extractor.git
cd engagement-data-extractor

Install the required packages:

bash

    pip install -r requirements.txt

    Configure Selenium with Firefox: Ensure that geckodriver is installed and available in your system’s PATH.

Usage
Running the Pipeline

You can run the entire engagement data extraction pipeline by providing the YouTube video URL.

bash

python main.py

You will be prompted to enter the YouTube video URL. The pipeline consists of the following steps:

    Step 1: Downloads SVG heatmaps from the YouTube video using Selenium.
    Step 2: Modifies the downloaded SVGs and converts them to PNG format for analysis.
    Step 3: Extracts engagement data from the PNGs and stores it in a CSV file.

Example Folder Structure

After running the pipeline, the following folder structure will be generated:

graphql

.
├── svgs/               # Contains original SVG heatmaps downloaded from YouTube.
├── modified_svgs/      # Contains modified SVGs with adjusted colors.
├── pngs/               # Contains PNGs generated from the modified SVGs.
├── csv/                # Contains the extracted engagement data in CSV format.

CSV Output

The engagement data is saved in csv/engagement_data.csv, where you’ll find pixel-wise data such as:

    Image: The PNG file associated with the segment.
    Pixel: The pixel number on the x-axis of the image.
    Time (s): The mapped time in the video corresponding to that pixel.
    Gray Value: The gray pixel count at that position.
    Normalized Engagement (%): The normalized engagement percentage based on pixel intensity.

Files

    main.py: Orchestrates the entire pipeline.
    yt_heatmap_getter.py: Downloads SVG heatmaps from YouTube using Selenium.
    svg_to_png.py: Modifies the SVGs and converts them to PNG format.
    data_extractor.py: Extracts gray pixel data from PNGs to compute engagement metrics.
    segments.py: Defines the segments for a specific video. This data is currently hardcoded but will be extracted dynamically in future versions.

Roadmap

    Automatic Segmentation: Implement a feature to automatically detect and extract segment information for any video.
