talaba = {
    "ism": "Ali",
    "yosh": 20,
    "fanlar": ["Matematika", "Dasturlash"]
}
ustoz = {'fizika':'N.Asadov',
         'matematika':'Doston',
         'Dasturlash':'Sunnat'}
lugat = talaba | ustoz


print (sorted(lugat.items()))