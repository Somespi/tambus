<center>

<img src="./assets/banner.svg" width="300">


##### Bambus Template Engine 
</center>


## Usage

To get started, follow the example below to render a template:

```python
import tambus

t = tambus.TambusEngine()

# Rendering HTML
with open("/templates/index.html") as f:
    print(t.translate(f.read(), hello="world!"))
```

Imagine the content of `/templates/index.html` is as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <h1> Hello {content} </h1>
</body>
</html>
```

The output would be:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <h1> Hello world! </h1>
</body>
</html>
```
