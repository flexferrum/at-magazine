# Еженедельный дайджест Author.Today {{fromDate}} - {{currentDate}}
{% set groupedUpdates = newBooks | groupby('mainGenre')%}

## Обновления по жанрам:
{% for g, l in groupedUpdates %}
### {{g}} ({{l | length}})
{% endfor %}