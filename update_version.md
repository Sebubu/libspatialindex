# Update version

This document is written for collaborators and describes how to update the package on PyPi.
This tutorial as basically aligned with [python packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/).


### Accounts

- [Test PyPi](https://test.pypi.org/user/apgsga/)
- [PyPi](https://pypi.org/user/apgsga/)

### Projects
- [libspatialindex on PyPi](https://pypi.org/project/libspatialindex/)


### Update version

Be sure you have installed the `requirements.txt` and your pip is up to date.

- Update version in setup.py.
- Build library.
```bash
# Build library
python3 setup.py sdist bdist_wheel
```

- If everything is ok, upload the packge to PyPi.
```bash
twine upload dist/*
```
