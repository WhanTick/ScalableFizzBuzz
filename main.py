
rule_dictionary = {
    3: "Fizz",
    5: "Buzz",
}

def fizz_buzz(rules, maxNumber):
    for num in range(1, maxNumber +1):
        
        output = ""
        
        for divisor, word in rules.items():
            if num % divisor == 0:
                output += word
                
        if not output: output = num
            
        print(output)
        
if __name__ == '__main__':
    fizz_buzz(rule_dictionary, 100)