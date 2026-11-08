import os
import pymupdf4llm
import pathlib

def convert_pdfs_in_directory():
    # Define directories
    current_dir = pathlib.Path(__file__).parent
    output_dir = current_dir / "converted_docs"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Find all PDF files in the current directory
    pdf_files = list(current_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    print(f"Found {len(pdf_files)} PDF files. Starting conversion...")
    
    for pdf_file in pdf_files:
        try:
            print(f"Converting: {pdf_file.name}...")
            
            # Convert PDF to Markdown
            md_text = pymupdf4llm.to_markdown(str(pdf_file))
            
            # Define output filename
            output_filename = f"{pdf_file.stem}.md"
            output_path = output_dir / output_filename
            
            # Write Markdown to file
            output_path.write_text(md_text, encoding="utf-8")
            
            print(f"✓ Saved to: {output_path.relative_to(current_dir)}")
            
        except Exception as e:
            print(f"✗ Failed to convert {pdf_file.name}: {e}")

    print("\nAll done! Check the 'converted_docs' folder.")

if __name__ == "__main__":
    convert_pdfs_in_directory()
