from typing import List

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    cycles = {}
    
    def has_cycle(course, visited):
        if course in cycles:
            return cycles[course]

        if course not in courses:
            cycles[course] = False
            return cycles[course]

        if course in visited:
            cycles[course] = True
            return cycles[course]
        visited.add(course)
        
        for prereq in courses[course]:
            next_visited = visited.copy()
            if has_cycle(prereq, next_visited):
                cycles[course] = True
                return cycles[course]
        cycles[course] = False
        return cycles[course]

    if len(prerequisites) <= 1:
        return True

    courses = {}
    for course, prereq in prerequisites:
        if course in courses:
            courses[course].append(prereq)
        else:
            courses[course] = [prereq]
    
    for course in courses:
        if has_cycle(course, set()):
            return False
    return True

        