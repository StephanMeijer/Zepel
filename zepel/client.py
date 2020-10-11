import requests
from dataclasses import dataclass, field
from marshmallow_dataclass import dataclass
from datetime import datetime
from typing import Optional, List

from .url import get_url

class ZepelClient():
    subdomain: str = None
    token: str = None

    def __init__(self, subdomain: str, token: str):
        """
        >>> ZepelClient(None, 'token')
        Traceback (most recent call last):
          ...
        AssertionError
        >>> ZepelClient('subdomain')
        Traceback (most recent call last):
          ...
        TypeError: __init__() missing 1 required positional argument: 'token'
        """
        assert subdomain
        assert token

        self.subdomain = subdomain
        self.token = token

    def headers(self):
        """
        >>> client = ZepelClient("developmenthuis", "alpha-beta-gamma-abc-xyz")
        >>> client.headers()
        {'Authorization': 'Bearer alpha-beta-gamma-abc-xyz'}
        """
        return {
            'Authorization': "Bearer " + self.token
        }

    def get_url(self, name: str, **kwargs):
        """
        >>> client = ZepelClient('sub', 'token')
        >>> client.get_url('projects')
        'https://sub.zepel.io/api/v1/projects'
        """
        kwargs['subdomain'] = self.subdomain

        for arg in [ 'list', 'project', 'item', 'board' ]:
            if kwargs.get(arg):
                kwargs = {
                    **kwargs,
                    **kwargs.get(arg).meta,
                    arg + '_id': kwargs.get(arg).id
                }

        return get_url(name, **kwargs)

    def wrap_call(self, schema, name: str, **kwargs):
        response = requests.get(self.get_url(name, **kwargs), headers=self.headers())

        if response.status_code == 200:
            value = response.json().get(name)

            if type(value) is list:
                return [ schema.load({ **entity, 'meta': kwargs }) for entity in response.json().get(name) ]

            return schema.load({ **value, 'meta': kwargs })
        else:
            raise Exception(response)

class Repository():
    client: ZepelClient = None

    def __init__(self, client: ZepelClient):
        assert client

        self.client = client

@dataclass
class ZepelProject():
    id: str
    title: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    key: Optional[str]

    meta: dict

@dataclass
class ZepelList():
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: datetime
    type: Optional[str]
    project_id: Optional[str]
    default_board_id: Optional[str]

    meta: dict

@dataclass
class ZepelItem():
    id: str
    title: Optional[str]
    type: Optional[str]
    parent_id: Optional[str]
    due_date: Optional[datetime]
    assignee_ids: Optional[List[str]]
    is_archived: bool
    tags: List[str]
    updated_at: datetime
    created_at: datetime
    status_id: Optional[str]
    estimate: Optional[float]
    description: Optional[str]
    list_id: Optional[str]
    key: Optional[str]
    requestor_id: Optional[str]
    section_id: Optional[str]
    project_id: Optional[str]

    meta: dict

class ProjectRepository(Repository):
    def index(self, **kwargs):
        return self.client.wrap_call(ZepelProject.Schema(), 'projects', **kwargs)

    def get(self, **kwargs):
        return self.client.wrap_call(ZepelProject.Schema(), 'project', **kwargs)

class ListRepository(Repository):
    def index(self, **kwargs):
        return self.client.wrap_call(ZepelList.Schema(), 'lists', **kwargs)

    def get(self, **kwargs):
        return self.client.wrap_call(ZepelList.Schema(), 'list', **kwargs)

class ItemRepository(Repository):
    def index(self, **kwargs):
        return self.client.wrap_call(ZepelItem.Schema(), 'items', **kwargs)

    def get(self, **kwargs):
        return self.client.wrap_call(ZepelItem.Schema(), 'item', **kwargs)
