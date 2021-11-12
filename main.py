#Introducing data input for cw deadline
print('Enter data for CW Deadline')
year = int(input('Input year: '))
month = int(input('Input month: '))
day = int(input('Input day: '))
hour = int(input('Input hour: '))
minutes = int(input('Input minutes: '))

cw_deadline = [hour, minutes, day, month, year]
print('Enter data for Submission date')
s_year = int(input('Input year: '))
s_month = int(input('Input month: '))
s_day = int(input('Input day: '))
s_hour = int(input('Input hour: '))
s_minutes = int(input('Input minutes: '))

submission_date = [s_hour, s_minutes, s_day, s_month, s_year]

print('Deadline: ', cw_deadline)
print('Submission: ', submission_date)

if cw_deadline < submission_date:
    #Put validation code here
else:
    print('You get full mark!')