if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()    

    #get score's list by query name
    query_score_list = list(student_marks[query_name])

    average=(sum(query_score_list)/len(query_score_list)) # find average student score

    # print average correct to two decimal places    
    print("{0:.2f}".format(average))