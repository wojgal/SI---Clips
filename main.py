import clips
from tkinter import *

#Properties
properties = {}

def setup_properties():
    file = open('full_descriptions.txt', 'r')

    data = file.readlines()

    for line in data:
        name, full_name = line.replace('\n', '').split('=')
        properties[name] = full_name

    file.close()

setup_properties()

def get_properties(name):
    return properties[name]


clips_env = clips.Environment()
clips_env.load('movieortv.clp')
clips_env.reset()
clips_env._agenda.run()

def get_current_id():
    eval_str = '(find-all-facts ((?f state-list)) TRUE)'
    curr_id = str(clips_env.eval(eval_str)[0]['current'])

    return curr_id

def get_curret_UIstate():
    curr_id = get_current_id()
    eval_str = '(find-all-facts ((?f UI-state)) ' + '(eq ?f:id ' + curr_id + '))'
    UIstate = clips_env.eval(eval_str)[0]

    return UIstate

def get_display():
    UIstate = get_curret_UIstate()
    display = str(UIstate['display'])

    return get_properties(display)

def get_valid_answer(id):
    UIstate = get_curret_UIstate()
    valid_answers = UIstate['valid-answers']

    if len(valid_answers) <= id:
        return ''

    return valid_answers[0]

def ans_button_state(id):
    valid_answer = get_valid_answer(id)

    if valid_answer == '':
        return DISABLED

    return NORMAL

def get_back_button():
    UIstate = get_curret_UIstate()
    state = str(UIstate['state'])

    if state == 'final':
        return 'Restart'

    if state == 'initial':
        return ''

    return 'Back'

def ans_button_command(id):
    curr_id = get_current_id()

    clips_env._facts.assert_string('(next ' + curr_id + ' ' + get_valid_answer(id) + ')')

def back_button_command():
    pass


#TKINTER
root = Tk()

root.title('Cant decide what to watch')

question = Label(root, text=get_display())

button_ans1 = Button(root, text=get_valid_answer(0), padx=100, pady=10, command=lambda: ans_button_command(0), state=ans_button_state(0))
button_ans2 = Button(root, text=get_valid_answer(1), padx=100, pady=10, command=lambda: ans_button_command(1), state=ans_button_state(1))
button_ans3 = Button(root, text=get_valid_answer(2), padx=100, pady=10, command=lambda: ans_button_command(2), state=ans_button_state(2))
button_ans4 = Button(root, text=get_valid_answer(3), padx=100, pady=10, command=lambda: ans_button_command(3), state=ans_button_state(3))
button_ans5 = Button(root, text=get_valid_answer(4), padx=100, pady=10, command=lambda: ans_button_command(4), state=ans_button_state(4))
button_ans6 = Button(root, text=get_valid_answer(5), padx=100, pady=10, command=lambda: ans_button_command(5), state=ans_button_state(5))
button_ans7 = Button(root, text=get_valid_answer(6), padx=100, pady=10, command=lambda: ans_button_command(6), state=ans_button_state(6))
button_back = Button(root, text=get_back_button(), padx=100, pady=10)

question.grid(row=0, column=3)

button_ans1.grid(row=1, column=0)
button_ans2.grid(row=1, column=1)
button_ans3.grid(row=1, column=2)
button_ans4.grid(row=1, column=3)
button_ans5.grid(row=1, column=4)
button_ans6.grid(row=1, column=5)
button_ans7.grid(row=1, column=6)
button_back.grid(row=2, column=3)










root.mainloop()
