from setuptools import setup, find_packages

setup(
    name = 'stock_func',
    version = '0.0.1',
    description='주식 보조 함수들',
    url = 'https://github.com/YongYeonKan/Stock_func.git',
    author= '간용연',
    author_email= 'youngyoun501@naver.com',
    license = '라이센스 이름',
    packages=find_packages(),
    install_requires = ['pandas'],
)