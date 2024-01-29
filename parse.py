from typing import List, Union, Callable
from bs4 import BeautifulSoup, Tag, NavigableString

def is_header(element: Union[Tag, NavigableString, None]) -> bool:
    """
    Returns true if the element is the header of a documentation entry 
    """
    if element.name == 'p':
        for element_2 in element:
            if element_2.name:
                element_2_class = element_2.get("class")
                if element_2_class and element_2_class[0] == 'SIntrapara':
                        if element_2.find('blockquote', class_='SVInsetFlow'):
                            return True
    return False


def bs4_parser(entry: List[Union[Tag, NavigableString, None]]) -> str:
    """
    Basic built-in BS4 parser
    """
    return "\n".join(e.get_text() for e in entry)

def get_entries(page_html: str, entry_parser: Callable[[List[Union[Tag, NavigableString, None]]], str] = bs4_parser) -> List[str]:
    """
    Returns a parsed list of documentation entries from the given HTML
    """
    soup = BeautifulSoup(page_html, "html.parser")
    body = soup.find('div', class_='main')

    entries = []
    last_header = None
    for i, element in enumerate(body.children):
        if element.name and is_header(element):
            if last_header is not None:
                entry = body.contents[last_header:i]
                entries.append(entry)
            last_header = i

    return [entry_parser(e) for e in entries]
    

