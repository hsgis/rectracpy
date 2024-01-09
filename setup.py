from setuptools import setup

setup(name='rectrac',
      version='0.1',
      description='RecTrac SDK',
      long_description='Classes and methods for use in Calling RecTrac for purposes of integration',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
	  keywords='api integration',
      url='',
      author='Joel Conrad, Town of Holly Springs',
      author_email='joel.conrad@hollyspringnc.gov',
      license='MIT',
 
      packages=[
          'rectrac'
      ],
      install_requires=[
          'pydantic'
      ],
	  include_package_data=True,
      zip_safe=False)
