import os
import time

#путь каталога, который надо скопировать
source = ['C:\\try']

#путь основного каталога резервного копирования
target_dir = 'C:\\Backup'

#текущаяя дата, служит именм подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')

#текущее время, служит именем zip-архива
now = time.strftime('%H%M%S')

#создание каталога если его еще нет
if not os.path.exists(today):
    os.mkdir(today)     #создание каталога
print('Каталог успешно создан', today)

#задание имени zip-файла
target = today + os.sep + now + '.zip'

#команда zip для перемещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#запуск создания резервной копии
if os.system(zip_command) == 0:     #os.system возвращает 0 если команда выполняется упешно
    print('Резервная копия создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
