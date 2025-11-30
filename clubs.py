from pyscript import display, document


club1 = { 
    'name' : 'Math Club',
    'desc' : 'A club for students who excel in Mathematics and Geometry. We train students to be competition ready.',
    'time' : 'Every Monday, 2:30-4:30 PM',
    'location' : 'Room 703',
    'moderator' : 'Mr. Tamon',
    'category' : 'Academic',
} #Math Club/Club 1

club2 = {
    'name' : 'Science Club',
    'desc' : 'We train and teach students who are interested & excel in Science. We perform experiments for learning.',
    'time' : 'Every Tuesday, 2:00-4:00 PM',
    'location' : 'Chemistry Lab',
    'moderator' : 'Mr. Calpo',
    'category' : 'Academic',
} #Science Club/Club 2

club3 = {
    'name' : 'Volleyball Varsity',
    'desc' : 'A club for students passionate about volleyball and have well developed skills. We strengthen skills and build teamwork.',
    'time' : 'Every Tuesday, 3:00-5:00 PM',
    'location' : 'Court/Quadrangle',
    'moderator' : 'Mr. Gervacio',
    'category' : 'Sports'
} #VolleyBall Varsity/Club 3

def math_club(k):
    document.getElementById('club_desc').innerHTML = " "
    display(f"Name: {club1['name']}", target='club_desc')
    display(f"Description: {club1['desc']}", target='club_desc')
    display(f"Time: {club1['time']}", target='club_desc')
    display(f"Location: {club1['location']}", target='club_desc')
    display(f"Club Moderator: {club1['moderator']}", target='club_desc')
    display(f"Category: {club1['category']}", target='club_desc')

def science_club(k):
    document.getElementById('club_desc').innerHTML = " "
    display(f"Name: {club2['name']}", target='club_desc')
    display(f"Description: {club2['desc']}", target='club_desc')
    display(f"Time: {club2['time']}", target='club_desc')
    display(f"Location: {club2['location']}", target='club_desc')
    display(f"Club Moderator: {club2['moderator']}", target='club_desc')
    display(f"Category: {club2['category']}", target='club_desc')
    
def varsity(k):
    document.getElementById('club_desc').innerHTML = " "
    display(f"Name: {club3['name']}", target='club_desc')
    display(f"Description: {club3['desc']}", target='club_desc')
    display(f"Time: {club3['time']}", target='club_desc')
    display(f"Location: {club3['location']}", target='club_desc')
    display(f"Club Moderator: {club3['moderator']}", target='club_desc')
    display(f"Category: {club3['category']}", target='club_desc')

    
