from datetime import datetime


class BookInfo:

    def __init__(self):
        self.id = 0
        self.title = ''
        self.url = ''
        self.author = ''
        self.authorUsername = ''
        self.annotation = ''
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()
        self.textLength = 0
        self.isFinished = False
        self.isDraft = False
        self.isCommercial = False
        self.viewCount = 0
        self.likeCount = 0
        self.commentCount = 0
        self.reviewCount = 0
        self.adultOnly = False
        self.mainGenre = ''
        self.subGenres = []
        self.tags = []
