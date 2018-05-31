import azure.storage.file.fileservice

fs = azure.storage.file.fileservice.FileService(
    account_name='TTsensitivedata', 
    sas_token=<REDACTED>)

fs.get_file_to_path('secrets', None, 'config.txt', 'config')
