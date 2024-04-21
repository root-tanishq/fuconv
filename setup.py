from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='fuconv',
    version='0.0.1',
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='uint and hex values converter for solidity CTFs',
    url='https://github.com/root-tanishq/fuconv',
    author='Tanishq Rathore',
    license='MIT',
    packages=['fuconv'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'fuconv = fuconv.__main__:main'
        ]
    },
)