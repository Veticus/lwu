# Argparse basics
Start by importing `argparse` and creating an `ArgumentParser` object in the `__main__`.

```python
import argparse

parser = argparse.ArgumentParser()
```

The ArgumentParser constructor takes these parameters:

| Parameter             | Description                                                                                                            |
|-----------------------|------------------------------------------------------------------------------------------------------------------------|
| prog                  | Name of the program<br/>default: `os.path.basename(sys.argv[0])`                                                       |                                                                    |
| usage                 | String describing the usage<br/>default: generatedfrom arguments added to the parser                                   |
| description           | Text to show before the argument help<br/>default: nothing                                                             |
| epilog                | Text to show after the argument help<br/>default: nothing                                                              |
| parents               | List of other `ArgumentParser` objects to include                                                                      |
| formatter_class       | A class for customzing the help output<br/>(see docs)[https://docs.python.org/3/library/argparse.html#formatter-class] |
| prefix_chars          | Set of characters to prefix the optional arguments<br/>default: "-"                                                    |
| fromfile_prefix_chars | (see docs)[https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars]                                      |
| argument_Default      | The default value for each argument<br/>default: none                                                                  |
| conflict_handler      | How to resolve conflicting optionals<br/>(see docs)[https://docs.python.org/3/library/argparse.html#conflict-handler]  |
| add_help              | Boolean, wheter or not the -h/--help option is added<br/>default: `True`                                               |
| allow_abbrev          | If `True` allows options to be abbreviated, if the abbreviation is unambiguous<br/>Default: `True`                     |
| exit_on_error         | If `True` will make `ArgumentParser` exit with error info, when an error occurs<br/>Default: `True`                    |






# Defining and using arguments
Arguments are defined using the `add_argument()` method in the `ArgumentParser` object.
It's most basic usage is like this:
```python
parser.add_argument('-f')
```
or 
```python
parser.add_argument('-f', '--f00')
```

`add_argument()` takes these parameters:

| Parameter     | Description                                                                                                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name or flags | The name or a list of option strings for this argument<br/>example: `foo`, `-f` or `--foo`                                                                               |
| action        | The "basic type of action" to happen, which this argument is used                                                                                                        |
| nargs         | The number of arguments to expect from this flag<br/>use `nargs="+" when dealing with an unknown number of arguments for this flag. also applies to positional arguments |
| const         | A constant value required by some `action` and `nargs` selections.<br/>(see docs)[https://docs.python.org/3/library/argparse.html#const]                                 |
| default       | The default value for this flag                                                                                                                                          |
| type          | The data type to which this argument should be converted                                                                                                                 |
| choices       | A sequence of permittable values for this flag                                                                                                                           |
| required      | For optionals: wheter or not this flag must be "used"<br/>Bad design warning: users expect optionals to be OPTIONAL - not required                                       |
| help          | Text describing what this argument does                                                                                                                                  |
| metavar       | Name for this argument in usage messages<br/>Overrides the default help text that is just the name of the argument                                                       |
| dest          | Name of the attribute to be added to the object returned by `parse_args()`                                                                                               |



## About "name or flags"
The name or flag of the argument is the "name" with which it's returned by `parse_args()`.
So when doing `args = parser.parse_args()`, `args` will be a list holding the arguments.
Meaning, if there is an argument or flag called `cow`, it will be acceesible as `args.cow` after parsing.

By default the name will be shown in the help text as well. This can be overridden, by using the `metavar` parameter, when calling `add_argument()`.





## Positional arguments
Positional arguments don't need a dash or double dash in front of them.

They'll either be added individually named to `args` after parsing with `args = parser.parse_args()` - OR as a list of strings. See below for clarification.



### Specific number of positional arguments
Here's an example of how to define and use a specific number of positional arguments:

```python
import argparse


def main():
	parser = argparse.ArgumentParser(description="Some words")
	parser.add_argument("word1", help="This is the first word")
	parser.add_argument("word2", help="This is the second word")
	args = parser.parse_args()
	# Or words = [getattr(args, f'word{i}') for i in range(1, 4)] to be fancy
	print([args.word1, args.word2])


if __name__ == "__main__":
	main()
```

This can be called like `python3 thatfile.py firstword secondword` and will print `['firstword', 'secondword']` to the console.





### Unknown number of positional arguments
nargs="+" one or more
nargs="*" zero or more

When dealing with an unknown number of positional arguments, it's easiest to use `nargs="+"` or `nargs="*"` as arguments when calling `add_arguments()`.
`nargs="+"` will allow ONE or more positional arguments, while `nargs="*"` will allow ZERO or more.

Here's an example:

```python
import argparse


def main():
	parser = argparse.ArgumentParser(description='some words')
	parser.add_argument('words', nargs='+', help='one or more words')
	args = parser.parse_args()

	if args.words:
		for word in args.words:
			print(word)


if __name__ == "__main__":
	main()
```

This can be called like `python3 thatfile.py firstword secondword` and will print `firstword` and `secondword` on their own lines.




## Optional arguments
Optional arguments are added in a similar manner, as the positional arguments.
There are however some small conveniences built in.

### The `action` argument
The default action is just to store the arguments value.
But some simple tasks can be achieved using the `action` parameter.
This can result in a bit more readable and simple code.
They're described in (the docs)[https://docs.python.org/3/library/argparse.html#action]  but here are some examples:

#### The `version` action

Here's an example, for an optional argument that can be used as `-v` or `--version`, and will print out the name or the program and a number:
```python
import argparse


def main():
    parser = argparse.ArgumentParser(description='Only shows version')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.3-beta')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
```
This can be called like `python3 thatfile.py -v` and will print `thatfile.py version 0.1.3-beta`
`%(prog)s` is a format specifier that gets the program name from `sys.argv[0]`.

#### The `sture_true` and `store_false` actions
`action="store_true"` and will store the value of the argument with `True` of the argument is present. If not present it will be `False` by default.
`action="store_false"` does the opposite.


#### The `count` action
```python
import argparse


def main():
	parser = argparse.ArgumentParser(description='counting verbosity levels, because raisins')
	parser.add_argument('-v', '--verbose', action='count', default=0)
	args = parser.parse_args()

	if args.verbose == 1:
		print("verbosity level 1")
	elif args.verbose == 2:
		print("verbosity level 2")
	elif args.verbose >= 3:
		print("verbosity level 3 (or more)")
	else:
		print("no verbosity level")


if __name__ == '__main__':
	main()
```
This can be called like: `python3 thatfile.py -v`, which will print `verbosity level 1`.
Calling it like: `python3 thatfile.py -vv` will print `verbosity level 2`.
Calling it like: `python3 thatfile.py -vvv` will print `verbosity level 3 (or more)`.
Calling it like: `python3 thatfile.py -vvvv` will also print `verbosity level 3 (or more)`.


#### The `help` action
`action="help"` will make the program print an autogenerated "help" text, if the flag is used. The rest of the program will not run.
It uses the `help="some text"` parameter, used when calling `add_argument()`.
It also shows the text defined in the `description="some description"` argument, for the `ArgumentParser()` constructor.


### Single- and double dash flags
Am argument prepended with a dash can take all actions.

Here's an example that also uses the `default` parameter in the `add_argument()` call.

```python
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n')
	args = parser.parse_args()

	if args.n:
		print(f"-n is {args.n}")
	else:
		print("no -n value given")


if __name__ == "__main__":
	main()
```
Calling it like `python3 thatfile.py -n 20` will print `-n is 20`, while `python3 thatfile.py` will print `no -n value given`.

If the argument were added with `parser.add_argument("-n", "--n")` it'd likewise be possible to use `-n 20` or `--n 20` as CLI arguments.



### Example: Double dash flags (as booleans)
The `action` parameter needs to be set. Usually as `action="store_true"` or `action="store_false"`.

Here's an example:
```python
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--do-thing', action="store_true")
	args = parser.parse_args()
	print("doing" if args.do_thing else "not doing")  # bonus ternary operator action


if __name__ == '__main__':
	main()
```
Calling this like `python3 thatfile.py --do-thing` will print `doing`, while `python3 thatfile.py` will print `not doing`.
In other words, `args.do_thing` will simply be `True` if the program is run with `--do-thing`.
