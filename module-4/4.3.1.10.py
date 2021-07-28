def liters_100km_to_miles_gallon(liters):
# Write your code here.
  mile = 100 * 1000 / 1609.344
  gallon = liters / 3.785411784
  return mile / gallon

def miles_gallon_to_liters_100km(miles):
# Write your code here
  km = miles * 1609.344 / 1000
  return 100 / km * 3.785411784

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
