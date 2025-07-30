# Maintainer: Your Name <your.email@example.com>
pkgname=dirlink
pkgver=1.0.1
pkgrel=3
pkgdesc="A Tiny CLI Tool For Faster Command Line File System Navigation"
arch=('any')
url="https://github.com/BravestCheetah/DirLink"   # Your project homepage or repo URL
license=('MIT')
depends=('python' 'python-pyperclip')
makedepends=('python' 'python-pip')  # Optional, if building needs them
source=("https://github.com/BravestCheetah/DirLink/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('SKIP') # I dont wanna go through the hassle of doing this every new release

prepare() {
  cd "$srcdir"
  tar xf "v${pkgver}.tar.gz"
}

package() {
  install -dm755 "$pkgdir/usr/lib/python3.13/site-packages/dirlink"
  cp -r "$srcdir/dirlink-${pkgver}/src/dirlink/"* "$pkgdir/usr/lib/python3.13/site-packages/dirlink/"

  install -dm755 "$pkgdir/usr/bin"
  cat > "$pkgdir/usr/bin/dirlink" << EOF
#!/bin/bash
exec python3 -m dirlink.cli "\$@"
EOF
  chmod +x "$pkgdir/usr/bin/dirlink"
}
