from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class RuleOfTree(App):
    def build(self):
        # front-end
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (0.5, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # back-end
        # add widgets to window

        # Text input widget 1
        self.base = TextInput(
                         multiline=False,
                         padding_y=(70, 70),
                         padding_x=70,
                         size_hint=(0.5, 0.6)
                         )
        self.window.add_widget(self.base)

        # Text input widget 2
        self.new_value = TextInput(
                         multiline=False,
                         padding_y=(70, 70),
                         padding_x=70,
                         size_hint=(0.5, 0.6)
                         )
        self.window.add_widget(self.new_value)

        # Text input widget 3
        self.base_result = TextInput(
                         multiline=False,
                         padding_y=(70, 70),
                         padding_x=70,
                         size_hint=(0.5, 0.6)
                         )
        self.window.add_widget(self.base_result)

        self.space1 = Label(
                    text=" ",
                    size_hint=(0.5, 0.6)
                    )
        self.window.add_widget(self.space1)

        # Button
        self.button = Button(
                      text="CONVERT",
                      size_hint=(0.25, 0.25),
                      bold=True,
                      background_color='#00FCE'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def rule_of_tree(self, base, base_result, new_value):
        x = base_result * new_value
        new_result = x / base
        new_result = '{:.2f}'.format(new_result)
        return new_result

    def to_float(self, string):
        if string == "":
            string = 1
        else:
            string = float(string)
        return string

    def callback(self, instance):
        base = self.to_float(self.base.text)
        base_result = self.to_float(self.base_result.text)
        new_value = self.to_float(self.new_value.text)
        new_result = self.rule_of_tree(base, base_result, new_value)
        self.space1.text = new_result


if __name__ == "__main__":
    RuleOfTree().run()
