##  _ctypes
### Intro
ImportError: DLL load failed while importing _ctypes: The specified module could not be found.
### Reason
LibFFI code is harder to maintain. Thus, it stops at since Python 3.8 . 

    On some OSes (Win included) LibFFI code (at least the needed part) was duplicated in Python codebase and built into _ctypes.pyd. Although it was easier at the beginning, it's not a good practice as it becomes very hard to maintain if one needs to keep the referred software up to date, and also licensing might become a problem. So, since Python 3.8 they stopped doing that

![image](https://github.com/40843245/Python_Tutorial/assets/75050655/99785081-c18f-49da-b49d-e3a62d595c88)

### Ref
https://stackoverflow.com/questions/73458524/importerror-dll-load-failed-while-importing-ctypes-the-specified-module-coul
