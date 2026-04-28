"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    updated_scores = []
    for score in student_scores:
        updated_scores.append(round(score))
    return updated_scores
        


def count_failed_students(student_scores):
    fail_count = 0 
    for score in student_scores:
        if score < 41:
            fail_count += 1
    return fail_count

def above_threshold(student_scores, threshold):
    the_best = []
    for score in student_scores:
        if round(score) >= threshold:
            the_best.append(score) 
    return the_best


def letter_grades(highest):
    not_fail = 40
    start = 41
    increment = (highest - start) / 4
    step = (highest - not_fail) / 4
    
    thresholds = [int(start + step * i) for i in range(0, 4)]
    return thresholds

def student_ranking(student_scores, student_names):
    list_of_info = []
    for index, name in enumerate(student_names):
        list_of_info.append(f'{index + 1}. {student_names[index]}: {student_scores[index]}')
    return list_of_info


def perfect_score(student_info):
    perfection = []
    for student in student_info:
        if student[1] == 100:
            perfection.append(student)
            return perfection[0]
        else:
            continue
    return perfection
