from setuptools import setup

setup(name='conspiracygifting',
      version='0.1',
      description='Create a conspiracy!',
      url='http://github.com/rcackerman/conspiracygifting',
      author='Rebecca Ackerman',
      author_email='rcackerman@gmail.com',
      license='MIT',
      packages=['conspiracygifting'],
	  scripts=['bin/conspiracycmd'],
	  include_package_data=True,
	  package_data={'env':['.env']},
	  install_requires=['bottle==0.12.7','gunicorn==19.1.1','requests==2.4.3','misaka==1.0.2'],
      zip_safe=False)
