import os

def combine_md_per_folder():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_folder = os.path.join(base_dir, 'os-documentation')
    output_root = os.path.join(base_dir, 'combined_output')

    os.makedirs(output_root, exist_ok=True)

    for foldername, subfolders, filenames in os.walk(root_folder):
        md_files = [f for f in sorted(filenames) if f.lower().endswith('.md')]
        if md_files:
            relative_path = os.path.relpath(foldername, root_folder)
            output_filename = relative_path.replace(os.sep, '_') or 'root'
            output_path = os.path.join(output_root, f'{output_filename}_combined.md')

            with open(output_path, 'w', encoding='utf-8') as outfile:
                for md_file in md_files:
                    file_path = os.path.join(foldername, md_file)
                    outfile.write(f"\n\n# {md_file}\n\n")  # Optional: filename as heading
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')

if __name__ == "__main__":
    combine_md_per_folder()
