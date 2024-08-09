import os
import shutil
import subprocess
import click

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'quick-flaskwind')

def copy_template(destination):
    if os.path.exists(destination):
        raise FileExistsError(f"Directory {destination} already exists.")
    shutil.copytree(TEMPLATE_DIR, destination)

def run_command(command, cwd):
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        raise RuntimeError(f"Command {command} failed.")

@click.command()
@click.argument('project_name')
def create_project(project_name):
    """Creates a new Flask and Tailwind CSS project."""
    try:
        copy_template(project_name)
        print(f"Created project directory {project_name}")
        print("Installing Python dependencies...")
        run_command(f"pip install -r requirements.txt", cwd=project_name)
        print("Installing npm packages...")
        run_command(f"npm install", cwd=project_name)
        print("Building Tailwind CSS...")
        run_command(f"npm run build-css", cwd=project_name)
        print("Setup completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    create_project()