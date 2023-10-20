import os

def count_md_files(directory="."):
    """
    Count the number of .md files in the given directory, excluding README.md.
    """
    return sum(1 for filename in os.listdir(directory) if filename.endswith('.md') and filename != "README.md")

def update_readme(number):
    """
    Update README.md with the new number.
    """
    readme_path = "./README.md"

    # If the file doesn't exist, create it with the header
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as file:
            file.write(f"---\nnumber:{number}\n---\n")
        return

    # Read the existing file content
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    # Check if the header exists and update it
    if lines and lines[0] == "---\n" and lines[2] == "---\n":
        lines[1] = f"number:{number}\n"
    else:  # If header doesn't exist, prepend it
        lines = [f"---\nnumber:{number}\n---\n"] + lines

    # Write the updated content back to README.md
    with open(readme_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    number = count_md_files()
    update_readme(number)
    print(f"Updated README.md with {number} .md files.")
