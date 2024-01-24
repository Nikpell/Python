"""
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции,
которые могут верно работать за пределами модуля.
"""
import date
import guess
import riddle

__all__ = [guess.guess_fun,
           riddle.ask_riddle_dict,
           riddle.print_dict_riddle,
           riddle.answer_to_dict,
           riddle.answer,
           date.truly_date]
