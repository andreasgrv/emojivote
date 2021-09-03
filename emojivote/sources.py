import re
import requests
from html.parser import HTMLParser


class ArxivHTMLParser(HTMLParser):
    def __init__(self):
        super(ArxivHTMLParser, self).__init__()
        self.in_title = False

        self.authors = []
        self.abstract = None
        self.title = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name', None) == 'citation_title':
            self.title = attrs['content']
        elif tag == 'meta' and attrs.get('name', None) == 'citation_author':
            self.authors.append(attrs['content'])
        elif tag == 'meta' and attrs.get('name', None) == 'citation_abstract':
            self.abstract = attrs['content'].strip()

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

    @property
    def author_list(self):
        return ', '.join(self.authors)


class ArxivParser(object):
    """Extract information from an Arxiv page"""

    URL_REGEX = r'^https?://arxiv\.org'

    def __init__(self, url):
        super(ArxivParser, self).__init__()
        self._populate_urls(url)

    def _populate_urls(self, url):
        if url.endswith('.pdf'):
            abs_url = url[:-4]
            abs_url = abs_url.replace('pdf', 'abs')
            self.abstract_url = abs_url
        else:
            self.abstract_url = url
        pdf_url = self.abstract_url.replace('abs', 'pdf')
        pdf_url = '%s.pdf' % pdf_url
        self.pdf_url = pdf_url

    def gather_data(self):
        r = requests.get(self.abstract_url)
        if r.ok:
            html_parser = ArxivHTMLParser()
            html_parser.feed(r.text)
            # Filter out the [] from the title
            self.title = html_parser.title
            self.abstract = html_parser.abstract
            self.authors = html_parser.author_list

    @property
    def arxiv_id(self):
        return self.abstract_url.rsplit('/')[-1]

    @classmethod
    def process(cls, url):
        parser = cls(url)
        parser.gather_data()
        return dict(title=parser.title,
                    authors=parser.authors,
                    abstract=parser.abstract,
                    url=parser.pdf_url)

    @classmethod
    def recognise(cls, url):
        return re.match(cls.URL_REGEX, url) is not None
