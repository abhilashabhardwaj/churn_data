import numpy as np
import pandas as pd


class fifa:
    """
    https://regenerativetoday.com/30-very-useful-pandas-functions-for-everyday-data-analysis-tasks/
    """
    def __init__(self, filename):
        self.df_fifa = pd.read_csv(filename, sep=',')

    def func1_basics(self):
        print(self.df_fifa.columns) # columns list
        print(len(self.df_fifa.columns)) # num columns
        print(self.df_fifa.describe()) # describe the dataframe
        print(self.df_fifa.aggregate) # The aggregation operations are
        # always performed over an axis, either the
        # index (default) or the column axis.
        print(self.df_fifa.abs()) # abs function is applied over values
        # that are numeric only. so if a negative number is there,
        # it will return its absolute value.

    def func2_columns(self):
        print(self.df_fifa.columns)

    def func3_drop(self):
        column_power_jumping = self.df_fifa['power_jumping']
        column_preferred_foot = self.df_fifa['preferred_foot']
        # print(column_power_jumping)
        print(column_preferred_foot.isna().count())
        print(column_preferred_foot.notna().count())
        # isna() gives False where there are values
        # notna() gives True where there are values
        # so, the count is always same.

        # columns before dropping
        print("columns before dropping: ", len(self.df_fifa.columns))
        # drop unwanted columns
        self.df_fifa = self.df_fifa.drop(columns=['Unnamed: 0', 'weak_foot', 'real_face'])
        # columns after dropping
        # 3 columns got dropped
        print("columns after dropping, 3 columns got dropped: ", len(self.df_fifa.columns))

    def func4_len(self):
        print("length of the dataframe: ", len(self.df_fifa))

    def func5_query(self):
        """
        #TODO should work more on query function
        https://sparkbyexamples.com/pandas/pandas-dataframe-query-examples/
        You can filter or query using a boolean expression.
        I will use ‘shooting’ and ‘passing’ columns for this example.
        Here I am checking for which rows ‘shooting’ is bigger than ‘passing’.
        :return:
        """
        # print(self.df_fifa['shooting'])
        # print(self.df_fifa['passing'])
        # print("There are %d shooting values that are more than passing." % len(self.df_fifa.query('shooting > passing')))
        # alternate

        # print("abhilasha query: ", len(self.df_fifa.query('shooting > passing')))

        # query to find height and weight
        height_col = self.df_fifa['height_cm']
        print("height col:", height_col, height_col.aggregate)
        print("query to find height greater than 180 cms", self.df_fifa.query('height_cm > 190')['height_cm'])


if __name__ == "__main__":
    ip_file = '/home/meetu/PycharmProjects/pythonProject/churn_data/churn_data/fifa.csv'
    call_fifa = fifa(ip_file)
    # call_fifa.func1_basics()
    # call_fifa.func2_columns()
    # call_fifa.func3_drop()
    # call_fifa.func4_len()
    call_fifa.func5_query()



