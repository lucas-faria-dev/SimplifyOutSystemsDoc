# Simplify OutSystems Doc AKA (Markdown Folder Combiner)

This Python script recursively scans a folder called `os-documentation`, finds all `.md` (Markdown) files in each subfolder, and combines them into a single Markdown file per folder.

All combined files are saved in a new folder called `combined_output`, which will be created in the same directory as the script.

## 📁 Folder Structure

```
project-folder/
├── os-documentation/
│   ├── section1/
│   │   ├── file1.md
│   │   └── file2.md
│   └── section2/
│       └── notes.md
├── combined_output/         <-- created automatically
│   ├── section1_combined.md
│   └── section2_combined.md
├── combine_script.py        <-- this script
└── README.md                <-- this README
```

## ✅ Features

* Traverses all subfolders inside the `os-documentation` folder.
* Combines only `.md` files within the same folder.
* Outputs combined files into `combined_output/`.
* Automatically names the output files based on the folder structure.
* Adds a heading with the original filename before each file's content (optional).

## 🚀 How to Use

1. Create a folder called `os-documentation`.
2. Place your [OutSystems documentation](https://github.com/OutSystems/docs-product/) files inside the `os-documentation` folder, organized however you'd like.
3. Run the script:

```bash
python combine_script.py
```

3. Find the results in the `combined_output` folder.

## 📝 Notes

* The script must be run from the same directory where it's located.
* The output file for each folder is named like `subfolder1_subfolder2_combined.md`.

## 🐍 Requirements

* Python 3.x (no external libraries needed)

## ✌🏼 Peace of mind

There is a .gitignore file configured for python (as per GitHub suggestion). Also git won't track files under the `os-documentation` folder, nor the `combined_output folder`. 

## ⭐ Contribution
Feel free to contribute.