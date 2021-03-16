import pandas as pd

def main():
    """
    Print table example
    """
    d = {"key1": 1.5,
         "key2": -1.9}
    
    df = pd.DataFrame(data={"keys": d.keys(), 
                            "values": d.values()})
    
    print(df)
