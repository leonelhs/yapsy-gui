#############################################################################
#
#   Setup based on Labelme install script:
#   https://github.com/wkentaro/labelme
#
##############################################################################
import os
import re

from setuptools import setup


def get_version():
    filename = "yapsygui/__init__.py"
    with open(filename) as f:
        match = re.search(
            r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M
        )
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_install_requires():
    install_requires = [
        "yapsy>=1.12.2",
        "qtpy>=1.11.2"
    ]

    # Find python binding for qt with priority:
    # PyQt5 -> PySide2
    # and PyQt5 is automatically installed on Python3.
    QT_BINDING = None

    try:
        import PyQt5  # NOQA

        QT_BINDING = "pyqt5"
    except ImportError:
        pass

    if QT_BINDING is None:
        try:
            import PySide2  # NOQA

            QT_BINDING = "pyside2"
        except ImportError:
            pass

    if QT_BINDING is None:
        # PyQt5 can be installed via pip for Python3
        # 5.15.3, 5.15.4 won't work with PyInstaller
        install_requires.append("PyQt5!=5.15.3,!=5.15.4")
        QT_BINDING = "pyqt5"

    del QT_BINDING

    if os.name == "nt":  # Windows
        install_requires.append("colorama")

    return install_requires


def main():
    setup(
        name='yapsygui',
        version=get_version(),
        packages=['yapsygui', 'yapsygui.ui'],
        url='https://github.com/leonelhs/yapsy-gui',
        license='Apache',
        author='leonel hernandez',
        author_email='leonelhs@gmail.com',
        description='GUI for Yapsy plugin system',
        install_requires=get_install_requires(),
        package_data={"yapsygui": ["template.html", "plugins/*.py", "plugins/*.plugin"]},
        entry_points={"console_scripts": ["yapsygui=yapsygui.__main__:main"]},
    )


if __name__ == "__main__":
    main()
