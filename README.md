# Yapsy QT GUI
## Python plugin manager

This project is a GUI python plugin manager. Backend is implemented over [Yapsy](https://github.com/tibonihoo/yapsy/)

### Basic plugin structure:


###### plugin1.plugin

```properties
# Plugin descriptor file
[Core]
Name = Plugin Test
Module = plugin1

[Documentation]
Author = Leonel Hernandez
Version = 0.1
Website = https://github.com/leonelhs/
Description = This is a demo plugin
```

######  plugin1.py
```python
# Plugin module file
from qtpy.QtWidgets import QPushButton
from yapsy.IPlugin import IPlugin


class PluginOne(IPlugin):

    def __init__(self):
        super().__init__()
        self.context = None
        self.name = "Plugin test-01"

    def action(self, context):
        self.context = context
        button = QPushButton(self.name)
        button.clicked.connect(self.task)
        context.layout().addWidget(button)

    def task(self):
        self.context.output.append("This is a text from plugin test-01")
```
### Minimal Application
```python
import sys
from qtpy import QtWidgets
from qtpy.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextBrowser
from yapsygui import DialogPlugins


def fetchPlugins(plugins):
    for plugin in plugins:
        plugin.plugin_object.action(win)


app = QtWidgets.QApplication()
win = QWidget(None)
win.setLayout(QVBoxLayout())
btn_manager = QPushButton("Show Manager")
win.layout().addWidget(btn_manager)

manager = DialogPlugins(win, "./plugins")
manager.connect(fetchPlugins)
manager.loadPlugins()

btn_manager.clicked.connect(manager.show)
win.output = QTextBrowser(win)
win.layout().addWidget(win.output)

win.show()
sys.exit(app.exec_())
```            

### Install 

```console
foo@bar:~$ pip install yapsygui
foo@bar:~$ yapsygui
```

### For install a new plugin just locate plugin descriptor
<img src="https://drive.google.com/uc?export=view&id=1XtvcdVRvxMAIulBRnz47yH11UaBcpQGL"/>

### Test plugin action
<img src="https://drive.google.com/uc?export=view&id=1e71NxPSuQ_jgOCNL0zwXZcs9cRm7j60I"/>


