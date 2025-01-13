this_text = "Ucime se Python"

def log_into_terminal(text_z_parametru, second_to_log):
    def fourth_function():
        print("Jsem uvnitr fourth_function")

    local_text = "Jsem uvnitr funkce"
    print(this_text)
    print(local_text)
    fourth_function()
    print(text_z_parametru)
    print(second_to_log)


def another_function():
    second = "Druhy argument z another function"
    log_into_terminal("Ahoj z another function", second)

another_function()

third_function = log_into_terminal
second = "Druhy argument z third function"
third_function("Ahoj z third function", second)



