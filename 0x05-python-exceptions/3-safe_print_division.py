#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        return None
    finally:
        print("Inside result: {}".format(result)
              if 'result' in locals() else "Inside result: None")
        return result
