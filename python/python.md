# python

## type hints

```python
def get_filename_from_conf(**kwargs) -> Optional[str]:
    file_name = smt.get('file_path')  # Returns None if 'file_name' is not present.
    return file_path
```

Here, `Optional[str]` is equivalent to `Union[str, None]`, indicating that the function might return None.
