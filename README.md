<center>

<img src="./assets/banner.svg" width="300">


##### Bambus Template Engine 
</center>



## Usage 

```py

import tambus

t = tambus.TambusEngine()

# rendering HTML
with open("/templates/index.html") as f:
    print(t.translate(f.read(), hello="world!"))


```

And if we assume that the content of `/templates/index.html` is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>MyPage</title>
</head>
<body>
    <h1> Hello {hello} </h1>
</body>
</html>
```

The output would be:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>MyPage</title>
</head>
<body>
    <h1> Hello world! </h1>
</body>
</html>
```
