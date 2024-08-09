from setuptools import setup, find_packages

setup(
    name='quick-flaskwind',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Flask',
    ],
    entry_points='''
        [console_scripts]
        create-flask-tailwind=flask_tailwind_template.cli:create_project
    ''',
    package_data={
        'flask_tailwind_template': [
            'template/templates/*',
            'template/static/css/*',
        ],
    },
    author='Liam Stamper',
    author_email='liam.stamper@gmail.com',
    description='A CLI tool to create Flask and Tailwind CSS projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
