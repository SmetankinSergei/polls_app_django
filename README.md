<h1>Polls app Django</h1>

<h2>Описание</h2>
<p>Веб-приложение на базе Django для проведения опросов и возможностью динамического 
отображения вопросов в зависимости от ответов пользователя.</p>
<p>Приложение включает в себя модели для опросов и ответов, а также следующие функции:</p>
<ul>
<li>Создание и редактирование опросов и вопросов через панель администратора</li>
<li>Реализован веб-интерфейс, позволяющий пользователям проходить опросы и отвечать на вопросы</li>
<li>Сохранение ответов пользователей в связке с соответствующими опросами</li>
<li>Содержит логику, позволяющую определить, какие вопросы показывать или скрывать 
в зависимости от предыдущих ответов пользователя (т.е. дерево)</li>
<li>Вывод результатов опросов, включая статистику ответов на каждый вопрос, после 
завершения опроса:
    <ul>
    <li>Общее количество участников опроса</li>
    <li>На каждый вопрос:
        <ul>
        <li>Количество ответивших и их доля от общего количества участников (в процентах)</li>
        <li>Порядковый номер вопроса по количеству ответивших. Если количество совпадает, 
то и номер должен совпадать (например, для трёх вопросов с 95, 95, 75 ответивших 
получаются соответствующие им номера 1, 1, 2)</li>
        <li>Количество ответивших на каждый из вариантов ответа и их доля от общего количества 
ответивших на этот вопрос после завершения опроса (в процентах)</li>
        </ul>
    </li>
    </ul>
</li>
</ul>

<h2>Dependencies</h2>
<p>requirements.txt</p>

<h2>P.S.</h2>
<p>Для Вашего удобства в демонстрационных целях добавлены dump-файлы таблиц.</p>
<p>Порядок загрузки:</p>
<ol>
<li>poll_data.json</li>
<li>question_data.json</li>
<li>answer_data.json</li>
</ol>