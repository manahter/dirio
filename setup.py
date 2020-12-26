import setuptools


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setuptools.setup(
    name='dirio',
    version='0.1.2',
    description='Python Independent Class Process. Uses serialization method with JSON',
    url='http://github.com/manahter/dirio',
    long_description_content_type='text/markdown',
    long_description=readme(),
    author='manahter',
    author_email='manahter@gmail.com',
    platforms=['Linux', 'Windows', 'Mac'],
    keywords=['independent', 'class', 'process', 'thread'],
    packages=setuptools.find_packages(),
    license='MIT',
    zip_safe=True,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 1 - Planning ',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
    ]
)

# Resources;
# https://www.codementor.io/@ajayagrawal295/how-to-publish-your-own-python-package-12tbhi20tf
# https://github.com/Carglglz/upydevice/blob/master/setup.py
# https://aligoren.com/python-ile-pypi-paketleri-olusturmak/
# https://twine.readthedocs.io/en/latest/
# https://pypi.org/classifiers/

# ################################
# ########## PYPi'ye modul yukleme
# ################################

# Twine yoksa, kur
#   $ pip install twine

# #################### Bu dizinde;
# Dist paketlerini olustur
#   $ python setup.py sdist bdist_wheel

# TestPyPi'ye gonderme:
#   $ twine upload -r testpypi dist/*
#       username: ...
#       password:
#       ...

# PYPi'ye gonderme:
#   $ twine upload dist/*

# Diğer Kullanım çeşitleri:
# Test PYPi'ye gönder
#   $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# Yüklü dosyaları atla, yüklenmemişleri gönder (Test PYPi için)
#   $ twine upload --repository-url https://test.pypi.org/legacy/ --skip-existing dist/*

# NOT: aynı isim ve versiyonda dosyayı birdaha yükleyemiyorsun.
