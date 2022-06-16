def main(article: str = '') -> str:
    """
    :param article:
    :return title
    """
    if len(article) > 25:
        title = article[0:25].rsplit(' ', 1)[0] + '...'
        return title
    elif len(article) <= 25 and article.endswith('...'):
        return article
    else:
        return article
