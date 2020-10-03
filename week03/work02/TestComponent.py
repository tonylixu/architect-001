from NamedContainerComponent import NamedContainerComponent
from LeafComponent import LeafComponent


class TestComponent2:
    def __init__(self):
        pass

    def test(self):
        winForm = NamedContainerComponent('WinForm')
        frame = NamedContainerComponent('FRAME1')

        picture = LeafComponent('Picture')
        login = LeafComponent('Button-login')
        register = LeafComponent('Button-register')
        label1 = LeafComponent('Label-username')
        textbox1 = LeafComponent('TextBox-TextField')
        label2 = LeafComponent('Label-password')
        passwordbox = LeafComponent('Password-PasswordField')
        checkbox = LeafComponent('CheckBox-Check')
        textbox2 = LeafComponent('TextBox-Remember password')
        linklabel = LeafComponent('LinkLabel-Forget password')

        frame.add_node(label1)
        frame.add_node(textbox1)
        frame.add_node(label2)
        frame.add_node(passwordbox)
        frame.add_node(checkbox)
        frame.add_node(textbox2)
        frame.add_node(linklabel)

        winForm.add_node(picture)
        winForm.add_node(login)
        winForm.add_node(register)
        winForm.add_node(frame)

        winForm.print()


if __name__ == '__main__':
    t = TestComponent2()
    t.test()
