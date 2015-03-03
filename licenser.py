import sys
import argparse
import os

def hasLicense(content, license_text):
    return content.startswith(license_text)

def insertLicenseToSingleFile(file_path, license_text, extensions):
    if extensions is None or file_path.endswith(tuple(extensions)):
        with open(file_path,'r+', encoding='utf8') as f:
            content = f.read()
            if not hasLicense(content, license_text):
                f.seek(0,0)
                print('Inserting license to file: ' + file_path)
                f.write(license_text + '\n' + content)

def process(path, license_path, extensions, ignored_files):
    with open(license_path, encoding='utf8') as f:
        license = f.read()

    for folder, subs, files in os.walk(path):
        for filename in files:
            path = os.path.join(folder, filename)
            if ignored_files is None or not filename in ignored_files: 
                insertLicenseToSingleFile(path, license, extensions, test_run)

def main():
    parser = argparse.ArgumentParser(description='Inserts license text to source files.')
    parser.add_argument('path', help='Specifies directory of target files.')
    parser.add_argument('license', help='Path to license file.')

    parser.add_argument('--extensions', nargs='*', help='Extensions of target files.')
    parser.add_argument('--ignorefiles', nargs='+', help='List of filenames to ignore.')

    args = parser.parse_args()

    process(args.path, args.license, args.extensions, args.ignorefiles)

if __name__ == "__main__":
    main()