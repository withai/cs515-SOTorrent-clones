import os
import sys

import matplotlib.pyplot as plt
import numpy as np

def main():

    dataset_dir = "/s/fir/c/nobackup/cs515a/dataset/"

    files = [f for f in os.listdir(dataset_dir) if f.startswith("codeSnippets")]

    line_split = "&#xD;&#xA;"

    pl_counts = {}

    for file_name in files:
        file_path = os.path.join(dataset_dir, file_name)
        with open(file_path, "r") as f:
            next(f)
            for line in f:
                try:
                    line = line[1:-1]
                    code_lines = line.split(line_split)
                    for code_line in code_lines:
                        if("<!-- language:" in code_line):
                            language = code_line[4:-3].split(":")[1].strip()
                            language = language.lower()
                            if(language.startswith("lang-")):
                                language = language[5:]
                            try:
                                pl_counts[language] += 1
                            except KeyError:
                                pl_counts[language] = 1
                            break
                except:
                    pass

    pl_counts["c++"] += pl_counts['cpp']

    pl_tuple = [(pl_counts_key, pl_counts[pl_counts_key]) for pl_counts_key in pl_counts]
    pl_tuple.sort(key=lambda x: x[1], reverse=True)

    top_10 = pl_tuple[:10]

    pl_languages = [x[0] for x in top_10]
    pl_count = [x[1] for x in top_10]

    y_pos = np.arange(len(pl_languages))

    plt.figure(figsize=(10,10))
    plt.bar(y_pos, pl_count, align='center', alpha=0.5)
    plt.xticks(y_pos, pl_languages, fontsize=14)
    plt.ylabel('Number of code blocks', fontsize=14)
    plt.title('Number of code blocks in SOTorrent dataset in top 10 programming languages', fontsize=16)
    plt.yscale('log')
    plt.savefig("/s/fir/c/nobackup/cs515a/graphs/top-10-languages.png")







if __name__ == "__main__":
    main()
