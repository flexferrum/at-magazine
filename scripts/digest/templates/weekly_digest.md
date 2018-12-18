# Еженедельный дайджест Author.LastWeek {{fromDate}} - {{currentDate}}
{% set groupedUpdates = newBooks | groupby('mainGenre')%}

## Новые работы по жанрам:
{% for g, l in groupedUpdates %}
[spoiler={{g}} ({{l | length}}) (нажми, чтобы прочитать)]
{% for book in l -%}
{% if book.isNew -%}
**{{ book.author | trim }}** {{ 'разместил(а)' if book.isFinished else 'добавил(а)' }} книгу "[{{ book.title }}]({{ book.url }})"

{% if book.annotation is defined and (book.annotation | trim | length) > 0 -%}
`{{ book.annotation | replace('<br/>', '') | truncate }}`

{% endif -%}
{% elif book.isFinished -%}
**{{ book.author | trim }}** завершил(а) книгу "[{{ book.title }}]({{ book.url }})"
{% else -%}
**{{ book.author | trim }}** обновил(а) книгу "[{{ book.title }}]({{ book.url }})"
{% endif -%}
{%endfor %}
[/spoiler]
{% endfor %}