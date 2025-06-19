import os
import warnings
from datetime import datetime
from types import SimpleNamespace

# Imports of toolbox functions (to be implemented)
# from nowcasting_toolbox_py.tools.common_load_data import common_load_data
# from nowcasting_toolbox_py.tools.common_heatmap import common_heatmap
# from nowcasting_toolbox_py.tools.common_NaN_Covid_correct import common_NaN_Covid_correct
# from nowcasting_toolbox_py.models.dfm import DynamicFactorModel
# from nowcasting_toolbox_py.tools.DFM_estimate import DFM_estimate
# from nowcasting_toolbox_py.tools.BEQ_estimate import BEQ_estimate
# from nowcasting_toolbox_py.tools.BVAR_estimate import BVAR_estimate
# from nowcasting_toolbox_py.tools.DFM_News_Mainfile import DFM_News_Mainfile
# from nowcasting_toolbox_py.tools.BEQ_News_Mainfile import BEQ_News_Mainfile
# from nowcasting_toolbox_py.tools.BVAR_News_Mainfile import BVAR_News_Mainfile
# from nowcasting_toolbox_py.tools.common_range import common_range
# from nowcasting_toolbox_py.tools.common_mae import common_mae
# from nowcasting_toolbox_py.tools.common_save_results import common_save_results
# from nowcasting_toolbox_py.tools.common_eval_models import common_eval_models

def main():
    # ---------------------------------------------------------------------
    # 0. TOOLBOX SETTINGS
    # ---------------------------------------------------------------------
    do_eval = True      # False = nowcast, True = model evaluation
    do_loop = False     # False = single model, True = loop over models
    do_range = False    # compute alternative model ranges
    do_mae = False      # compute MAE/FDA from past errors
    do_subset = False   # subset of input data

    # ---------------------------------------------------------------------
    # 1. MODEL INPUTS
    # ---------------------------------------------------------------------
    country = SimpleNamespace()
    country.name = 'Example1'
    country.model = 'DFM'  # 'DFM', 'BEQ', or 'BVAR'

    # Model hyper-parameters
    Par = SimpleNamespace()
    # common
    Par.startyear = 2005
    Par.startmonth = 1
    do_Covid = 0         # 0: none, 1: dummies Jun/Sep2020, 2: NaN, 3: outlier-corr, 4: dummies Mar/Jun2020

    # DFM parameters
    Par.p = 4            # lags
    Par.r = 5            # factors
    Par.idio = 1         # idiosyncratic: 0=iid,1=AR(1)
    Par.thresh = 1e-4
    Par.max_iter = 100
    Par.block_factors = False

    # Bridge equation
    Par.lagM = 1
    Par.lagQ = 1
    Par.lagY = 1
    Par.type = 901
    Par.Dum = [(2020,3), (2020,6), (2020,9)]

    # BVAR parameters
    Par.bvar_lags = 5
    Par.bvar_thresh = 1e-6
    Par.bvar_max_iter = 200

    # MAE / FDA parameters (user-specified)
    MAE = SimpleNamespace(
        Bac=SimpleNamespace(mae_1st=0.15, mae_2nd=0.15, mae_3rd=0.15,
                            fda_1st=0.88, fda_2nd=0.88, fda_3rd=0.88),
        Now=SimpleNamespace(mae_1st=0.24, mae_2nd=0.24, mae_3rd=0.21,
                            fda_1st=0.73, fda_2nd=0.85, fda_3rd=0.88),
        For=SimpleNamespace(mae_1st=0.48, mae_2nd=0.30, mae_3rd=0.29,
                            fda_1st=0.56, fda_2nd=0.68, fda_3rd=0.70)
    )

    # Evaluation parameters
    Eval = SimpleNamespace(
        data_update_lastyear=2023,
        data_update_lastmonth=10,
        eval_startyear=2020,
        eval_startmonth=10,
        eval_endyear=2022,
        eval_endmonth=10,
        gdp_rel=2
    )

    # Loop parameters
    Loop = SimpleNamespace(
        n_iter=10,
        name_loop='b1',
        min_startyear=2008,
        max_startyear=2014,
        startmonth=1,
        min_var=5,
        max_var=10,
        min_p=1,
        max_p=4,
        min_r=2,
        max_r=6,
        min_lagM=1,
        max_lagM=4,
        min_lagQ=1,
        max_lagQ=4,
        min_lagY=1,
        max_lagY=2,
        min_bvar_lags=2,
        max_bvar_lags=4,
        do_random=True,
        list_name='Eval_list_DFM.xlsx',
        name_customloop='customloop',
        alter_covid=True
    )

    var_keep = [1,3,5,7,9,10,11,13,14,15,19,21,22,24,25,26,27,28,30,31]

    print("Section 1: Model inputs loaded")

    # ---------------------------------------------------------------------
    # 2. SETUP FOLDERS AND FILES
    # ---------------------------------------------------------------------
    m = 6  # months ahead

    if not do_eval:
        date_today = datetime.today()
    else:
        date_today = datetime(Eval.data_update_lastyear, Eval.data_update_lastmonth, 1)

    rootfolder = os.getcwd()
    outputfolder = os.path.join(rootfolder, 'output', country.name)
    excel_datafile = f"data_{country.name}.xlsx"
    excel_outputfile = os.path.join(outputfolder, f"{country.name}_tracking.xlsx")
    newsfile = 'cur_nowcast.mat'

    # Align loop name
    if do_loop == 2:
        Loop.name_loop = Loop.name_customloop

    Loop.excel_loopfile = os.path.join(rootfolder, 'eval', country.name,
                                       f"{country.name}_{country.model}_loop_{Loop.name_loop}.xlsx")

    print("Section 2: Folders and files set up")

    # ---------------------------------------------------------------------
    # 3. LOAD DATA & INITIALIZE
    # ---------------------------------------------------------------------
    # Par, xest, t_m, groups, nameseries, blocks, groups_name, fullnames, datet, Loop = \
    #     common_load_data(excel_datafile, 'Monthly', 'Quarterly', 'blocks', Par, m,
    #                      do_loop, date_today, Loop)

    # if do_subset:
    #     # subset logic
    #     pass

    print("Section 3: Data loaded")

    if not do_eval:
        # -----------------------------------------------------------------
        # 4. ESTIMATE AND NEWS DECOMPOSITION
        # -----------------------------------------------------------------
        # heatmap = common_heatmap(xest, Par, groups, groups_name, fullnames)
        print("Section 4: Starting estimation")
        # xest_out, ... = common_NaN_Covid_correct(xest, datet, do_Covid, ...)
        # Res = {
        #     'DFM': lambda: DFM_estimate(xest_out, Par),
        #     'BEQ': lambda: BEQ_estimate(xest_out, Par, datet, nameseries, True, []),
        #     'BVAR': lambda: BVAR_estimate(xest_out, Par, datet)
        # }[country.model]()
        print("Section 4: Estimation completed")

        # -----------------------------------------------------------------
        # 5. NEWS DECOMPOSITION
        # -----------------------------------------------------------------
        print("Section 5: News decomposition")
        # news_results, news_results_fcst, ... = {
        #     'DFM': lambda: DFM_News_Mainfile(...),
        #     'BEQ': lambda: BEQ_News_Mainfile(...),
        #     'BVAR': lambda: BVAR_News_Mainfile(...)
        # }[country.model]()

        # -----------------------------------------------------------------
        # 6. RANGE OF NOWCASTS
        # -----------------------------------------------------------------
        if do_range:
            print("Section 6: Computing range of nowcasts")
            # range_ = common_range(...)
        else:
            range_ = None
            print("Section 6: Skipping range (do_range=False)")

        # -----------------------------------------------------------------
        # 7. ERROR EVALUATION
        # -----------------------------------------------------------------
        print("Section 7: Error evaluation")
        # MAE = common_mae(xest, Par, t_m, m, datet, do_Covid, country, MAE, do_mae, nameseries)

        # -----------------------------------------------------------------
        # 8. SAVE RESULTS
        # -----------------------------------------------------------------
        print("Section 8: Saving results")
        # common_save_results(...)

    else:
        # -----------------------------------------------------------------
        # EVALUATION MODE
        # -----------------------------------------------------------------
        print("Section: Running evaluation mode")
        # Loop, Eval = common_eval_models(do_loop, Loop, Eval, xest, Par, t_m, m, country, datet, do_Covid, groups)

    print("End nowcast")

if __name__ == '__main__':
    main()
