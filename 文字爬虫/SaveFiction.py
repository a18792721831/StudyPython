def saveFiction(fiction, filePath):
    if fiction is not None and fiction.strip() != '':
        file = open(filePath, 'w', encoding='utf-8')
        file.write(fiction)
        file.close()
