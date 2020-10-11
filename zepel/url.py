import re



def get_url(name: str, **kwargs):
    """
    This magic creates an dictionary with string keys and functions as values. The functions take the
    arguments placed in the URIs of the API.

    Usage example:
        urls.get('project')(subdomain='example')

    Tests...

    >>> get_url('projects', subdomain="test")
    'https://test.zepel.io/api/v1/projects'

    >>> get_url('project', subdomain='test', project_id=123)
    'https://test.zepel.io/api/v1/projects/123'

    >>> get_url('lists', subdomain='abcproject', project_id='none-of-your-business')
    'https://abcproject.zepel.io/api/v1/projects/none-of-your-business/lists'

    >>> get_url('list', subdomain='abc', project_id='123', list_id='xyz')
    'https://abc.zepel.io/api/v1/projects/123/lists/xyz'

    >>> get_url('items', subdomain='abc', project_id='123', list_id='xyz')
    'https://abc.zepel.io/api/v1/projects/123/lists/xyz/items'

    >>> get_url('item', subdomain='abc', project_id='123', list_id='xyz', item_id=9999)
    'https://abc.zepel.io/api/v1/projects/123/lists/xyz/items/9999'

    >>> get_url('test', subdomain='test')
    Traceback (most recent call last):
     ...
    TypeError: 'NoneType' object is not callable

    >>> get_url('project', subdomain='sub')
    Traceback (most recent call last):
     ...
    KeyError: 'project_id'
    """
    return dict([ ( k, url.format ) for k, url in [
        ('projects', 'https://{subdomain}.zepel.io/api/v1/projects'),
        ('project', 'https://{subdomain}.zepel.io/api/v1/projects/{project_id}'),
        ('lists', 'https://{subdomain}.zepel.io/api/v1/projects/{project_id}/lists'),
        ('list', 'https://{subdomain}.zepel.io/api/v1/projects/{project_id}/lists/{list_id}'),
        ('items', 'https://{subdomain}.zepel.io/api/v1/projects/{project_id}/lists/{list_id}/items'),
        ('item', 'https://{subdomain}.zepel.io/api/v1/projects/{project_id}/lists/{list_id}/items/{item_id}')
    ] ]).get(name)(**kwargs)
