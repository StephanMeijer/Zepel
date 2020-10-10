# Zepel for Python

## Example usage

To be documented further soon.

```python
>>> client = ZepelClient("subdomain", 'api key')
>>> pr = ProjectsRepository(client)
>>> lr = ListsRepository(client)
>>> ir = ItemRepository(client)

>>> items = [ [ ir.index(list=list) for list in lr.index(project=p) ] for p in pr.index() ]
```
