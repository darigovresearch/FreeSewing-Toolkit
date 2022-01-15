# generate_pattern_docs.py is code to make the docs folder structure for new patterns

# imports
import os


# relevant filder names
docs_folders = [
    "cutting",
    "fabric",
    "instructions",
    "needs"
]

# relevant titles
docs_titles = [
    "Cutting",
    "Fabric options",
    "Construction",
    "What you need"
]


def generate_folder_structure(pattern_name):
    """generate_folder_structure is code to make the folder structure for a
    given pattern name"""
    print("Generating folder structure:")

    # generate the initial folder
    try:
        os.mkdir(pattern_name)
    except Exception as e:
        print(pattern_name + " folder already generated")

    os.chdir(pattern_name)

    for i in range(0, len(docs_folders)):
        print("\tGenerating subfolder-" + docs_folders[i])

        # making all sub folders
        try:
            os.mkdir(docs_folders[i])
        except Exception as e:
            print(docs_folders[i] + " folder already generated")

        os.chdir(docs_folders[i])

        # making the file
        x = open("en.md", "w")

        # writing content to the file
        temp_text = "<Fixme>\nComplete documentation for " + pattern_name + "\n</Fixme>"
        x.write(temp_text)

        # closing the file
        x.close()

        # going back to the main folder
        os.chdir("..")

    print("\nFolder structure for '" + name + "' has been generated, you can now copy it to the correct folder of your fork of the monorepo to fill in")


if __name__ == '__main__':
    name = input("What is the name of your pattern? - ")

    generate_folder_structure(name)
