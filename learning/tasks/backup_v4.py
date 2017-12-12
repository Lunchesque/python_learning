import os
import time

source = ['C:\\try']    #путь каталога, который надо скопировать

target_dir = 'C:\\Backup'   #путь основного каталога резервного копирования

today = target_dir + os.sep + time.strftime('%Y%m%d')   #текущаяя дата, служит именм подкаталога в основном каталоге

now = time.strftime('%H%M%S')   #текущее время, служит именем zip-архива

comment = input('Введите комметарий --> ')      #запрос комментария пользователя
if len(comment) == 0:   #проверка введн ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):   #создание каталога если его еще нет
    os.mkdir(today)     #создание каталога
print('Каталог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))    #команда zip для перемещения файлов в zip-архив

#запуск создания резервной копии
if os.system(zip_command) == 0:     #os.system возвращает 0 если команда выполняется упешно
    print('Резервная копия создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
