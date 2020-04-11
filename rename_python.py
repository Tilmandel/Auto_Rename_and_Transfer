import os
from shutil import copy2 as cp

sourece_folder_not_renamed_All = r'.'
sourece_folder_not_renamed_All_double_check = r'.\double-check-not-renamed'
sourece_folder_renamed_all = r'.\Renamed_all'
all_language_dict = {"felu": "fexx", "fglu": "fgxx", "fflu": "ffxx"}


class Walk_and_file_read_move(object):
    def __init__(self):
        "map all var to avoid remapping this over and over"
        self.walk_renamed_folder = os.walk(sourece_folder_renamed_all)
        self.walk_root_folder = os.walk(sourece_folder_not_renamed_All)
        self.walk_duble_check = os.walk(sourece_folder_not_renamed_All_double_check)
        self.read_to_be_renamed_file = open("list_to_be_renamed.txt", "r+")
        self.write_all_renamed_file = open("_list_of_renamed.txt", "w+")
        self.write_duble_check_list_to_file = open("double_check_list.txt", "w+")

    def _read_to_be_renamed_file(self):
        opend = self.read_to_be_renamed_file
        read = opend.read()
        data = read.split("\n")
        return data

    def _write_check_file(self, folder, file_to_write):
        "loop thru all pdf that are found in pointed directory and write this list to provided file."
        for root, dirs, files in folder:
            list_of_duble_check = files
        for item in list_of_duble_check:
            file_to_write.writelines(item + "\n")
        file_to_write.writelines("Sum: {}".format(len(list_of_duble_check)))

    def _move_to_be_renamed(self, item):
        for file in item:
            for end_with in all_language_dict:
                src = sourece_folder_not_renamed_All + "\\" + file + end_with + ".pdf"
                dest = sourece_folder_renamed_all + "\\" + file + all_language_dict[end_with] + ".pdf"
                try:
                    print(file + all_language_dict[end_with])
                    cp(src, dest)
                    os.remove(src)
                except BaseException:
                    print(file + all_language_dict[end_with])
                    src = sourece_folder_not_renamed_All + "\\" + file +all_language_dict[end_with] + ".pdf"
                    cp(src, dest)
                    os.remove(src)


# ====Instance creation======
rename = Walk_and_file_read_move()
# ====Read what need to be moved and renamed, execute ======
read = rename._read_to_be_renamed_file()
move = rename._move_to_be_renamed(read)
# ====Write summary to files======
duble = rename._write_check_file(rename.walk_duble_check, rename.write_duble_check_list_to_file)
renamed = rename._write_check_file(rename.walk_renamed_folder, rename.write_all_renamed_file)
