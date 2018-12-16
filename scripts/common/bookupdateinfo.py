from datetime import datetime


class BookUpdateInfo:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.author = ''
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()
        self.textLength = 0
        self.isFinished = False
        self.annotation = ''
        self.adultOnly = False
        self.mainGenre = ''
        self.subGenres = []

    @staticmethod
    def createFromJson(node) :
        result = BookUpdateInfo()

        result.title = node['title']
        result.author = node['author']
        result.annotation = node['abstract']
        result.mainGenre = node['main_genre']

        result.createdAt = datetime.utcfromtimestamp(int(node['created_at']))
        result.updatedAt = datetime.utcfromtimestamp(int(node['updated_at']))
        result.isFinished = False if node['is_finished'] == 'False' else True
        result.adultOnly = False if node['adult_only'] == 'False' else True
        return result
