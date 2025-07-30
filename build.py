#!/usr/bin/env python3

import os
import subprocess
import shutil
import hashlib
from pathlib import Path

try:
    import tomllib
except ImportError:
    print("Error: The 'tomllib' module is not available. Ensure you're using Python 3.11 or later.")
    exit(1)

# 1. Extract version from pyproject.toml
project_root = Path(__file__).resolve().parent
pyproject_path = project_root / 'pyproject.toml'

if not pyproject_path.exists():
    print(f"Error: {pyproject_path} not found.")
    exit(1)

with open(pyproject_path, 'rb') as f:
    pyproject_data = tomllib.load(f)

try:
    version = pyproject_data['project']['version']
except KeyError:
    print("Error: Version not found in pyproject.toml under [project].")
    exit(1)

print(f"Version: {version}")

# 2. Check if source tarball exists
sdist = project_root / f'dist/dirlink-{version}.tar.gz'
if not sdist.exists():
    print(f"Source tarball not found: {sdist}")
    print("Running uv build ...")
    subprocess.run(['uv', 'build', '--sdist'], check=True)
    if not sdist.exists():
        print("Still not found; looked in dist/")
        exit(1)

# 3. Create temporary build directory
wd = Path(subprocess.check_output(['mktemp', '-d'], text=True).strip())
print(f"Working dir: {wd}")
shutil.copy(sdist, wd)
os.chdir(wd)

# 4. Create PKGBUILD
pkgbuild_content = f"""# Maintainer: Your Name <you@example.com>
pkgname=dirlink
pkgver={version}
pkgrel=1
pkgdesc="DirLink utility"
arch=('any')
url=""
license=('MIT')
depends=('python')
source=("dirlink-{version}.tar.gz")
sha256sums=($(sha256sum "dirlink-{version}.tar.gz" | awk '{{print $1}}'))

build() {{
  cd "dirlink-{version}"
  python setup.py build
}}

package() {{
  cd "dirlink-{version}"
  python setup.py install --root="$pkgdir" --prefix=/usr
}}
"""
with open('PKGBUILD', 'w') as f:
    f.write(pkgbuild_content)

# 5. Run makepkg
print("Running makepkg ...")
subprocess.run(['makepkg', '--force', '--nocheck', '--syncdeps'], check=True)

# 6. Find and install the package
pkg = next(wd.glob(f'dirlink-{version}-*.pkg.tar.zst'), None)
if not pkg:
    print("No package built!")
    exit(1)

print(f"Built package: {pkg}")
print("Installing package...")
subprocess.run(['sudo', 'pacman', '-U', '--noconfirm', str(pkg)], check=True)

print("Done.")
