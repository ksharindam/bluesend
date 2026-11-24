from setuptools import setup


setup(
    name='bluesend',
    #version="1.0",
    packages=['bluesend'],
    entry_points={
      'gui_scripts': ['bluesend=bluesend.main:main'],
    },
    data_files=[
        ('share/applications', ['data/bluesend.desktop']),
        ('share/file-manager/actions', ['data/bluetooth-share.desktop'])
    ],
    include_package_data=True,
    zip_safe=False
)
