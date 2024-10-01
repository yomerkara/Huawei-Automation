from user_input import ask_user_questions
from concat_sources import concat_sources
from filter_data import filter_excel_with_answers

def main():
    # Call the function from questionnaire.py
    answers = ask_user_questions()
    print(answers)
    
    if answers["files_loaded"] == "E":
        concat_sources()
        filter_excel_with_answers(answers)
    

if __name__ == "__main__":
    main()