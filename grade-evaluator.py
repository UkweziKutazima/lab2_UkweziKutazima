import csv
import sys
import os




def load_csv_data():
    try:
        filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    except EOFError:
        print("\nError: Input interrupted. Exiting.")
        sys.exit(1)
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row_num, row in enumerate(reader, start=2):
                try:
                    assignment_name = row['assignment'].strip()
                    group = row['group'].strip()
                    
                    if not assignment_name:
                        print(f"Error on line {row_num}: Assignment name is empty.")
                        sys.exit(1)
                        
                    score = float(row['score'])
                    weight = float(row['weight'])
                    
                    if score != score or weight != weight:
                        print(f"Error on line {row_num}: Score or weight is 'nan'.")
                        sys.exit(1)
                        
                    assignments.append({
                        'assignment': assignment_name,
                        'group': group,
                        'score': score,
                        'weight': weight
                    })
                except (KeyError, ValueError, TypeError):
                    print(f"Error on line {row_num}: Missing fields or invalid data format. Please check your CSV.")
                    sys.exit(1)
                    
        if not assignments:
            print("Error: The CSV file is empty or contains no valid data.")
            sys.exit(1)
            
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)




def evaluate_grades(data):
    print("\n--- Processing Grades ---")
    
    total_weight = 0
    formative_weight = 0
    summative_weight = 0
    
    formative_score_total = 0
    summative_score_total = 0
    
    failed_formatives = []


    for item in data:
        if item['weight'] <= 0:
            print(f"Error: Weight for '{item['assignment']}' must be greater than 0. Got {item['weight']}.")
            sys.exit(1)


        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: Score for '{item['assignment']}' is {item['score']}. Must be between 0 and 100.")
            return


    for item in data:
        total_weight += item['weight']
        if item['group'] == 'Formative':
            formative_weight += item['weight']
        elif item['group'] == 'Summative':
            summative_weight += item['weight']
            
    if round(total_weight, 2) != 100 or round(formative_weight, 2) != 60 or round(summative_weight, 2) != 40:
        print("Weight Validation Error:")
        print(f" - Total Weight: {total_weight} (Expected: 100)")
        print(f" - Formative Weight: {formative_weight} (Expected: 60)")
        print(f" - Summative Weight: {summative_weight} (Expected: 40)")
        return


    for item in data:
        weighted_score = (item['score'] / 100) * item['weight']
        
        if item['group'] == 'Formative':
            formative_score_total += weighted_score
            if item['score'] < 50:
                failed_formatives.append({'name': item['assignment'], 'weight': item['weight']})
        elif item['group'] == 'Summative':
            summative_score_total += weighted_score


    total_grade = formative_score_total + summative_score_total
    gpa = (total_grade / 100) * 5.0


    percentage_formative = (formative_score_total / formative_weight) * 100
    percentage_summative = (summative_score_total / summative_weight) * 100


    print(f"\nTotal Grade: {total_grade:.2f} / 100")
    print(f"GPA: {gpa:.2f} / 5.0")


    if percentage_formative >= 50 and percentage_summative >= 50:
        print("Final Status: PASSED")
    else:
        print("Final Status: FAILED")
        
        if failed_formatives:
            max_failed_weight = max(item['weight'] for item in failed_formatives)
            resubmissions = [item['name'] for item in failed_formatives if item['weight'] == max_failed_weight]
            
            print("\nResubmission Options (Highest weight failed formatives):")
            for r in resubmissions:
                print(f" - {r}")




if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
