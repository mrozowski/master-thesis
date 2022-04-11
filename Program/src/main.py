from ctypes import windll

import view
import presenter

def main():
    myappid = u'mrozowski.master-thesis.0.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    """Creating MVP"""
    _view = view.View()
    _presenter = presenter.Presenter(_view)
    _view.set_presenter(_presenter)
    _presenter.show()


if __name__ == "__main__":
    main()
