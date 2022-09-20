from setuptools import setup, find_packages

setup(name='clean_folder',
      version='1.0.0',
      description='sorting and cleaning folder',
      url='https://github.com/Trotoria/GoIT_HW/blob/main/Core/Module_07/clean_folder',
      author='Viktoriia Trotska',
      author_email='trotoria@icloud.com',
      license='MIT',
      packages=find_packages(),
      # install_requires=['pathlib', 'sys', 'pprint', 'shutil'],
      entry_points={'console_scripts': [
          'clean-folder=clean_folder.clean:main']},
      include_package_data=True
      )
