stud = {
    "name":"badal",
    "cgpa":9.7,
    "sub":{
        "chem":90,
        "phy":80,
        "math":95,
    }
}
print(stud.update({"course":"b.tech"}))
print(stud.get("chem"))
print(stud.items())
print(stud.values())
print(stud.keys())
print(stud["sub"]["math"])
print(type(stud))