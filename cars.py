showroom = set()
showroom.add("Bronco")
showroom.add("Pilot")
showroom.add("Jeep")
showroom.add("Car")

print(len(showroom))

showroom.add("Bronco")

print(showroom)

showroom.update({"Truck", "Motorcycle"})
print(showroom)

showroom.discard("Car")

print(showroom)

junkyard = set()
junkyard.add("Pinto")
junkyard.add("El Camino")
junkyard.add("Prius")
junkyard.add("Bronco")
junkyard.add("Jeep")

print(junkyard)

print(showroom.intersection(junkyard))
print(showroom.union(junkyard))

new_showroom = showroom.union(junkyard)
new_showroom.discard("Pinto")
print(new_showroom)