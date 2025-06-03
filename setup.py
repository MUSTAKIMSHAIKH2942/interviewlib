from setuptools import setup, find_packages

setup(
    name='interviewlib',
    version='0.1.0',
    packages=find_packages(),
    description='Python interview questions and solutions library',
    author='Mustakim Shaikh',
    author_email='mustakim.shaikh.prof@gmail.com',
    url='https://github.com/yourusername/interviewlib',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        '',
    ],
    python_requires='>=3.6',
)
