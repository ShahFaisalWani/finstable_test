degree_input = [0, 28, 60, 180, 202]

for degree in degree_input:
  minute_per_degree = 12 * 60 / 360

  minutes = degree * minute_per_degree

  hour = int(minutes / 60)
  minute = int(minutes % 60)

  print(f"{degree} => {hour:02}:{minute:02}")
