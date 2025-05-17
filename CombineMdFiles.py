import os

def combine_md_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_folder = os.path.join(base_dir, 'os-documentation')
    output_file = os.path.join(base_dir, 'combined_output.md')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in sorted(filenames):
                if filename.lower().endswith('.md'):
                    file_path = os.path.join(foldername, filename)
                    relative_path = os.path.relpath(file_path, root_folder)
                    outfile.write(f"\n\n# {relative_path}\n\n")  # Optional: include relative path as a header
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')

# Run the function
if __name__ == "__main__":
    combine_md_files()