import os


def mergeFile(filePath1, filePath2):
    if filePath1 is not None and filePath1.strip() != '' and \
            filePath2 is not None and filePath2.strip() != '':
        file1 = open(filePath1, 'a', encoding = 'utf-8')
        file2 = open(filePath2, 'r', encoding = 'utf-8')
        file1.write(file2.read())
        file1.close()
        file2.close()
        os.remove(filePath2)
