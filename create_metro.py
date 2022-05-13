from metro_graph_builder import Metro

SaintP_metro = Metro()
SaintP_metro.create_line(['Парнас',
                          'Проспект просвещения',
                          'Озерки',
                          'Удельная',
                          'Пионерская',
                          'Черная речка',
                          'Петроградская',
                          'Горьковская',
                          'Невский проспект',
                          'Сенная площадь',
                          'Технологический институт 2',
                          'Фрунзенская',
                          'Московские ворота',
                          'Электросила',
                          'Парк победы',
                          'Московская',
                          'Звездная',
                          'Купчино'], 3)
SaintP_metro.create_line(['Девяткино',
                          'Гражданский проспект',
                          'Академическая',
                          'Политехническая',
                          'Площадь мужества',
                          'Лесная',
                          'Выборгская',
                          'Площадь Ленина',
                          'Чернышевская',
                          'Площадь восстания',
                          'Владимирская',
                          'Пушкинская',
                          'Технологический институт 1',
                          'Балтийская',
                          'Нарвская',
                          'Кировский завод',
                          'Автово',
                          'Ленинский проспект',
                          'Проспект ветеранов'], 3)

SaintP_metro.create_line(['Беговая',
                          'Новокрестовская',
                          'Приморская',
                          'Василеостровская',
                          'Гостиный двор',
                          'Маяковская',
                          'Площадь александра невского 1',
                          'Елизаровская',
                          'Ломоносовская',
                          'Пролетарская',
                          'Обухово',
                          'Рыбацкое'], 3)

SaintP_metro.create_line(['Спасская',
                          'Достоевская',
                          'Лиговский проспект',
                          'Площадь александра невского 2',
                          'Новочеркасская',
                          'Ладожская',
                          'Проспект большевиков',
                          'Улица дыбенко'], 3)

SaintP_metro.create_line(['Комендантский проспект',
                          'Старая деревня',
                          'Крестовский остров',
                          'Чкаловская',
                          'Спортивная',
                          'Адмиралтейская',
                          'Садовая',
                          'Звенигородская',
                          'Обводный канал',
                          'Волковская',
                          'Бухарестская',
                          'Международная',
                          'Проспект славы',
                          'Дунайская',
                          'Шушары'], 3)

SaintP_metro.add_edge('Технологический институт 2', 'Технологический институт 1', 1)
SaintP_metro.add_edge('Невский проспект', 'Гостиный двор', 1)
SaintP_metro.add_edge('Площадь восстания', 'Маяковская', 1)
SaintP_metro.add_edge('Площадь александра невского 1', 'Площадь александра невского 2', 1)
SaintP_metro.add_edge('Достоевская', 'Владимирская', 1)
SaintP_metro.add_edge('Звенигородская', 'Пушкинская', 1)
SaintP_metro.add_edge('Садовая', 'Спасская', 1)
SaintP_metro.add_edge('Садовая', 'Сенная площадь', 1)
SaintP_metro.add_edge('Сенная площадь', 'Спасская', 1)


SaintP_metro.save_metro('Saint-Petersburg_Metro_graph.json')
