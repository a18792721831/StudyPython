from xlrd import open_workbook
from createSql import getSql


def excel2Sql():
    print('Please input file path:')
    filePath = input()
    excelFile = open_workbook(filePath)
    sheet = excelFile.sheet_by_index(0)
    print('Please input author:')
    author = input()
    with open(filePath.replace('.xlsx', '.sql'), 'a') as file:
        for r in range(1, sheet.nrows):
            row = sheet.row_values(r)
            file.write(getSql(int(row[0]), row[1], row[2], author))


if __name__ == "__main__":
    excel2Sql()