def getPlanetName(id: Int): String = { 
  var planeta = ""
  if id == 1 then
    planeta += "Mercury"
  else if id == 2 then
    planeta += "Venus"
  else if id == 3 then
    planeta += "Earth"
  else if id == 4 then
    planeta += "Mars"
  else if id == 5 then
    planeta += "Jupiter"
  else if id == 6 then
    planeta += "Saturn"
  else if id == 7 then
    planeta += "Uranus"
  else if id == 8 then
    planeta += "Neptune"
  return planeta
} 