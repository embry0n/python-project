# напиши здесь свое приложение
# main.py - ЗАГОТОВКА для учеников
# Образец (готовый экран): PulseScr. Смотри на него и пиши остальные по аналогии.
# Места, где нужно писать код, помечены: # TODO

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test

# Глобальные переменные: экраны записывают сюда данные пользователя
age = 7
name = ""
p1, p2, p3 = 0, 0, 0


# =====================================================
# ОБРАЗЕЦ. Экран первого замера пульса. Разбери построчно!
# =====================================================
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 1. Текст-инструкция сверху
        instr = Label(text=txt_test1)

        # 2. Строка "подпись + поле ввода"
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)  # self. - чтобы достать в next()
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        # 3. Кнопка. on_press = что выполнить при нажатии
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        # 4. Складываем всё в вертикальную колонку и добавляем на экран
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p1                          # говорим: меняем глобальную переменную
        p1 = int(self.in_result.text)      # текст из поля -> число
        self.manager.current = 'sits'      # переходим на экран с именем 'sits'


# =====================================================
# ЗАДАНИЕ 1. Экран имени и возраста
# Что должно быть: инструкция txt_instruction, два поля (имя и возраст),
# кнопка "Начать".
# Подсказка: как PulseScr, только полей ДВА (line1 и line2).
# В next(): сохрани name и age, перейди на экран 'pulse1'.
# =====================================================
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: создай Label с txt_instruction
        InstLabel = Label(text = txt_instruction)
        # TODO: создай две строки BoxLayout (имя и возраст) с TextInput
        Podpis = BoxLayout(orientation='vertical', padding=15, spacing=15)
        TextInp = BoxLayout(orientation='vertical', padding=5, spacing=5)
        TextInp.add_widget(InstLabel)
        # TODO: создай кнопку 'Начать' и привяжи к self.next
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        # TODO: собери всё в outer и сделай self.add_widget(outer)
        outer = BoxLayout(orientation='vertical', padding=12, spacing=12)
        outer.add_widget(self.btn)
        outer.add_widget(Podpis)
        outer.add_widget(TextInp)
        pass

    def next(self):
        # TODO: global name, age
        # TODO: name = текст из поля имени
        # TODO: age = число из поля возраста
        # TODO: перейти на экран 'pulse1'
        pass


# =====================================================
# ЗАДАНИЕ 2. Экран с приседаниями
# Что должно быть: текст txt_sits и кнопка 'Продолжить'. Полей ввода нет!
# Подсказка: это PulseScr без строки с полем.
# =====================================================
class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: Label с txt_sits
        Label_txt = Label(text = txt_sits, color = 'red')
        # TODO: кнопка 'Продолжить'
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2),
                          pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        # TODO: собрать в outer и добавить на экрн
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(Label_txt)
        outer.add_widget(self.btn)
        pass

    def next(self):
        # TODO: перейти на экран 'pulse2'
        pass


# =====================================================
# ЗАДАНИЕ 3. Экран второго и третьего замеров
# Что должно быть: txt_test3, ДВА поля (результат и результат после отдыха),
# кнопка 'Завершить'.
# В next(): запиши p2 и p3 (global p2, p3), перейди на 'result'.
# =====================================================
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: по образцу PulseScr, но два поля: self.in_result1 и self.in_result2
        pass

    def next(self):
        # TODO: global p2, p3
        # TODO: p2 = int(...), p3 = int(...)
        # TODO: перейти на экран 'result'
        self.manager.current = 'pulse2'
        pass


# =====================================================
# ЗАДАНИЕ 4. Экран результата
# Что должно быть: одна Label, в которую при открытии экрана
# попадает текст: имя + результат функции test(...)
# Подсказка: метод on_enter вызывается сам, когда экран открывается.
# =====================================================
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO: создай self.instr = Label(text='')
        # TODO: добавь её в BoxLayout и на экран
        pass

    def on_enter(self):
        # TODO: self.instr.text = name + '\n' + test(p1, p2, p3, age)
        pass


# =====================================================
# ЗАДАНИЕ 5. Приложение: соедини все экраны
# Подсказка: add_widget(КлассЭкрана(name='имя_экрана'))
# Имена экранов: 'instr', 'pulse1', 'sits', 'pulse2', 'result'
# =====================================================
class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        # TODO: добавь все 5 экранов в sm
        return sm


app = HeartCheck()
app.run()