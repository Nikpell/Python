import model
import view
import logger


def start():
        equation_string = ''
        string = ''
        summa = ''
        common_string = ''
        while string.count('=') < 1:
            string = view.input_number()
            equation_string += string
            common_string += string
            equation_string = model.change_string(equation_string)
            view.print_result(equation_string.replace('=', ''))
        summa = model.summa(equation_string)
        logger.log(f'{common_string}{summa}')
        view.print_result(f'{common_string}{summa}')

