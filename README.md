<center>

<img src="./assets/banner.svg" width="300">


##### very basic Template Engine 
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
    <h1> Hello {hello} </h1>
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

## Other features

you can use if statement in tambus using this syntax:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <h1>The Answer:
    {#if is_true}
        <bold>True</bold>
    {/if}
    </h1>
</body>
</html>
```

You can also repeat some part of the code using `{#repeat}`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <h1>The Answer:
    {#repeat 5}
        {car}
    {/repeat}
    </h1>
</body>
</html>
```
## Markdown 
tambus offers a great way for customizable MD2HTML. 

```python
from tambus import MDEngine, Component

component = [Component(r"# (.*?)",r"<h1 class='my-custom-h1'>\1</h1>")] 

with open("file.md") as f:
    mdcontent = MDEngine(component).translate(f.read())
```


## Contribution Guidelines
Contributions to Tambus are welcome! If you have any bug fixes, improvements, or new features to add, please submit a pull request. Make sure to follow the coding style and include tests for any new functionality.
            
## License
Tambus is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
            
