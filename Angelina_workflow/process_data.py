import pandas as pd
import pyreadstat
import os
from data_game import DataGame

"""
version information:
python = 3.11.5 
pandas = 2.0.3 (pandas version must > 1.5, otherwise calculate_stats() method may raise error)
numpy = 1.24.3 
pyreadstat = 1.2.4
sklearn = 1.3.0 

Your python and libraries versions don't need to be totally same as above; 
Generally, python > 3.7 and pandas > 1.5 is enough.
"""

class DataSoup(DataGame):
    def __init__(self,  path: str=None, product: str=None):
        r"""
        Read single SAS files or read them week by week or read them based on a list.

        Parameters
        ----------
        path: str
            Data location.
        product: str, defaults to 'lds'
            The product and test. Such as for 'lds_func_2023wk23', product input should be "lds_func".
        """

        self.path = path
        self.product = product

    def create_filename_path(self, year: int, wk: int, wk_label: bool=True):
        r"""
        Generage file name path.

        Parameters
        ----------
        wk_label: bool, defaults to True
            Identifier of filename whether contains 'wk'. For example, if the filename is 'lds_func_202301'
            then wk_label should be set as False.
        year: int, defaults to 2023
            Which year of data you want to pull.
        wk: int, defaults to 1
            Which wk of data you want to find. Notice: for wk less than 10, only use the number
            itself. Such as for wk09, you should define wk=9.
        """
        if wk_label == True:
            self.file_name = "_".join([self.product, str(year) + "wk" + format(wk, '02')])
        else:
            self.file_name = "_".join([self.product, str(year) + format(wk, '02')])
        filename_path = self.path + "\\" + self.file_name + ".sas7bdat"
        
        return filename_path
        

    def read_sas(self, year: int, wk: int, wk_label: bool=True, 
                 keep_vars: list=None, condition: str=None, 
                 sort_by: list=None, save: bool=False)-> pd.DataFrame:
        r"""
        Read SAS files stored as SAS7BDAT format files.

        Parameters
        ----------
        year: int, defaults to 2023
            Define the year of data you want to find.
        wk: int, defaults to 1
            Which wk of data you want to find. Notice: for wk less than 10, please only use the number
            itself. Such as for wk09, you should define wk=9.
        wk_label: bool, defaults to True
            Identifier of filename whether contains 'wk'. For example, if the filename is 'lds_func_202301'
            then wk_label should be set as False.
        keep_vars: list, defaults to None
            If None, all columns will be read. Otherwise, the columns in list will be read.
        condition: str, defaults to None
            Filter condition for pulling data. 
        sort_by: list, defaults to None
            Key list to sort and drop duplicates. If you want to keep the latest record, make sure the last
            character is a date/time. For example: sort_by=["hddsn", "hd", "enddate"]
            sort list variables must be included in keep_vars.
        """
        
        filename_path = DataSoup.create_filename_path(self, year=year, wk=wk, wk_label=wk_label) 
        
        print(f"{self.file_name} start...")

        if keep_vars == None:
            df, _ = pyreadstat.read_sas7bdat(filename_path)
        else:
            df, _ = pyreadstat.read_sas7bdat(filename_path, usecols=keep_vars)
        
        data = pd.DataFrame()
        if condition == None:
            pass
        else:
            df = df.query(condition)
        data = pd.concat([data, df], axis=0)
        
        if len(data) == 0:
            print(f"{self.file_name} is empty!")
        else:
            # drop duplicates
            if sort_by == None:
                pass
            else:
                data = DataSoup.drop_duplicates(self, df=data, by=sort_by)
        if save:
            DataSoup.save_csv(self, data, f"{self.file_name}.csv")

        return data
        

    def pull_bywk(self, year: int=None, start: int=None, end: int=None, wk_label: bool=True, 
                  keep_vars: list=None, condition: str=None, sort_by: list=None, save=False, save_name=None)-> pd.DataFrame:
        r"""
        Read SAS files stored as SAS7BDAT format files week by week.

        Parameters
        ----------
        year: int, defaults to 2023
            Define the year of data you want to find.
        start: int
            Define the beginning week you want to find.
        end: int
            Define the endding week you want to find.
        wk_label: bool, defaults to True
            Identifier of filename whether contains 'wk'.
        keep_vars: list, defaults to None
            If None, all columns will be read. Otherwise, the columns in list will be read.
        condition: str, defaults to None
            Filter condition for pulling data. 
        sort_by: list, defaults to None
            Key list to sort and drop duplicates. If you want to keep the latest record, make sure the last
            character is a date/time. For example: sort_by=["hddsn", "hd", "enddate"]
            sort list variables must be included in keep_vars.
            
        """

        dt = pd.DataFrame()
        for week in range(start, end + 1):
            data = DataSoup.read_sas(self, year=year, wk=week, wk_label=wk_label, keep_vars=keep_vars, condition=condition, sort_by=sort_by, save=False)
            if len(data) == 0:
                pass
            else:
                dt = pd.concat([dt, data], axis=0)
                print(f"read from {self.file_name} data size: {data.shape}")
        if len(dt) == 0:
            print(f"Dataset are all empty from wk{start} to wk{end}")
        else:
            if sort_by == None:
                pass
            else:
            # drop duplicates
                dt = DataSoup.drop_duplicates(self, df=dt, by=sort_by)

        if save:
            DataSoup.save_csv(self, dt, save_name)
        
        return dt
    

    def read_list(self, file_name: str, keep_vars: list=None, condition: str=None) -> pd.DataFrame:
        r"""
        Read list data, such as HDDSN list or SN list and so on.
        ONLY .sas7bdat and .csv format are supported.
        
        Parameters
        ----------
        file_name: str
            ONLY .sas7bdat and .csv format are supported.
        keep_vars: list, defaults to None
            If None, all columns will be read. Otherwise, the columns in list will be read.
        condition: str, defaults to None
            Filter condition when you read data.
        """

        if "\\" in self.path:
            filename_path = {self.path} + "\\" + file_name
        else:
            filename_path = self.path + file_name

        file_format = file_name.rpartition('.')[-1]
        if file_format == "sas7bdat":
            if keep_vars == None:
                snlist, _ = pyreadstat.read_sas7bdat(filename_path)
            else:
                snlist, _ = pyreadstat.read_sas7bdat(filename_path, usecols=keep_vars)
        elif file_format == "csv":
            if keep_vars == None:
                snlist = pd.read_csv(filename_path)
            else:
                snlist = pd.read_csv(filename_path, usecols=keep_vars)
        else:
            raise TypeError(f"{file_format} file is not supported!")
        
        if condition == None:
            pass
        else:
            snlist = snlist.query(condition)

        # snlist.columns = snlist.columns.str.upper()
        return snlist


    def pull_bylist(self, list_data: pd.DataFrame, data_keep_vars: list=None, list_keep_vars: list=None, 
                    data_condition: str=None, wk_label: bool=True, year: int=None, 
                    start: int=None, end: int=None, 
                    how:str=None, on=None, left_on=None, right_on= None, 
                    sort_by: list=None, save: bool=False, save_name=None)-> pd.DataFrame:
        r"""
        Read SAS files stored as SAS7BDAT format files based on key parameters from a list.

        Parameters
        ----------
        list_data: pd.DataFrame
            A dataframe that includes key parametrs, such as HDDSN or SN or Wafernum.
        data_keep_vars: list, defaults to None
            If None, all columns will be read. Otherwise, the columns in list will be read.
        list_keep_vars: list, defaults to None
            If None, all columns of list data will be kept.
        data_condition: str, defaults to None
            Filter condition for pulling data. 
        wk_label: bool, defaults to True
            Identifier of filename whether contains 'wk'.
        year: int, defaults to 2023
            Define the year of data you want to find.
        start: int
            Define the beginning week you want to find.
        end: int
            Define the endding week you want to find.
        on : list
            Field names to join on. Must be found in both DataFrames.
        sort_by: list, defaults to None
            Key list to sort and drop duplicates. If you want to keep the latest record, make sure the last
            character is a date/time. For example: sort_by=["hddsn", "hd", "enddate"]
            sort list variables must be included in keep_vars.
        left_on : list
            Field names to join on in left DataFrame. 
        right_on : list
            Field names to join on in right DataFrame.
        how: str, defaults to None
            Based on test data(left DataFrame), there are four method you could choose: 
            {'left', 'right', 'outer', 'inner'}
            * left: use only keys from left frame (SQL: left outer join)
            * right: use only keys from right frame (SQL: right outer join)
            * outer: use union of keys from both frames (SQL: full outer join)
            * inner: use intersection of keys from both frames (SQL: inner join).

        """

        data = pd.DataFrame()
        if list_keep_vars == None:
            pass
        else:
            list_data = list_data[list_keep_vars]

        for week in range(start, end + 1):
            dt = DataSoup.read_sas(self, year=year, wk=week, wk_label=wk_label, keep_vars=data_keep_vars, 
                                    condition=data_condition, sort_by=sort_by, save=False)
            match_data = pd.merge(dt, list_data, on=on, left_on=left_on, right_on=right_on, how=how, 
                          suffixes=('', '_DROP')).filter(regex='^(?!.*_DROP)')
            data = pd.concat([data, match_data], axis=0)
            print(f"selected data size: {match_data.shape}")
        
        if sort_by == None:
                pass
        else:
            data = DataSoup.drop_duplicates(self, df=data, by=sort_by) # drop duplicates

        if save:
            DataSoup.save_csv(self, data, save_name)
            
        return data
    

    def drop_duplicates(self, df: pd.DataFrame, by: list):
        df = df.sort_values(by=by, axis=0, ascending=False)
        df = df.drop_duplicates(subset=by[:-1], keep='first')
        return df
    

    def preview_header(self, year: int, wk: int, wk_label: bool=True, max_display=300, save=False):
        r"""
        Read per week test dataset colnum names without load the data.
        """
        filename_path = DataSoup.create_filename_path(self, year=year, wk=wk, wk_label=wk_label)
        df, _ = pyreadstat.read_sas7bdat(filename_path, metadataonly=True)
        column_name = df.columns.tolist()
        print(f"\n{self.file_name} has {len(column_name)} columns:")
        if len(column_name) > max_display:
            print(column_name[:max_display])
        else:
            print(column_name)

        if save:
            col_df = pd.Series(data=column_name, name="Column Name")
            save_name = f"{self.file_name} Column Name.csv"
            DataSoup.save_csv(self, col_df, save_name)
        
        return None
    
    def save_csv(self, data: pd.DataFrame, save_name: str=None):
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
        data.to_csv(f"./backup/{save_name}", index=False)
        return None

    