# PDF to Audio Converter

A Python script to convert PDF files to MP3 audio files using text-to-speech technology.

## Project Structure

```
pdf_to_audio/
├── pdf_to_audio.py          # Main conversion script
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── input/                   # Place PDF files here to convert
├── output/                  # Generated MP3 files will be saved here
└── utils/
    └── text_processor.py    # Helper functions for text processing
```

## Features

- Convert PDF files to MP3 audio
- Batch processing of multiple PDF files
- Text cleaning and formatting
- Error handling for corrupted files
- Google Text-to-Speech integration

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Place PDF files in the `input/` directory

3. Run the script:
   ```
   python pdf_to_audio.py
   ```

## Usage

The script will:
1. Read all PDF files from the `input/` directory
2. Extract text from each PDF
3. Clean and format the text
4. Convert text to speech
5. Save MP3 files in the `output/` directory

## Dependencies

- PyPDF2 - PDF text extraction
- gTTS - Google Text-to-Speech
- pathlib - File path handling 