import os

def sort():
    all_files = os.listdir()
    files = [f for f in all_files if os.path.isfile(f) and f != "sorter.py"]
    
    for f in files:
        print('Sorting: ' + f)
        split_file = f.rsplit('.', 1)
        if(len(split_file) < 2):
            extension = "no_extension"
        else:
            extension = split_file[-1]
        
        if(not os.path.isdir(extension)):
            os.mkdir(extension)
        os.replace(f, "{}/{}".format(extension, f))

if __name__ == "__main__":
    sort()
