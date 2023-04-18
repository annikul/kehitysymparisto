import traceback

def divide(x, y):
    try:
        result = x / y
    
    #except Exception:
    #   traceback.print_exc()
    except:
        print('division by zero!')
    finally:
        print('heippa!')