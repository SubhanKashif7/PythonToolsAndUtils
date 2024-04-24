from setuptools import setup, find_packages

setup(
    name='pytimefunctions',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'threading'
    ],
    author='Subhan Kashif',
    author_email='ksubhank38@gmail.com',
    description='setInterval and setTimeout funcs of js alternatives in python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_package',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
