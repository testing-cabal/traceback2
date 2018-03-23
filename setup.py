import setuptools
import traceback2

setuptools.setup(
    version=traceback2.__version__,
    setup_requires=['pbr'],
    pbr=True)

