import PySimpleGUI as sg
import zipfile
import os


folder = sg.popup_get_folder('请选择要压缩的文件夹')
zip_path = sg.popup_get_file(
  '请选择要保存的压缩包位置',
  save_as=True,
  default_extension='zip',
  file_types=(('压缩包', '.zip'), )
)

with zipfile.ZipFile(zip_path, 'w') as zipobj:
  for file in os.scandir(folder):
    zipobj.write(file.path, file.path.replace(folder, '.'))

zip_size = os.stat(zip_path).st_size // 1024
sg.popup(f'压缩包体积大小为：{zip_size} KB')