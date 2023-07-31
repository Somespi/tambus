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

## overflow Control

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


## Contribution Guidelines
Contributions to Tambus are welcome! If you have any bug fixes, improvements, or new features to add, please submit a pull request. Make sure to follow the coding style and include tests for any new functionality.
            
## License
Tambus is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
            
