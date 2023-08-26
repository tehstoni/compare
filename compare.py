def compare_files(file1, file2):
    # Read the contents of both files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    lmhash_password = {}
    for line in file2_lines:
        parts = line.strip().split(':')
        if len(parts) == 2:
            lmhash, password = parts
            lmhash_password[lmhash] = password

    for line in file1_lines:
        parts = line.strip().split(':')
        if len(parts) >= 4:
            full_name = parts[0]
            name_parts = full_name.split('\\')
            if len(name_parts) > 1:
                name = name_parts[1]
            else:
                name = full_name
            lmhash = parts[3]
            if lmhash in lmhash_password:
                password = lmhash_password[lmhash]
                print(f"{full_name}:{lmhash}:{password}")
        else:
            print(f"Invalid entry: {line.strip()}")
            
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Please provide two input files.")
    else:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
        compare_files(file1_path, file2_path)
