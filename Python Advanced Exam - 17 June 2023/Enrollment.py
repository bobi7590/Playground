def gather_credits(needed_credits,*args):

    courses = []
    acumulated_credits = 0
    for name,giving_credits in args:
        if acumulated_credits > needed_credits:
            break
        if name in courses:
            continue
        courses.append(name)
        acumulated_credits += giving_credits
    if acumulated_credits >= needed_credits:
        return f"""Enrollment finished! Maximum credits: {acumulated_credits}.\nCourses: {', '.join(sorted(courses))}"""
    return f"You need to enroll in more courses! You have to gather {needed_credits - acumulated_credits} credits more."




print(gather_credits(
    60,
    ("Basics", 27),
    ('Application',1),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30),

))


