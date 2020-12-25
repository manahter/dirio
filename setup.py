import setuptools


def readme():
    with open('README.md', 'r', encoding="utf-8") as f:
        return f.read()


setuptools.setup(
    name='dirio',
    version='0.1.0',
    description='Python Independent Class Process. Uses serialization method with JSON',
    url='http://github.com/manahter/dirio',
    long_description_content_type='text/markdown',
    long_description=readme(),
    author='manahter',
    author_email='manahter@gmail.com',
    platforms=['Linux', 'Windows', 'Mac'],
    packages=setuptools.find_packages(),
    license='MIT',
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning ',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
    ]
)

# Resources;
# https://pypi.org/classifiers/
# https://www.codementor.io/@ajayagrawal295/how-to-publish-your-own-python-package-12tbhi20tf
# https://github.com/Carglglz/upydevice/blob/master/setup.py
