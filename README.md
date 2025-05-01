# ScalableFizzBuzz

A Python implementation of the classic FizzBuzz coding challenge inspired by Tom Scott's video on [FizzBuzz](https://www.youtube.com/watch?v=QPZ0pIK_wsc). This simple yet insightful coding exercise demonstrates scalability and flexibility in software design, making it useful for both learning and interview preparation.

## Overview

FizzBuzz is a classic programming task frequently used in coding interviews. It involves iterating through numbers and printing:
- "Fizz" for multiples of 3
- "Buzz" for multiples of 5
- "FizzBuzz" for multiples of both 3 and 5

This implementation expands the original concept, allowing easy scalability to accommodate additional rules.

## Features

- Customizable ruleset through a Python dictionary.
- Easy scalability for adding new divisors and outputs.
- Ideal for understanding basic programming constructs.

## Usage

Clone the repository or download the main file directly:

```bash
git clone https://github.com/WhanTick/ScalableFizzBuzz.git
cd ScalableFizzBuzz
```

Run the program using Python:

```bash
python main.py
```

## Customization

You can easily modify or add new rules by adjusting the `rule_dictionary`:

```python
rule_dictionary = {
    3: "Fizz",
    5: "Buzz",
    7: "Bazz"  # Example of adding an additional rule
}
```

Adjust the range by changing the `maxNumber` parameter:

```python
fizz_buzz(rule_dictionary, 100)
```

## Educational Value

- Enhances understanding of loops and conditionals.
- Demonstrates basic algorithm optimization and flexibility.
- Serves as a useful preparation exercise for coding interviews.

## Inspiration

Inspired by Tom Scott's exploration of the FizzBuzz problem:
- [Tom Scott - FizzBuzz](https://www.youtube.com/watch?v=QPZ0pIK_wsc)

## License

This project is licensed under the MIT License.

---

Enjoy exploring and learning from ScalableFizzBuzz! 🚀💻

