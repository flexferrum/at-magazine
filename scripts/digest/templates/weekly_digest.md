# Еженедельный дайджест Author.Today {{fromDate}} - {{currentDate}}
{% set groupedUpdates = newBooks | groupby('mainGenre')%}

## Обновления по жанрам:
{% for g, l in groupedUpdates %}
### {{g}}
{% endfor %}