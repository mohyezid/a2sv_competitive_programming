if __name__ == '__main__':
    n = int(raw_input())
    summ=0
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input() 
     
    for i in student_marks[query_name]:
        summ=summ+i
        
    ave=summ/3
    print("%.2f" % ave)
