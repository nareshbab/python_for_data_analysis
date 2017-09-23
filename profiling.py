import pandas as pd
import pandas_profiling

def main():
    df = pd.read_csv("FL_insurance_sample.csv")
    print df.head(10)

    profile = pandas_profiling.ProfileReport(df)
    profile.to_file("myoutputfile.html")

if __name__ == "__main__":
    main()
