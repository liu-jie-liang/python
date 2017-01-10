import sys

from PyQt4 import QtGui

app = QtGui.QAppliction(sys.arv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle("simple")
widget.show()

sys.exit(app.exec_())