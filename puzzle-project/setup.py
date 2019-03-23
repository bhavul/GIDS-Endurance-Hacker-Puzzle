from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon'
]

setup(name='puzzle',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = puzzle:main
      """,
      )