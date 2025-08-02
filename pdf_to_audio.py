import os 
from pathlib import Path 
import PyPDF2
from gtts import gTTS

input_dir = Path("input")
output_dir = Path("output")

input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
            
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return None
    
def text_to_audio(text, output_filename):
    """
    Convert text to audio and save to a file
    """
    try:
        tts = gTTS(text=text, lang='en', slow=False)

        output_path = output_dir / output_filename
        tts.save(str(output_path))

        print(f"Successfully created {output_filename}")
        return True
    
    except Exception as e:
        print(f"Error converting text to audio: {e}")
        return False
    
def convert_pdf_to_audio(pdf_path):
    """
    Main function to convert a single PDF to audio
    """
    text = extract_text_from_pdf(pdf_path)
    
    if text is None:
        print(f"Could not extract text from {pdf_path}")
        return False
    
    pdf_name = pdf_path.stem
    output_filename = f"{pdf_name}.mp3"
    
    success = text_to_audio(text, output_filename)
    
    return success

if __name__ == "__main__":
    pdf_files = list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the input directory!")
        print("Please place PDF files in the 'input' folder.")
    else:
        print(f"Found {len(pdf_files)} PDF file(s) to convert...")
        
        for pdf_file in pdf_files:
            print(f"\nConverting: {pdf_file.name}")
            success = convert_pdf_to_audio(pdf_file)
            
            if success:
                print(f"✅ Successfully converted {pdf_file.name}")
            else:
                print(f"❌ Failed to convert {pdf_file.name}")
        
        print("\nConversion complete!")