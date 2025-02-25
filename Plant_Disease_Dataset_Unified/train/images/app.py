import os

def count_files_in_directories(base_path="."):
    directories = []
    for root, dirs, files in os.walk(base_path):
        if root == base_path:
            for directory in dirs:
                dir_path = os.path.join(base_path, directory)
                file_count = sum([len(files) for _, _, files in os.walk(dir_path)])
                directories.append((directory, file_count))
    return directories

def generate_latex_table(directories):
    latex_code = r"""
    \documentclass{article}
    \usepackage{booktabs}
    \begin{document}
    \begin{table}[h]
        \centering
        \begin{tabular}{l c}
            \toprule
            Directory Name & Number of Files \\
            \midrule
    """
    
    for directory, file_count in directories:
        latex_code += f"            {directory} & {file_count} \\\n"
    
    latex_code += """\
            \bottomrule
        \end{tabular}
        \caption{Number of Files in Each Directory}
        \label{tab:dir_files}
    \end{table}
    \end{document}
    """
    
    return latex_code

def main():
    base_path = "./"  # Change this to the target directory
    directories = count_files_in_directories(base_path)
    latex_table = generate_latex_table(directories)
    
    with open("directory_list.tex", "w") as file:
        file.write(latex_table)
    
    print("LaTeX file 'directory_list.tex' has been generated.")

if __name__ == "__main__":
    main()

