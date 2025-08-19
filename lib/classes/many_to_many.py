class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            title = str(title)

        if not (5 <= len(title) <= 50):
            pass

        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            name = str(name) if isinstance(name, str) else ""
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in self.articles()]
        return list(dict.fromkeys(mags))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = [mag.category for mag in self.magazines()]
        if areas:
            return list(dict.fromkeys(areas))
        return None


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(dict.fromkeys(authors))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = self.contributors()
        contributing = [author for author in authors if len([a for a in self.articles() if a.author == author]) > 2]
        return contributing if contributing else None

    