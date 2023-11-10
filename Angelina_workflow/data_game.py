import pandas as pd
import numpy as np
import os
from functools import reduce
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


OBJECT_MAX = 50
SUFFIXES = ["x", "y", "y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"]
IQR_THRESHOLD = 10

class DataGame:
    def __init__(self):
        pass

    def summary(self, data: pd.DataFrame, object_max=OBJECT_MAX, percentiles=None, display_numeric: bool=True, 
                display_object: bool=True, save: bool=False, display_head: bool=False):
        r"""
        For object data (e.g. strings or timestamps), the result’s index will include count, unique, top, 
        and freq. The top is the most common value. The freq is the most common value’s frequency. 
        Timestamps also include the first and last items. 

        For numeric data, the result’s index will include count, mean, std, min, max as well as lower, 50 and 
        upper percentiles. By default the lower percentile is 25 and the upper percentile is 75. The 50 
        percentile is the same as the median.

        Parameters
        ----------
        data: pd.DataFrame
            The data you want to summarize.
        object_max: int, defaults to 50
            The maximum number for an numeric variable  

        """
        df = data.copy()
        s = df.nunique()
        for idx, qty in zip(s.index, s.to_numpy()):
            if qty <= object_max:
                data[idx] = df[idx].astype('object')
        if display_head:
            print("Data View:\n", data.head())
        if display_object:
            cat_summary = df.describe(include=[object])
            print("Object Summary:\n", cat_summary)
        if display_numeric:
            con_summary = data.describe(percentiles=percentiles, include=[np.number])
            print("Numeric Summary:\n", con_summary)

        if save & display_object:
            DataGame.save_data(self, cat_summary, save_name="category_summary.csv", index=True)
        if save & display_numeric:
            DataGame.save_data(self, con_summary, save_name="numeric_summary.csv", index=True)
        
        return None


    def save_data(self, data: pd.DataFrame, save_name: str=None, index=False):
        r"""
        Save data to csv file and save to a folder named "backup".

        Parameters
        ----------
        data: pd.DataFrame
            The data you wanna save
        save_name: str
            Data name, must be .csv file, for example: save_name="LDS_Func.csv"
        """
        os.makedirs("./backup/", exist_ok=True)
        data.to_csv(f"./backup/{save_name}", index=index)
        return None

    def read_col_name(self, data: pd.DataFrame, max_display=100, save=False):
        column_name = data.columns.tolist()
        print(f"The data has {len(column_name)} columns:")
        if len(column_name) > max_display:
            print(column_name[:max_display])
        else:
            print(column_name)

        if save:
            col_df = pd.Series(data=column_name, name="Column Name")
            save_name = f"{self.product}.upper() Column Name"
            DataGame.save_data(self, col_df, save_name)
        
        return None

    def read_col_value(self, data: pd.DataFrame, cols, dropna=True):
        if isinstance(cols, str):
            print(data[cols].value_counts())
        else:
            print(data.groupby(cols, dropna=dropna)[cols[-1]].count())

    def add_col(self, data: pd.DataFrame, new_colname: str, func)-> pd.DataFrame:
        data[new_colname] = data.apply(func, axis=1)
        print(f"{new_colname} freq:\n{data[new_colname].value_counts()}")
        return data

    def remove_col(self, data, cols, inplace=False, save=False, save_name=None):
        if inplace:
            data.drop(cols, axis=1, inplace=True)
            if save:
                DataGame.save_data(self, data, save_name)
        else:
            df = data.drop(cols, axis=1, inplace=False)
            if save:
                DataGame.save_data(self, df, save_name)
            return df

    def filter_data(self, data: pd.DataFrame, condition: str, inplace=False) -> pd.DataFrame:
        df = data.query(condition, inplace=inplace)
        return df

    def merge_data(self, data_list, on, how="outer", drop_samecol=False, suffixes=None, save=False, save_name=None) -> pd.DataFrame:
        if suffixes is None:
            suffixes = [f"_{SUFFIXES[i]}" for i in range(len(data_list))]

        if isinstance(on[0], str):
            if drop_samecol:
                df_merged = reduce(lambda  left, right: pd.merge(left, right, on=on, how=how, 
                            suffixes=('', '_DROP')).filter(regex='^(?!.*_DROP)'), data_list)
            else:
                df_merged = reduce(lambda  left, right: pd.merge(left, right, on=on, how=how, 
                            suffixes=suffixes), data_list)
        else:
            df_merged = pd.DataFrame()
            for idx, (df, col) in enumerate(zip(data_list, on)):
                if len(df_merged) == 0:
                    df_merged = df
                else:
                    if drop_samecol:
                        df_merged = pd.merge(df_merged, df, left_on=list(on[idx-1]), right_on=list(col), how=how, 
                                             suffixes=('', '_DROP')).filter(regex='^(?!.*_DROP)')
                    else:
                        df_merged = pd.merge(df_merged, df, left_on=list(on[idx-1]), right_on=list(col), how=how, 
                                             suffixes=suffixes)
        if save:
            DataGame.save_data(self, df_merged, save_name)
        return df_merged

    def concat_data(self, data_list, ignore_index=False, save=False, save_name=None) -> pd.DataFrame:
        df_list = []
        for df in data_list:
            df_copy = df.copy()
            df_copy.columns = df_copy.columns.str.lower()
            df_list.append(df_copy)
        df_concat = pd.concat(df_list, axis=0, ignore_index=ignore_index)
        
        if save:
            DataGame.save_data(self, df_concat, save_name)

        return df_concat
    
    def remove_outlier(self, data, colname, iqr_range=IQR_THRESHOLD, dropna=False, keep_all=False, key=None, save=False, save_name=None) -> pd.DataFrame:
        df = data.copy()
        if dropna:
            df.dropna(subset=[colname])

        q1 = data[colname].quantile(0.25)
        q3 = data[colname].quantile(0.75)
        iqr = q3 - q1 #Interquartile range
        fence_low  = q1 - iqr_range * iqr
        fence_high = q3 + iqr_range * iqr
        df_out = df.loc[(df[colname] > fence_low) & (df[colname] < fence_high)]

        if save:
            DataGame.save_data(self, df_out, save_name)
        
        if keep_all:
            keep_vars = df_out.columns.tolist()
        else:
            if key is None:
                keep_vars = [colname]
            else:
                keep_vars = list(key)
                keep_vars.append(colname)
        return df_out[keep_vars]
            

    def normalize_data(self, data, x: str, y, outlier_threshold=IQR_THRESHOLD, save=False, save_name=None):
        df = data.copy()
        for var in [x, y]:
            df = DataGame.remove_outlier(self, df, var, iqr_range=outlier_threshold, dropna=True, keep_all=True)
        X = df[x].values.reshape(-1, 1)
        Y = df[y].values.reshape(-1, 1)
        pred_y = LinearRegression().fit(X, Y).predict(X)
        # df[f"{y}_Pred"] = np.squeeze(pred_y)
        df[f"{y}_N"] = np.squeeze(pred_y) - df[y]
        print(f"{y} normalize to {x} R2: {round(r2_score(Y, pred_y), 4)}") 

        if save:
            DataGame.save_data(self, df, save_name)

        return df

    def normalize_multi_data(self, data, x, y_list, key_para,outlier_threshold=IQR_THRESHOLD, save=False, save_name=None):
        dfs = [data]
        for y in y_list:
            globals()[f'df_{y}'] = DataGame.normalize_data(self, data, x, y, outlier_threshold=outlier_threshold)
            dfs.append(globals()[f'df_{y}']) 
        dfs.sort(key=lambda s: len(s), reverse=True)
        df_out = DataGame.merge_data(self, dfs, on=key_para, drop_samecol=True)
        if save:
            DataGame.save_data(self, df_out, save_name)
        return df_out

    def calculate_stats(self, data, cols, keys=None, group=None,percentiles=None, 
                        keep_minmax=False, iqr_range=10, save=False, save_name=None):
        # define keys -- merge on variables
        if group is None:
            pass
        else:
            keys = list(keys) + list(group)

        # remove outliers for each variable
        df = data[keys]
        for col in cols:
            col_series = DataGame.remove_outlier(self, data, col, iqr_range=iqr_range, dropna=False, 
                                                 keep_all=False, key=keys)
            df = pd.merge(df, col_series, on=keys, how='outer')    
        # perform summary
        if group is None:
            summary_df = df[cols].describe(percentiles=percentiles)   
            summary_out = summary_df.T.reset_index(names=['Parameters'])
        else:
            summary_df = df.groupby(group)[cols].describe(percentiles=percentiles)
            summary_df.columns = ['_'.join(cols) for cols in summary_df.columns.to_flat_index()]
            summary_out = summary_df.reset_index()

        if keep_minmax:
            pass
        else:
            min_max = ["max", "min", "50"]
            all_stats = summary_out.columns.tolist()
            remove_vars = [var for stat in min_max for var in all_stats if stat in var]
            keep_stats = [col for col in all_stats if col not in remove_vars]
            summary_out  = summary_out[keep_stats]
        
        if save:
            DataGame.save_data(self, summary_out, save_name)
        return summary_out

        





    
        



