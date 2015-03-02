import sys
import argparse
import os

def insertLicenseToSingleFile(file_path, license_text, extensions, test):
    print('Inserting license to file: ' + file_path)
    if not test and file_path.endswith(tuple(extensions)):
        with open(file_path,'r+', encoding='utf8') as f:
            content = f.read()
            f.seek(0,0)
            f.write(license_text + '\n' + content)

def process(path, license_path, extensions, ignored_files, test):
    with open(license_path, encoding='utf8') as f:
        license = f.read()

    for folder, subs, files in os.walk(path):
        for filename in files:
            path = os.path.join(folder, filename)
            if ignored_files is None or not filename in ignored_files: 
                insertLicenseToSingleFile(path, license, extensions, test)

def main():
    parser = argparse.ArgumentParser(description='Inserts license text to source files.')
    parser.add_argument('path', help='Specifies directory of target files.')
    parser.add_argument('license', help='Path to license file.')

    parser.add_argument('--extensions', nargs='*', help='Extensions of target files.')
    parser.add_argument('--ignorefiles', nargs='+', help='List of filenames to ignore.')
    parser.add_argument('-t', '--test', help='Test run. Will print which files will be modified, but will not modify them.', action='store_true')

    args = parser.parse_args()

    process(args.path, args.license, args.extensions, args.ignorefiles, args.test)

if __name__ == "__main__":
    main()