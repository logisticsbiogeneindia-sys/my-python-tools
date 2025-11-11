def run(num):
    try:
        num = int(num)
        return num ** 2
    except:
        return "Invalid number"
