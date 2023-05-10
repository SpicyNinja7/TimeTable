from datetime import datetime

def display_timetable(subjects):
    timetable = {}
    for subject, time_slot, day in subjects:
        if day not in timetable:
            timetable[day] = {}
        else:
            for t in timetable[day]:
                if time_overlap(time_slot, t):
                    print(f"Error: Time slot overlap detected between {subject} and {timetable[day][t]} on {day} {time_slot}. Unable to add subject to timetable.")
                    continue
        timetable[day][time_slot] = subject

    day_list = ["Monday","Tuesday", "Wednesday","Thursday","Friday"]
    print("Day\tTime\t\tSubject")
    for day in day_list:
        if day in timetable.keys():
            for time_slot in sorted(timetable[day].keys()):
                print(f"{day}\t{time_slot}\t{timetable[day][time_slot]}")

def time_overlap(slot1, slot2):
    start1, end1 = slot1.split('-')
    start2, end2 = slot2.split('-')
    start1 = datetime.strptime(start1, "%H:%M")
    end1 = datetime.strptime(end1, "%H:%M")
    start2 = datetime.strptime(start2, "%H:%M")
    end2 = datetime.strptime(end2, "%H:%M")
    return (start1 <= start2 < end1) or (start1 < end2 <= end1) or (start2 <= start1 < end2) or (start2 < end1 <= end2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    subjects = [("Maths", "9:00-10:00", "Monday"),
                ("Science", "10:00-11:00", "Monday"),
                ("English", "9:00-10:00", "Tuesday"),
                ("Social Studies", "11:00-12:00", "Tuesday"),
                ("Physics", "10:30-11:30", "Monday"),
                ("Chemistry", "11:00-12:00", "Monday")]
    display_timetable(subjects)

