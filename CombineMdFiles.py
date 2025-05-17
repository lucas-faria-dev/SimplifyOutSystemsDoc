import os

def combine_md_files(root_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in sorted(filenames):
                if filename.lower().endswith('.md'):
                    file_path = os.path.join(foldername, filename)
                    outfile.write(f"\n\n# {filename}\n\n")  # Optional: adds a header with the filename
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')  # Ensure spacing between files

# Example usage:
combine_md_files('path/to/your/folder', 'combined_output.md')