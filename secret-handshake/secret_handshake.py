actions = ["wink", "double blink", "close your eyes", "jump", "reverse"]


def commands(binary_str):
    actions_index = [
        index for index, digit in enumerate(list(reversed(binary_str))) if digit == "1"
    ]
    action_list = [actions[i] for i in actions_index]
    if "reverse" in action_list:
        action_list.remove("reverse")
        action_list.reverse()
    return action_list
