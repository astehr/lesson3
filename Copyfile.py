import shutil

PATH_TO_FILE = 'File/old.txt'
def create_result_file():
    """Делаю новый файл, идентичный исходному, с другим названием"""
    src_file_obj = open(PATH_TO_FILE, 'rb')
    new = open(PATH_TO_FILE.rsplit('.', 1)[0] + '_res.txt', 'wb')
    shutil.copyfileobj(src_file_obj, new)


