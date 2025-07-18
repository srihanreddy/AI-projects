import os
import tkinter as tk
from tkinter import filedialog
from summarizer.extractor import extract_text_from_pdf
from summarizer.generator import summarize_chunks

# Create chunks without chunker.py
def split_text_into_chunks(text, max_tokens=1000):
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk.split()) + len(para.split()) <= max_tokens:
            current_chunk += "\n" + para
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# === Step 1: Ask user to select a PDF ===
root = tk.Tk()
root.withdraw()
pdf_path = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF Files", "*.pdf")]
)

if not pdf_path:
    print("❌ No file selected. Exiting.")
    exit()

# === Step 2: Extract PDF text ===
print("📤 Extracting text from PDF...")
raw_text = extract_text_from_pdf(pdf_path)

if not raw_text.strip():
    print("❌ PDF is empty or scanned. Cannot summarize.")
    exit()

# === Step 3: Chunk + Summarize ===
print("🧩 Splitting into chunks...")
chunks = split_text_into_chunks(raw_text)

print("🧠 Summarizing chunks...")
summary = summarize_chunks(chunks)

# === Step 4: Save output ===
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "summary.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(summary)

print(f"\n✅ Summary saved to '{output_path}'")
