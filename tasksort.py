def separate_tasks_alphabetically(tasks):
    tasks.sort() 
    separated_tasks = {}

    for task in tasks:
        first_letter = task[0].upper()
        if first_letter not in separated_tasks:
            separated_tasks[first_letter] = [task]
        else:
            separated_tasks[first_letter].append(task)

    return separated_tasks
