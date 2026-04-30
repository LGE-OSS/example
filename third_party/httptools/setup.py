import sys

vi = sys.version_info
if vi < (3, 5):
    raise RuntimeError('httptools require Python 3.5 or greater')
else:
    import os.path
    import pathlib

    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext as build_ext


setup(
    name='httptools',
    version='1.0.0',
    description='A collection of framework independent HTTP protocol utils.',
    url='https://github.com/MagicStack/httptools',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: Web Environment',
        'Development Status :: 5 - Production/Stable',
    ],
    platforms=['macOS', 'POSIX', 'Windows'],
    zip_safe=False,
    author='Yury Selivanov',
    author_email='yury@magic.io',
    license='MIT',
    packages=['httptools', 'httptools.parser'],
    include_package_data=True,
)
