import site
import shutil
import subprocess
from pathlib import Path

def manual_installation():
    """
    This function manually installs the required packages and copies the current folder to site-packages.
    """
    print("=== Manual installation ===")

    print('Installing required dependencies...')
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print('Error: ' + str(e))
        return

    print('Copying the module to site-packages...')
    try:
        site_packages_folder = Path(site.getsitepackages()[0])
        module_folder = (Path(__file__).resolve().parent / 'pyZUnivers')
        shutil.copytree(module_folder, site_packages_folder / 'pyZUnivers')
    except shutil.Error as e:
        print('Error: ' + str(e))
        return

    print('Installation completed successfully!')

if __name__ == '__main__':
    manual_installation()