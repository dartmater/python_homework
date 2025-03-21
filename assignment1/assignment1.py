#Task1
def hello():
    return "Hello!"
print(hello())

#Task2
def greet(name):
    return f"Hello, {name}!"
print(greet("Elle"))

#Task3

def calc(x, y, z="multiply"):
    try:  # Properly indented
        match z:
            case "add":
                return x + y
            case "subtract":
                return x - y
            case "multiply":
                return x * y
            case "divide":
                if y == 0:
                    return "You can't divide by 0!"
                return x / y
            case "modulo":
                if y == 0:
                    return "You can't divide by 0!"
                return x % y
            case "int_divide":
                if y == 0:
                    return "You can't divide by 0!"
                return x // y
            case "power":
                return x ** y
            case _:
                return f"Unsupported operation: {z}"
    except TypeError:
        return f"You can't {z} those values!"

print(calc(5, 3, "add"))
print(calc(5, 3, "subtract"))
print(calc(5, 3, "multiply"))

#Task4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Unsupported data type: {data_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion(5, "int"))      
print(data_type_conversion(5, "float"))    
print(data_type_conversion("banana", "int")) 
print(data_type_conversion("nonsense", "float")) 

#Task5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    
    print (grade(90, 80, 71, 65, 40))
    print(grade(90, 80, 71, 65, 40, 100))

#Task6
def repeat(string,count):
    result=""
    for i in range(count):
        result+=string
    return result
print(repeat("hello ", 3))

#Task7
def student_scores(operation, **kwargs):
    try:
        if not kwargs:
            return "No student scores provided."
        if operation == "best":
            best_value=0
            for key, value in kwargs.items():
                if value > best_value:
                    best_value = value
                    best_student = key
            return best_student
        elif operation == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid operation. Use 'best' or 'mean'."

    except Exception as e:
        return f"An error occurred: {e}"
 #Task8
def titleize(string):

    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = string.split()
    for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
             words[i] = word.capitalize()
            else:
                words[i] = word.lower()  
    return " ".join(words)

print(titleize("war and peace"))

#Task9
def hangman(secret,guess):
    result=""
    for letter in secret:
        if letter in guess:
            result+=letter
        else:
            result+="_"
    return result
print(hangman("alphabet", "ab"))

#Task10

def pig_latin(string):
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in string.split():
        if word[0] in vowels:
            result.append(word + "ay")
        else:
         if word.startswith("qu"):
            result.append(word[2:] + "quay")
         else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)
print(pig_latin("hello world"))
