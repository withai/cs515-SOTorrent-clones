import os
import random

dataset_dir = "/s/fir/c/nobackup/cs515a/dataset"

def main():

    prog_lang = "cpp2"
    prog_ext = ".cpp.zip"

    lang_dir = os.path.join(dataset_dir, prog_lang+"_comp")

    paths_file = os.path.join(lang_dir, "paths.txt")

    files_list = [f for f in os.listdir(lang_dir) if f.endswith(prog_ext)]

    # files_list_pick = random.sample(files_list, k=10000)

    with open(paths_file, "w") as paths_f:
        for f in files_list:
            paths_f.write(os.path.join(lang_dir, f) + "\n")


if __name__ == "__main__":
    main()
