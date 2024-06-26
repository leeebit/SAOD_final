from flask import Flask
from models import Answer, Question, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        q = Question(question_number = 1, dif = "easy", question = "Что такое дерево в программировании?")
        db.session.add(q)
        ans_1 = Answer(answer = "Cпециальный вид красиво оформленного комментария, который программисты используют для украшения своего кода.", is_true = False, question = q)
        ans_2 = Answer(answer = "Место, где растут байты информации, подобно деревьям в лесу, но только в цифровом виде.", is_true = False, question = q)
        ans_3 = Answer(answer = "Структура данных, представляющая собой набор элементов (узлов), организованных иерархически.", is_true = True, question = q)
        ans_4 = Answer(answer = "Магический объект, который используется для ускорения работы алгоритмов за счет сбора маны из окружающей среды.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()


        q = Question(question_number = 2, dif = "easy", question = "Какого вида деревьев не было в теоретической части?")
        db.session.add(q)
        ans_1 = Answer(answer = "Бинарные деревья.", is_true = False, question = q)
        ans_2 = Answer(answer = "R-деревья.", is_true = True, question = q)
        ans_3 = Answer(answer = "B-деревья.", is_true = False, question = q)
        ans_4 = Answer(answer = "N-арные деревья.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 3, dif = "easy", question = "Что такое бинарные деревья?")
        db.session.add(q)
        ans_1 = Answer(answer = "Структура данных, в которой хранятся только бинарные данные.", is_true = False, question = q)
        ans_2 = Answer(answer = "Упорядоченные структуры данных, где для каждого узла значение в левом поддереве меньше, чем у корня, а в правом - больше.", is_true = True, question = q)
        ans_3 = Answer(answer = "Специальные компьютерные программы, созданные для автоматического распознавания и анализа форм бинарных файлов.", is_true = False, question = q)
        ans_4 = Answer(answer = "Способ кодирования информации в виде двоичных чисел, используемый для сжатия данных.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 4, dif = "easy", question = "Для чего деревья не используются?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для оптимизации поиска.", is_true = False, question = q)
        ans_2 = Answer(answer = "Для маршрутизации в сетях.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для хранения и оптимизации данных.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для преобразования данных произвольного размера в фиксированный размерный набор битов.", is_true = True, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 5, dif = "easy", question = "Какие алгоритмы рассматриваются в теоретической части?")
        db.session.add(q)
        ans_1 = Answer(answer = "Код Прюфера и алгоритм Краскала.", is_true = True, question = q)
        ans_2 = Answer(answer = "Код Прюфера и алгоритм Баруха.", is_true = False, question = q)
        ans_3 = Answer(answer = "Алгоритм Грэхема и алгоритм Краскала.", is_true = False, question = q)
        ans_4 = Answer(answer = "Алгоритм Грэхема и алгоритм Баруха.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 6, dif = "easy", question = "Сколько шагов в алгоритме, по которому создаётся код Прюфера?")
        db.session.add(q)
        ans_1 = Answer(answer = "7", is_true = True, question = q)
        ans_2 = Answer(answer = "3", is_true = False, question = q)
        ans_3 = Answer(answer = "10", is_true = False, question = q)
        ans_4 = Answer(answer = "1", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 7, dif = "easy", question = "Для чего используется код Прюфера?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для создания тайных кодов в качестве дополнительной защиты конфиденциальной информации.", is_true = False, question = q)
        ans_2 = Answer(answer = "Для создания уникальных идентификаторов персонажей в компьютерных играх.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для перевода текстовых сообщений в мнемонические последовательности, чтобы улучшить запоминаемость информации.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для представления дерева в виде последовательности чисел.", is_true = True, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 8, dif = "easy", question = "Для чего нужен алгоритм Краскала?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для выбора цветовой схемы при создании графических дизайнов и иллюстраций.", is_true = False, question = q)
        ans_2 = Answer(answer = "Для построение минимального остовного дерева во взвешенном связном графе.", is_true = True, question = q)
        ans_3 = Answer(answer = "оптимальной стратегии в настольных играх, таких как шахматы или го.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для выявления общих кластеров в социальных сетях или сетях связи для улучшения аналитики и прогнозирования поведения пользователей.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 9, dif = "easy", question = "Сколько шагов в алгоритме Краскала?")
        db.session.add(q)
        ans_1 = Answer(answer = "5", is_true = False, question = q)
        ans_2 = Answer(answer = "8", is_true = False, question = q)
        ans_3 = Answer(answer = "6", is_true = False, question = q)
        ans_4 = Answer(answer = "4", is_true = True, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 10, dif = "easy", question = "В какой области не применяется алгоритм Краскала?")
        db.session.add(q)
        ans_1 = Answer(answer = "Сетевой дизайн.", is_true = False, question = q)
        ans_2 = Answer(answer = "Хранение пространственных объектов.", is_true = True, question = q)
        ans_3 = Answer(answer = "Планирование маршрутов.", is_true = False, question = q)
        ans_4 = Answer(answer = "Транспортная логистика.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()


        q = Question(question_number = 1, dif = "medium", question = "Что такое N-арные деревья?")
        db.session.add(q)
        ans_1 = Answer(answer = "Деревья, каждый узел которого имеет до n потомков.", is_true = True, question = q)
        ans_2 = Answer(answer = "Деревья, в которых каждый узел имеет N потомков.", is_true = False, question = q)
        ans_3 = Answer(answer = "Деревья, в которых каждый узел имеет не менее N потомков.", is_true = False, question = q)
        ans_4 = Answer(answer = "Деревья, в которых количество узлов в каждом уровне не превышает N.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 2, dif = "medium", question = "Что такое АВЛ-дерево?")
        db.session.add(q)
        ans_1 = Answer(answer = "Структура данных, представляющая собой бинарное дерево поиска, где разница высоты поддеревьев каждого узла не превышает 1.", is_true = True, question = q)
        ans_2 = Answer(answer = "Дерево, где каждый узел содержит ссылки на левого и правого потомка.", is_true = False, question = q)
        ans_3 = Answer(answer = "Специальный вид бинарного дерева поиска, где каждый узел имеет две дополнительные ссылки на предыдущий и следующий узлы.", is_true = False, question = q)
        ans_4 = Answer(answer = "Двоичное дерево, где каждый узел содержит только одно значение.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 3, dif = "medium", question = "Для чего используются деревья отрезков?")
        db.session.add(q)
        ans_1 = Answer(answer = "для решения задач на отрезках массива.", is_true = True, question = q)
        ans_2 = Answer(answer = "Для организации иерархических структур данных, где каждый узел может иметь несколько потомков.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для представления иерархии файловой системы на компьютере.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для хранения информации о графах и выполнения операций поиска кратчайшего пути или поиска в глубину.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 4, dif = "medium", question = "Как используются деревья в сетях?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для организации иерархической структуры сетевых устройств, таких как коммутаторы и маршрутизаторы, обеспечивая эффективное управление и масштабируемость сети.", is_true = True, question = q)
        ans_2 = Answer(answer = "Для реализации алгоритмов маршрутизации, таких как алгоритм Дейкстры или алгоритм Беллмана-Форда, которые определяют кратчайшие пути в сети между узлами.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для организации структуры доменных деревьев в сетях TCP/IP, таких как дерево доменных имен (DNS), обеспечивая иерархическое распределение имен в Интернете.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для построения структур виртуальных частных сетей (VPN), обеспечивая изоляцию и безопасность трафика между различными сегментами сети.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 5, dif = "medium", question = "Где используются деревья решений?")
        db.session.add(q)
        ans_1 = Answer(answer = "В машинном обучении и анализе данных для прогнозирования и классификации данных на основе определенных признаков.", is_true = True, question = q)
        ans_2 = Answer(answer = "В компьютерных играх для принятия решений и управления поведением враждебных и союзных персонажей.", is_true = False, question = q)
        ans_3 = Answer(answer = "В бизнесе для принятия стратегических решений, таких как разработка маркетинговых стратегий или определение приоритетов инвестиций.", is_true = False, question = q)
        ans_4 = Answer(answer = "В медицинской диагностике для определения диагноза на основе клинических данных и симптомов пациента.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 6, dif = "medium", question = "Какова длина кода Прюфера по сравнению с количеством вершин?")
        db.session.add(q)
        ans_1 = Answer(answer = "Длина кода Прюфера всегда на две единицы меньше количества вершин.", is_true = True, question = q)
        ans_2 = Answer(answer = "Длина кода Прюфера всегда на единицу меньше количества вершин.", is_true = False, question = q)
        ans_3 = Answer(answer = "Длина кода Прюфера всегда равна количеству вершин.", is_true = False, question = q)
        ans_4 = Answer(answer = "Длина кода Прюфера может быть как меньше, так и больше количества вершин.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 7, dif = "medium", question = "Что такое остовное дерево?")
        db.session.add(q)
        ans_1 = Answer(answer = "Подграф связного неориентированного графа, который является деревом и включает все вершины исходного графа.", is_true = True, question = q)
        ans_2 = Answer(answer = "Подграф ориентированного графа, содержащий только часть вершин исходного графа.", is_true = False, question = q)
        ans_3 = Answer(answer = "Граф, который включает в себя все рёбра исходного графа.", is_true = False, question = q)
        ans_4 = Answer(answer = "Граф, в котором все вершины соединены между собой прямо или косвенно.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 8, dif = "medium", question = "Какой тип данных используются в коде Прюфера?")
        db.session.add(q)
        ans_1 = Answer(answer = "Целые числа, представляющие метки вершин.", is_true = True, question = q)
        ans_2 = Answer(answer = "Символы, соответствующие меткам вершин.", is_true = False, question = q)
        ans_3 = Answer(answer = "Действительные числа, представляющие веса рёбер.", is_true = False, question = q)
        ans_4 = Answer(answer = "Логические значения, обозначающие наличие или отсутствие рёбер между вершинами.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 9, dif = "medium", question = "Какая сложность у кода Прюфера?")
        db.session.add(q)
        ans_1 = Answer(answer = "Линейная сложность O(n), где n - количество вершин в дереве.", is_true = True, question = q)
        ans_2 = Answer(answer = "Квадратичная сложность O(n^2), где n - количество вершин в дереве.", is_true = False, question = q)
        ans_3 = Answer(answer = "Экспоненциальная сложность O(2^n), где n - количество вершин в дереве.", is_true = False, question = q)
        ans_4 = Answer(answer = "Логарифмическая сложность O(log n), где n - количество вершин в дереве.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 10, dif = "medium", question = "Какая сложность у алгоритма Краскала?")
        db.session.add(q)
        ans_1 = Answer(answer = "Сложность близкая к O(E log E), где E - количество рёбер в графе.", is_true = True, question = q)
        ans_2 = Answer(answer = "Линейная сложность O(n), где n - количество вершин в графе.", is_true = False, question = q)
        ans_3 = Answer(answer = "Квадратичная сложность O(n^2), где n - количество вершин в графе.", is_true = False, question = q)
        ans_4 = Answer(answer = "Логарифмическая сложность O(log n), где n - количество вершин в графе.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 1, dif = "hard", question = "Для чего используются цвета в красно-черных деревьях?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для представления балансировки дерева и поддержания его структуры.", is_true = True, question = q)
        ans_2 = Answer(answer = "Для обозначения различных типов узлов в дереве, таких как корень, листья и внутренние узлы.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для указания уровня важности узлов в дереве.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для дополнительной защиты от ошибок в процессе операций вставки, удаления и поиска в дереве.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 2, dif = "hard", question = "Где используются деревья выражений?")
        db.session.add(q)
        ans_1 = Answer(answer = "В компиляторах и интерпретаторах для преобразования и вычисления математических выражений в код машинного или промежуточного уровня.", is_true = True, question = q)
        ans_2 = Answer(answer = "В базах данных для представления и обработки иерархических структур данных, таких как деревья XML или JSON.", is_true = False, question = q)
        ans_3 = Answer(answer = "В программировании для построения и обработки структур данных, таких как деревья поиска или деревья бинарных выражений.", is_true = False, question = q)
        ans_4 = Answer(answer = "В компьютерной графике и обработке изображений для организации иерархических структур данных, таких как деревья сцены или деревья трансформаций.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 3, dif = "hard", question = "Где используются дендрограммы?")
        db.session.add(q)
        ans_1 = Answer(answer = "В биоинформатике для визуализации результатов анализа генетических данных и кластеризации биологических образцов.", is_true = True, question = q)
        ans_2 = Answer(answer = "В графическом дизайне для создания декоративных элементов с мотивами природы, таких как ветви или листья деревьев.", is_true = False, question = q)
        ans_3 = Answer(answer = "В области метеорологии для визуализации связей между различными климатическими параметрами, такими как температура, влажность и атмосферное давление.", is_true = False, question = q)
        ans_4 = Answer(answer = "В архитектуре и градостроительстве для представления иерархии элементов в городском планировании, таких как здания, улицы и парк", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 4, dif = "hard", question = "Что такое splay-деревья?")
        db.session.add(q)
        ans_1 = Answer(answer = "Это бинарные деревья поиска, в которых после каждой операции доступа к узлу этот узел перемещается ближе к корню дерева, чтобы улучшить время доступа к часто используемым элементам.", is_true = True, question = q)
        ans_2 = Answer(answer = "Это структуры данных, используемые для организации множества данных в виде дерева, где каждый узел имеет два потомка и одного родителя.", is_true = False, question = q)
        ans_3 = Answer(answer = "Это деревья, в которых каждый узел содержит только одно значение, а каждое поддерево рассматривается независимо.", is_true = False, question = q)
        ans_4 = Answer(answer = "Это специальные структуры данных, используемые для сжатия и хранения больших объемов данных в оперативной памяти.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 5, dif = "hard", question = "Как деревья используются в файловой системе?")
        db.session.add(q)
        ans_1 = Answer(answer = "Для организации иерархической структуры каталогов и файлов, где каждый узел представляет собой каталог или файл, а дочерние узлы соответствуют содержимому каталога или файлам внутри него.", is_true = True, question = q)
        ans_2 = Answer(answer = "Для сжатия и хранения файлов различных типов, обеспечивая быстрый доступ и эффективное управление данными.", is_true = False, question = q)
        ans_3 = Answer(answer = "Для обеспечения безопасности и контроля доступа к файлам и каталогам, путем управления правами доступа на уровне узлов дерева.", is_true = False, question = q)
        ans_4 = Answer(answer = "Для поддержки операций поиска, добавления, удаления и модификации файлов и каталогов в файловой системе.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()


        q = Question(question_number = 6, dif = "hard", question = "Где используются деревья разбора?")
        db.session.add(q)
        ans_1 = Answer(answer = "В компиляции программ для представления структуры и синтаксического анализа исходного кода.", is_true = True, question = q)
        ans_2 = Answer(answer = "В медицинской диагностике для анализа симптомов и постановки диагнозов.", is_true = False, question = q)
        ans_3 = Answer(answer = "В финансовой аналитике для прогнозирования курсов валют и ценных бумаг.", is_true = False, question = q)
        ans_4 = Answer(answer = "В производстве для оптимизации производственных процессов и управления ресурсами.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 7, dif = "hard", question = "Какие виды деревьев используются в симуляции и анализе?")
        db.session.add(q)
        ans_1 = Answer(answer = "Деревья принятия решений, используемые для моделирования принятия решений в различных ситуациях.", is_true = True, question = q)
        ans_2 = Answer(answer = "Деревья эволюции, применяемые для изучения эволюции видов и развития популяций в течение времени.", is_true = False, question = q)
        ans_3 = Answer(answer = "Деревья выражений, используемые для анализа и оценки математических выражений и формул.", is_true = False, question = q)
        ans_4 = Answer(answer = "Деревья игр, используемые для моделирования стратегий и анализа исходов в различных игровых сценариях.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 8, dif = "hard", question = "Какие виды деревьев используются для систематизации поиска?")
        db.session.add(q)
        ans_1 = Answer(answer = "Бинарные деревья.", is_true = True, question = q)
        ans_2 = Answer(answer = "Деревья вывода", is_true = False, question = q)
        ans_3 = Answer(answer = "Деревья решений", is_true = False, question = q)
        ans_4 = Answer(answer = "Деревья покрытия", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()
        
        q = Question(question_number = 9, dif = "hard", question = "Как восстанавливается дерево по коду Прюфера?")
        db.session.add(q)
        ans_1 = Answer(answer = "Дерево восстанавливается путем последовательного добавления рёбер в пустой граф. Каждый раз удаляется вершина с минимальным кодом Прюфера, и соответствующее ребро добавляется в дерево.", is_true = True, question = q)
        ans_2 = Answer(answer = "Дерево восстанавливается путем последовательного добавления рёбер в пустой граф. Каждый раз удаляется вершина с максимальным кодом Прюфера, и соответствующее ребро добавляется в дерево.", is_true = False, question = q)
        ans_3 = Answer(answer = "Дерево восстанавливается путем последовательного добавления вершин и рёбер. Сначала создается список смежности для каждой вершины, затем вершины добавляются в граф.", is_true = False, question = q)
        ans_4 = Answer(answer = "Дерево восстанавливается путем создания начального графа, содержащего все вершины, и последовательного удаления рёбер на основе кода Прюфера.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()

        q = Question(question_number = 10, dif = "hard", question = "Как создается минимальное остовное дерево с помощью алгоритма Краскала?")
        db.session.add(q)
        ans_1 = Answer(answer = "Алгоритм Краскала создает минимальное остовное дерево путем поочередного добавления ребер с наименьшим весом из исходного графа в пустой граф, при условии что добавление ребра не создает цикл.", is_true = True, question = q)
        ans_2 = Answer(answer = "Алгоритм Краскала создает минимальное остовное дерево путем поочередного удаления ребер с наименьшим весом из исходного графа до тех пор, пока граф не станет деревом.", is_true = False, question = q)
        ans_3 = Answer(answer = "Алгоритм Краскала создает минимальное остовное дерево путем выбора случайных вершин и построения дерева из них с использованием наименьшего количества ребер.", is_true = False, question = q)
        ans_4 = Answer(answer = "Алгоритм Краскала создает минимальное остовное дерево путем поочередного добавления ребер с наибольшим весом из исходного графа в пустой граф, при условии что добавление ребра не создает цикл.", is_true = False, question = q)
        db.session.add_all([ans_1, ans_2, ans_3, ans_4])
        db.session.commit()
