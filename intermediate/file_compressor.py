# file_compressor.py
import zipfile

def compress_files(zip_name, *files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
            print(f"Added {file} to {zip_name}")

if __name__ == "__main__":
    compress_files('archive.zip', 'file1.txt', 'file2.txt')
