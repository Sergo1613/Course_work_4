<h1>Парсер вакансий</h1>

В файле `api.py` создали абстрактный класс для работы с API сайтов с вакансиями.\
Реализовал классы `HeadHunterAPI` и `SuperJobAPI`, наследующиеся от абстрактного класса, для работы с конкретными платформами, которые подключаются к API и получают вакансии.

В файле `vacancy.py` создал класс `Vacancy` для работы с вакансиями.\
В этом классе определил атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования.\
Реализовал методы сравнения вакансий между собой по зарплате.\
Также реализовал функцию `to_json` для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.

В файле `jsonhandler.py` реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.

В файле `utils.py` создал функцию для взаимодействия с пользователем.\
Взаимодействие выполняется через бесконечный цикл.\
Программа приветствует нас и позволяет выбрать платформу для поиска или сделать выход из неё.\
Если пользователь выбирает 1 или 2, программа уточняет какой запрос выполнить с помощью ввода через консоль, если пользователей набирает 3 - выход из программы.\
Дальше создается экземпляр класса для работы с API сайтов с вакансиями, получаем вакансии с платформы.\
Если данной вакансии нет, выводим, что нет такой вакансии.\
Если все успешно фильтруем и сортируем вакансии, создаем экземпляр класса `Vacancy` для дальнейшей работы с вакансиями.\
Программа уточняет какое количество вакансий мы хотим видеть, также ввод числа происходит через консоль.\
Сохраняем последнюю вакансию из предыдущего списка в `json файл 'vacancy.json'` при помощи ввода через консоль команды `yes`, если ввести другое значение, программа завершится.




