# Key Value Switch
# Description
# Build a function kvSwitch to switch the keys and values of a dictionary.

# Examples
# kvSwitch({"a": "1", "b": "2", "c": "3"}) returns {"1": "a", "2": "b", "3": “c"}

def kvSwitch(d):
    #mykey = list(d.key())
    #myvalue = list(d.value())
    my_dict = {y: x for x, y in d.items()}
    return my_dict
