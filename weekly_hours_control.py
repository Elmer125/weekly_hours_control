"""
Elmer Mauricio Marulanda Osorio
Group: 213022_295
Program: Systems Engineering
Source code: own authorship


A team manager needs to control the weekly working hours of a four-person work team.
The information is recorded in a matrix with the following structure:
[Resource Name, Monday, Tuesday, Wednesday, Thursday, Friday].
Develop a Python program that calculates the total weekly hours for each resource and
classifies the workday as "Overtime" if the total exceeds 40 hours, or as
"Standard Schedule" if it does not exceed that threshold. The program must use a
modular approach (functions) and present a clear final report.

"""

WEEKLY_HOURS = [
  ["Ana López",    8,  9,  8,  9, 10],
  ["Carlos Ruiz",  8,  8,  8,  8,  8],
  ["María Gómez",  6,  7,  8,  7,  6],
  ["Jorge Díaz",  10, 10,  9, 10,  8]
]

HOURS_THRESHOLD = 40

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def calculate_total_hours(resource_row):
  """Calculates the total weekly hours of a single resource.

  Receives a row from the matrix in the format
  [name, monday, tuesday, wednesday, thursday, friday] and returns
  the numeric sum of the five day values.
  """

  total = 0
  for day_hours in resource_row[1:6]:
    total = total + day_hours
  return total

def classify_workday(total_hours, threshold):
  """Classifies the workday as "Overtime" or "Standard Schedule".

  Returns "Overtime" if total_hours is strictly greater than the threshold,
  otherwise returns "Standard Schedule".
  """
  if total_hours > threshold:
    return "Overtime"
  else:
    return "Standard Schedule"

def process_resource(resource_row, threshold):
  """Processes a single resource: calculates its total and classifies it.

  Returns a tuple (name, total_hours, classification) so the caller
  can use the values without printing inside this function.
  """
  name = resource_row[0]
  total = calculate_total_hours(resource_row)
  classification = classify_workday(total, threshold)
  return (name, total, classification)

def generate_report(matrix, threshold):
  """Iterates through the matrix and prints a formatted weekly hours report."""
  print("=" * 60)
  print("           WEEKLY WORKING HOURS REPORT")
  print("=" * 60)
  print(f"{'Resource':<20}{'Total Hours':<15}{'Classification':<20}")
  print("-" * 60)

  for resource in matrix:
    name, total, status = process_resource(resource, threshold)
    print(f"{name:<20}{total:<15}{status:<20}")

  print("=" * 60)
  print(f"Standard hours threshold: {threshold} hours per week")
  print("=" * 60)



generate_report(WEEKLY_HOURS, HOURS_THRESHOLD)