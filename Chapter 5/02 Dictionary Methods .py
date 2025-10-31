marks = {
     "Samarth": 100, 
      "Madhav": 99,
      "Shiva" : 80,
      0: "God"
  }

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"Samarth":98})
print(marks)

print(marks.get("Samarth")) 