import tambus 


t = tambus.TambusEngine()

# rendering HTML
with open("./templates/index.html") as f:
    print(t.translate(f.read(), hello="world!"))