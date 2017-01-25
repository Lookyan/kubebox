from distutils.core import setup


setup(
    name='kubebox',
    version='0.1',
    description='Auto doc generation for confluence from swagger',
    packages=[
        'cmd',
        'utils'
    ],
    scripts=[
        'cmd/kubebox.py'
    ]
)
