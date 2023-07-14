# tuple unpacked
def employee_work_hours_check(work_hours):
    hard_work_employee = ''
    max_work_hours = 0

    for employee, work_hour in work_hours:
        if work_hour > max_work_hours:
            max_work_hours = work_hour
            hard_work_employee = employee

    return (hard_work_employee, max_work_hours)


print(employee_work_hours_check([('Abby', 60), ('Billy', 20), ('Mike', 145)]))