import os

dataset_dir = "/s/fir/c/nobackup/cs515a/dataset"

def main():

    prog_lang = "cpp2"
    prog_ext = ".cpp"

    lang_dir = os.path.join(dataset_dir, prog_lang)
    lang_comp_dir = os.path.join(dataset_dir, prog_lang + "_comp")
    os.makedirs(lang_comp_dir)

    files_list = [f for f in os.listdir(lang_dir) if f.endswith(prog_ext)]

    for f in files_list:
        file_path = os.path.join(lang_dir, f)
        dest_path = os.path.join(lang_comp_dir, f) + ".zip"
        os.system("zip " + dest_path + " " + file_path)


if __name__ == "__main__":
    main()
