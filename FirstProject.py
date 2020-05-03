import os,shutil
dict_extensions={
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'video_extensions' : ('.mp4','.mkv','.MKV','.flv','.npeg','.MP4'),
    'document_extensions' : ('.pdf','.PDF','.SRT','.doc','.txt','.docx','.XML'),
}

folder_path = input('Enter the folder Path: ')

def file_finder(folderPath,file_extensions):
    files=[]
    for file in os.listdir(folderPath):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

# print(file_finder(folder_path,video_extensions))
for extension_name,extension_tuple in dict_extensions.items():
    folder_name = extension_name.split('_')[0] + ' files'
    new_folder_path = os.path.join(folder_path,folder_name)
    os.mkdir(new_folder_path)
    for item in (file_finder(folder_path,extension_tuple)):
        item_path = os.path.join(folder_path,item)
        item_new_path = os.path.join(new_folder_path,item)
        shutil.move(item_path,item_new_path)
    # print('calling file finder')
    # print(file_finder(folder_path,extension_tuple))
    
