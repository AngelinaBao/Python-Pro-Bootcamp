from process_data import DataSoup
import time

start_time = time.time()
# --------------Read Data WK by WK----------------- 

QST_SORT_VARS = ["sn", "STORETS"]
QST_KEEP_VARS = ['PRODUCT', 'SEQUENCE_PARM', 'wafer_ec', 'TOOL', 'UP_DN', 'sn', 'STORETS', 'SPEC_DEF_CODE',
             'RCold_Res_MR1', 'RCold_Res_MR2', 'Delta_RC_R1', 'Delta_RC_R2', 
             'RCold_Res_MR1_Qst_A', 'RCold_Res_MR2_Qst_A', 'Quasi_WK']
QST_FILTER = 'wafer_ec in ["GD2b"] ' 


ds = DataSoup(path=r"C:\Data warehouse\GD2\QST\PHO", product="gd2_qst")
ds.preview_header(year=2023, wk=23, wk_label=True, save=False)
# qst = ds.read_sas(year=2023, wk=23, keep_vars=QST_KEEP_VARS, condition=QST_FILTER, sort_by=QST_SORT_VARS, save=False)
qst = ds.pull_bywk(year=2023, start=23, end=23, keep_vars=QST_KEEP_VARS, condition=QST_FILTER, 
                   sort_by=QST_SORT_VARS, save=True, save_name="LDS_GD2b_qst.csv")                  

ds.summary(qst, save=False, display_head=True)
ds.read_col_name(qst)
ds.read_col_value(qst, ["UP_DN", "wafer_ec"])
ds.read_col_value(qst, "PRODUCT")


# --------------Read List Data----------------- 
SNLIST_FILTER = 'sn.notna() & "." not in sn'

sn_ds = DataSoup(path="./backup/")
snlist = sn_ds.read_list("LDS_GD2b_qst.csv", keep_vars=['sn'], condition=SNLIST_FILTER)

# --------------Read Data based on a List----------------- 
FUNC_SORT_VARS = ["hddsn", "HD", "enddate"]
FUNC_KEEP_VARS = ['site', 'procid', 'HDD_GRP', 'HDD_Cap', 'HDD_MODEL', 'hddtrial', 'enddate', 'hddsn', 'HD', 
             'slidersn', 'pfcode', 'BADHEAD', 'hddcycle', 'ASM_DATE', 'mfgid', 'Grade_Combine_RAW', 'disk',
             'pACC', 'iACC', 'MCW_MD', 'OWP_MD_post', 'OWC_MD_post', 'BPISER_MD']
FILE_PATH = r"E:\Data warehouse\LDS\HDD Simple"
func_ds = DataSoup(path=FILE_PATH, product="cmr_func")
func_ds.preview_header(year=2023, wk=23, wk_label=True, save=False)
func= func_ds.pull_bylist(snlist, FUNC_KEEP_VARS, year=2023, start=40, end=43, 
                        how="inner", left_on=['slidersn'], right_on=['sn'], 
                        sort_by=FUNC_SORT_VARS, save=True, save_name="LDS_GD2b_Func.csv")
# func_ds.save_data(func, "LDS_GD2b_Func_r1.csv")

SRST_KEEP_VARS = ['site', 'procid', 'HDD_GRP', 'HDD_Cap', 'HDD_MODEL', 'hddtrial', 'enddate', 'hddsn', 'HD', 
             'slidersn', 'pfcode', 'BADHEAD', 'hddcycle', 'ASM_DATE', 'mfgid', 'Grade_Combine_RAW', 'disk']
srst_ds = DataSoup(path=FILE_PATH, product="cmr_srst")
srst_ds.preview_header(year=2023, wk=23, wk_label=True, save=False)
srst= srst_ds.pull_bylist(snlist, SRST_KEEP_VARS, year=2023, start=40, end=43, 
                        how="inner", left_on=['slidersn'], right_on=['sn'], 
                        sort_by=FUNC_SORT_VARS, save=True, save_name="LDS_GD2b_Srst.csv")


func_ds.read_col_name(func)
func_ds.read_col_value(func, ["HDD_GRP", "HDD_Cap", "disk"])
func_ds.read_col_value(func, 'HDD_GRP')

# ------------------ADD New Columns-------------------------
def set_group(data):
    if data["HDD_GRP"].startswith("PHO"):
        return "PHO"
    elif data["HDD_GRP"].startswith("THO"):
        return "THO"
    else:
        return "Other"

func = func_ds.add_col(func, "Site", set_group)
# func["Group"] = func.apply(set_group, axis=1) # add new column based on condition
func["Site_Disk"] = func["HDD_GRP"].str[:3] + "_" + func["disk"] # add new column based on current columns
func_ds.read_col_value(func, ["Site_Disk", "Site", "disk"])

func["Wafernum"] = func["slidersn"].str[:5].apply(lambda x: int(x, 16))
func_ds.read_col_name(func)
func_ds.read_col_value(func, "Wafernum")

# ---------------------Filter Data------------------------------
SL6a_filter = 'Site_Disk.str.split("_").str[-1] == "SL6a"'
func_SL6a = func_ds.filter_data(func, SL6a_filter)


# ---------------------Merge Data------------------------------
func_srst = func_ds.merge_data([func, srst], on=["hddsn", "HD", "slidersn"], how="left", 
                                suffixes=("_6400", "_6600"))
func_ds.read_col_name(func_srst)


# ---------------------Drop Colnums------------------------------
func_ds.remove_col(func_srst, ['hddcycle_6600', 'enddate_6600', 'mfgid_6600', 'disk_6600', 'sn_6600'], inplace=True)
func_ds.read_col_name(func_srst)

# ---------------------Concatenate Data------------------------------
hdd = func_ds.concat_data([func, srst])
print(hdd.procid.value_counts())


# ---------------------Normalize Data------------------------------
func_n = func_ds.normalize_multi_data(func, "MCW_MD", 
                                    ["pACC", "OWP_MD_post", "OWC_MD_post", "BPISER_MD"], 
                                    key_para=["hddsn", "HD", "slidersn"], 
                                    save=True, save_name="LDS_GD2b_Func_Nor.csv")
func_ds.summary(func_n, display_head=True)
# print(func.shape, func_n.shape)

# ---------------------Summarize statistics------------------------------
summary_func = func_ds.calculate_stats(func, ["MCW_MD","pACC", "OWP_MD_post"], 
                                       keys=["hddsn", "HD", "slidersn"],
                                       group=["Site", "Wafernum"], 
                                       percentiles=[.01, .99], save=True, save_name="Func_summary_persite.csv")
summary_func_oa = func_ds.calculate_stats(func, ["MCW_MD","pACC", "OWP_MD_post"], 
                                       keys=["hddsn", "HD", "slidersn"],
                                       percentiles=[.01, .99], 
                                       save=True, save_name="Func_summary_oa.csv")

print(f"Running time: {round(time.time() - start_time, 2)} seconds")