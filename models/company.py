class Company:
    def __init__(self, url):
        self.url = url
        self.domain = None
        self.name = None
        self.description = None
        self.industry = None
        self.technologies = []
        self.jobs = []
        self.evidence = []
        self.insights = []
        self.score = None