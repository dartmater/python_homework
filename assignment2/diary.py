#Task1: 
import traceback

def diary():
    try:
        with open('diary.txt', 'a') as file:
            first_entry = True
            while True:
                if first_entry:
                    prompt = input("What happened today? ")
                    first_entry = False
                else:  
                    prompt = input("What else? ")

                if prompt.lower() == "done for now":
                    file.write("done for now\n")
                    print("Goodbye!")
                    break

                file.write(prompt + "\n")
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]
        print(f"An exception occurred. Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")
  if __name__ == "__main__":  

    diary()
