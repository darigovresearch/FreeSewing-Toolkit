# generate_terms_csv.py is code to convert terms markdown into a csv file

# standard imports
import os
import csv

# non standard imports
import markdown as md


def parse_data():
    """parse_data is code to get relevant data from folder structure"""
    print("Running parse_data")

    # getting folder names
    x = os.listdir()
    print(x)

    folder_names = []

    for i in range(0, len(x)):
        temp_split = x[i].split(".")
        # print(temp_split)
        if len(temp_split) == 1:
            folder_names.append(x[i])
        else:
            pass

    print(folder_names)

    # generating content
    titles = ["Term", "Definition"]
    rows = []

    for i in range(0, len(folder_names)):

        temp_row = []
        os.chdir(folder_names[i]) # changing folder
        temp_file = open("en.md", "r") # opening en file
        full_content = temp_file.read() # getting content
        # print(full_content)

        temp_file.close() # closing file it's no longer needed

        split_content = full_content.split("---") # splitting content by "---"
        # print(split_content)

        temp_term = split_content[1][8:-1]
        # print(temp_term)

        temp_row.append(temp_term)

        markdown_definition = md.markdown(split_content[2])
        temp_row.append(markdown_definition)
        rows.append(temp_row)

        os.chdir("..") # returning back to source folder

    print(rows)
    print(len(rows))

    # exporting to csv
    export = open('FreeSewing_terms.csv', 'w')
    write = csv.writer(export)
    write.writerow(titles)
    write.writerows(rows)
    export.close()


if __name__ == '__main__':
    parse_data()
