import shutil

path = 'File/old.txt'
def create_result_file():
    """Делаю новый файл, идентичный исходному, с другим названием"""
    src_file_obj = open(path, 'rb')
    new = open(path.rsplit('.', 1)[0] + '_res.txt', 'wb')
    shutil.copyfileobj(src_file_obj, new)


