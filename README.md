### Python DIC Software 

This is a Python implementation of digital image correlation functions which are still in beta status. Nevertheless you can already use the Python functions to analyse your set of images to calculate different kind of displacements and strains.
Functions can be use to filter and correlate images first before analysing results using a graphical user interface.

### Acknowledgment:  
* Code Author: Charlie Bourigault
* Involved People: Melanie Senn, Chris Eberl
* Collaborators for strain measurements and reviewers: Felix Schiebel, Tobias Kennerknecht, Marco Sebastiani, Jiří Dluhoš
* Partial funding was provided by the European iStress project (http://www.stm.uniroma3.it/iSTRESS/Pages/iSTRESS%20Home%20page.aspx)
  
### License

Copyright 2016 Fraunhofer IWM  

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0  

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Dependencies and Installation

This project has been updated to use PySide6 for the Qt bindings (previously PyQt4). Install the runtime dependencies with:

```bash
pip install -r requirements.txt
```

If you prefer a single package, install PySide6 directly:

```bash
pip install PySide6
```

Migration notes:

- Qt binding: Project was migrated from PyQt4 to PySide6. Import statements now use `from PySide6.QtWidgets import *`, `from PySide6.QtCore import *`, and `from PySide6.QtGui import *`.
- Dialog execution: `exec_()` calls have been replaced with `exec()` for PySide6.
- Signals: `pyqtSignal` usage has been updated to `Signal` from `PySide6.QtCore`.
- Regular expressions: `QRegExp`/`QRegExpValidator` were replaced by `QRegularExpression`/`QRegularExpressionValidator` for Qt6 compatibility.
- Matplotlib backend: Qt backend imports have been updated from `backend_qt4agg` to `backend_qtagg`.

If something in the UI behaves differently after the migration, check for differences in API signatures such as `QFileDialog` return values or other Qt6 changes.
