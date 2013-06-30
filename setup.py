from distutils.core import setup
import structclass

setup(
    name='StructClass',
    version=structclass.__version__,
    packages=['structclass',],
    author='David Berthelot',
    license=open('LICENCE.txt').read(),
    long_description=open('README.md').read(),
    url='https://github.com/david-berthelot/StructClass'
)
