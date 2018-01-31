class Articles:
    """
   Blueprint for my articles 
    """

    def __init__(self, id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Source:
    """
    Blueprint for my Sourcece class
    """

    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
    






     






        