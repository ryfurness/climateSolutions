"""Biomass from Perennial Crops for Electricity Generation solution model.
   Excel filename: Drawdown-Biomass from Perennial Crops for Electricity Generation_RRS.ES_v1.1_13Jan2019_PUBLIC.xlsm
"""

import pathlib

import numpy as np
import pandas as pd

from model import adoptiondata
from model import advanced_controls
from model import ch4calcs
from model import co2calcs
from model import customadoption
from model import emissionsfactors
from model import firstcost
from model import helpertables
from model import operatingcost
from model import s_curve
from model import unitadoption
from model import vma
from model.advanced_controls import SOLUTION_CATEGORY

from model import tam
from solution import rrs

DATADIR = str(pathlib.Path(__file__).parents[2].joinpath('data'))
THISDIR = pathlib.Path(__file__).parents[0]
VMAs = vma.generate_vma_dict(THISDIR.joinpath('vma_data'))

REGIONS = ['World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)', 'Middle East and Africa',
           'Latin America', 'China', 'India', 'EU', 'USA']

scenarios = {
  'PDS-2p2050-Plausible (Book Ed. 1)': advanced_controls.AdvancedControls(
      # Plausible Scenario, This scenario follows a medium growth trajectory derived
      # from the biomass and waste electricity generation projections of the 2°C
      # Scenario of Energy Technology Perspectives from the International Energy Agency
      # (IEA, 2016), and the Energy [R]evolution Scenario (Greenpeace, 2015). The share
      # of biomass from these values is estimated to be 77.8 percent, of which 20.2
      # percent is assumed to use perennial biomass as a feedstock.

      # general
      solution_category='REPLACEMENT', 
      vmas=VMAs,
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source='Ambitious Cases', 
      soln_pds_adoption_prognostication_trend='3rd Poly', 
      soln_pds_adoption_prognostication_growth='Medium', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='Baseline Cases', 
      pds_source_post_2014='Drawdown TAM: Drawdown TAM - Post Integration - Plausible Scenario', 
      pds_base_adoption=[('World', 55.418723948374556), ('OECD90', 1.374902800958828), ('Eastern Europe', 0.049897295303677716), ('Asia (Sans Japan)', 4.292985516188078), ('Middle East and Africa', 0.41937969656046536), ('Latin America', 12.138577652661485), ('China', 4.6261055160089875), ('India', 3.3303919448438495), ('EU', 17.146488383747197), ('USA', 9.810373894058708)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=4440.0, ref_2014_cost=4440.0, 
      conv_2014_cost=2010.0317085196398, 
      soln_first_cost_efficiency_rate=0.075, 
      conv_first_cost_efficiency_rate=0.02, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=150171.4399091095, soln_avg_annual_use=5751.246634816959, 
      conv_lifetime_capacity=182411.2757676607, conv_avg_annual_use=4946.8401873420025, 

      soln_var_oper_cost_per_funit=0.015, soln_fuel_cost_per_funit=0.026376896689174464, 
      soln_fixed_oper_cost_per_iunit=47.95705623980464, 
      conv_var_oper_cost_per_funit=0.003752690403548987, conv_fuel_cost_per_funit=0.07, 
      conv_fixed_oper_cost_per_iunit=32.951404311078015, 

      # emissions
      ch4_is_co2eq=True, n2o_is_co2eq=True, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=31860.185185185182, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_funit=0.0, n2o_co2_per_funit=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=55500.0, 

    ),
  'PDS-1p2050-Drawdown (Book Ed. 1)': advanced_controls.AdvancedControls(
      # Drawdown Scenario, This scenario takes a medium growth adoption trajectory from
      # the IEA ETP 4°C Scenario and Greenpeace Reference Scenario. For this scenario,
      # instead of applying a constant share of perennials throughout the modeling
      # period, an increasing share was applied based on the production of perennial
      # energy crops, reaching 51 percent in 2050.

      # general
      solution_category='REPLACEMENT', 
      vmas=VMAs,
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source='Conservative Cases', 
      soln_pds_adoption_prognostication_trend='3rd Poly', 
      soln_pds_adoption_prognostication_growth='Medium', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='Baseline Cases', 
      pds_source_post_2014='Drawdown TAM: Drawdown TAM - Post Integration - Drawdown Scenario', 
      pds_base_adoption=[('World', 55.418723948374556), ('OECD90', 1.374902800958828), ('Eastern Europe', 0.049897295303677716), ('Asia (Sans Japan)', 4.292985516188078), ('Middle East and Africa', 0.41937969656046536), ('Latin America', 12.138577652661485), ('China', 4.6261055160089875), ('India', 3.3303919448438495), ('EU', 17.146488383747197), ('USA', 9.810373894058708)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=4440.0, ref_2014_cost=4440.0, 
      conv_2014_cost=2010.0317085196398, 
      soln_first_cost_efficiency_rate=0.075, 
      conv_first_cost_efficiency_rate=0.02, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=150171.4399091095, soln_avg_annual_use=5751.246634816959, 
      conv_lifetime_capacity=182411.2757676607, conv_avg_annual_use=4946.8401873420025, 

      soln_var_oper_cost_per_funit=0.015, soln_fuel_cost_per_funit=0.026376896689174464, 
      soln_fixed_oper_cost_per_iunit=47.95705623980464, 
      conv_var_oper_cost_per_funit=0.003752690403548987, conv_fuel_cost_per_funit=0.07, 
      conv_fixed_oper_cost_per_iunit=32.951404311078015, 

      # emissions
      ch4_is_co2eq=True, n2o_is_co2eq=True, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=31860.185185185182, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_funit=0.0, n2o_co2_per_funit=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=55500.0, 

    ),
  'PDS-0p2050-Optimum (Book Ed. 1)': advanced_controls.AdvancedControls(
      # Optimum Scenario, This scenario considers the low growth of the IEA ETP 6°C
      # Scenario projections, and a linear trend line extrapolation of 2006-2015
      # historical data for biomass and waste. Similar calculations to the Plausible
      # Scenario were considered for the electricity generated from perennial crops.

      # general
      solution_category='REPLACEMENT', 
      vmas=VMAs,
      report_start_year=2020, report_end_year=2050, 

      # adoption
      soln_ref_adoption_basis='Default', 
      soln_ref_adoption_regional_data=False, soln_pds_adoption_regional_data=False, 
      soln_pds_adoption_basis='Existing Adoption Prognostications', 
      soln_pds_adoption_prognostication_source='Baseline Cases', 
      soln_pds_adoption_prognostication_trend='3rd Poly', 
      soln_pds_adoption_prognostication_growth='Low', 
      source_until_2014='ALL SOURCES', 
      ref_source_post_2014='Baseline Cases', 
      pds_source_post_2014='Drawdown TAM: Drawdown TAM - Post Integration - Optimum Scenario', 
      pds_base_adoption=[('World', 55.418723948374556), ('OECD90', 1.374902800958828), ('Eastern Europe', 0.049897295303677716), ('Asia (Sans Japan)', 4.292985516188078), ('Middle East and Africa', 0.41937969656046536), ('Latin America', 12.138577652661485), ('China', 4.6261055160089875), ('India', 3.3303919448438495), ('EU', 17.146488383747197), ('USA', 9.810373894058708)], 
      pds_adoption_final_percentage=[('World', 0.0), ('OECD90', 0.0), ('Eastern Europe', 0.0), ('Asia (Sans Japan)', 0.0), ('Middle East and Africa', 0.0), ('Latin America', 0.0), ('China', 0.0), ('India', 0.0), ('EU', 0.0), ('USA', 0.0)], 

      # financial
      pds_2014_cost=4440.0, ref_2014_cost=4440.0, 
      conv_2014_cost=2010.0317085196398, 
      soln_first_cost_efficiency_rate=0.075, 
      conv_first_cost_efficiency_rate=0.02, 
      soln_first_cost_below_conv=True, 
      npv_discount_rate=0.094, 
      soln_lifetime_capacity=150171.4399091095, soln_avg_annual_use=5751.246634816959, 
      conv_lifetime_capacity=182411.2757676607, conv_avg_annual_use=4946.8401873420025, 

      soln_var_oper_cost_per_funit=0.015, soln_fuel_cost_per_funit=0.026376896689174464, 
      soln_fixed_oper_cost_per_iunit=47.95705623980464, 
      conv_var_oper_cost_per_funit=0.003752690403548987, conv_fuel_cost_per_funit=0.07, 
      conv_fixed_oper_cost_per_iunit=32.951404311078015, 

      # emissions
      ch4_is_co2eq=True, n2o_is_co2eq=True, 
      co2eq_conversion_source='AR5 with feedback', 
      soln_indirect_co2_per_iunit=31860.185185185182, 
      conv_indirect_co2_per_unit=0.0, 
      conv_indirect_co2_is_iunits=False, 
      ch4_co2_per_funit=0.0, n2o_co2_per_funit=0.0, 

      soln_energy_efficiency_factor=0.0, 
      soln_annual_energy_used=0.0, conv_annual_energy_used=0.0, 
      conv_fuel_consumed_per_funit=0.0, soln_fuel_efficiency_factor=0.0, 
      conv_fuel_emissions_factor=0.0, soln_fuel_emissions_factor=0.0, 

      emissions_grid_source='Meta-Analysis', emissions_grid_range='Mean', 
      emissions_use_co2eq=True, 
      conv_emissions_per_funit=0.0, soln_emissions_per_funit=55500.0, 

    ),
}

class Biomass:
  name = 'Biomass from Perennial Crops for Electricity Generation'
  units = {
    "implementation unit": "TW",
    "functional unit": "TWh",
    "first cost": "US$B",
    "operating cost": "US$B",
  }

  def __init__(self, scenario=None):
    if scenario is None:
      scenario = 'PDS-2p2050-Plausible (Book Ed. 1)'
    self.scenario = scenario
    self.ac = scenarios[scenario]

    # TAM
    tamconfig_list = [
      ['param', 'World', 'PDS World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['source_until_2014', self.ac.source_until_2014, self.ac.source_until_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
      ['source_after_2014', self.ac.ref_source_post_2014, self.ac.pds_source_post_2014,
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES',
       'ALL SOURCES', 'ALL SOURCES', 'ALL SOURCES'],
      ['trend', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly'],
      ['growth', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    tamconfig = pd.DataFrame(tamconfig_list[1:], columns=tamconfig_list[0], dtype=np.object).set_index('param')
    self.tm = tam.TAM(tamconfig=tamconfig, tam_ref_data_sources=rrs.tam_ref_data_sources,
      tam_pds_data_sources=rrs.tam_pds_data_sources)
    ref_tam_per_region=self.tm.ref_tam_per_region()
    pds_tam_per_region=self.tm.pds_tam_per_region()

    adconfig_list = [
      ['param', 'World', 'OECD90', 'Eastern Europe', 'Asia (Sans Japan)',
       'Middle East and Africa', 'Latin America', 'China', 'India', 'EU', 'USA'],
      ['trend', self.ac.soln_pds_adoption_prognostication_trend, '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly', '3rd Poly',
       '3rd Poly', '3rd Poly', '3rd Poly'],
      ['growth', self.ac.soln_pds_adoption_prognostication_growth, 'Medium',
       'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
       'Medium', 'Medium', 'Medium'],
      ['low_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      ['high_sd_mult', 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]
    adconfig = pd.DataFrame(adconfig_list[1:], columns=adconfig_list[0], dtype=np.object).set_index('param')
    ad_data_sources = {
      'Baseline Cases': {
          'Based on: IRENA (2016)': THISDIR.joinpath('ad', 'ad_based_on_IRENA_2016.csv'),
          'Based on: IEA ETP 2016 6DS': THISDIR.joinpath('ad', 'ad_based_on_IEA_ETP_2016_6DS.csv'),
      },
      'Conservative Cases': {
          'Based on: IEA ETP 2016 4DS': THISDIR.joinpath('ad', 'ad_based_on_IEA_ETP_2016_4DS.csv'),
          'Based on: Greenpeace (2015) - Reference Scenario': THISDIR.joinpath('ad', 'ad_based_on_Greenpeace_2015_Reference_Scenario.csv'),
      },
      'Ambitious Cases': {
          'Based on: IEA ETP 2016 2DS': THISDIR.joinpath('ad', 'ad_based_on_IEA_ETP_2016_2DS.csv'),
          'Based on: Greenpeace 2015 Energy Revolution': THISDIR.joinpath('ad', 'ad_based_on_Greenpeace_2015_Energy_Revolution.csv'),
          'Based on: Greenpeace 2015 Energy Revolution with Drawdown perennials': THISDIR.joinpath('ad', 'ad_based_on_Greenpeace_2015_Energy_Revolution_with_Drawdown_perennials.csv'),
          'Based on: Greenpeace 2015 Advanced Revolution with Drawdown perennials': THISDIR.joinpath('ad', 'ad_based_on_Greenpeace_2015_Advanced_Revolution_with_Drawdown_perennials.csv'),
          'Based on: IEA ETP 2016 2DS with OPT2 perennials': THISDIR.joinpath('ad', 'ad_based_on_IEA_ETP_2016_2DS_with_OPT2_perennials.csv'),
      },
      '100% RES2050 Case': {
          'Based on: Greenpeace 2015 Advanced Revolution': THISDIR.joinpath('ad', 'ad_based_on_Greenpeace_2015_Advanced_Revolution.csv'),
      },
    }
    self.ad = adoptiondata.AdoptionData(ac=self.ac, data_sources=ad_data_sources,
        adconfig=adconfig)

    ref_adoption_data_per_region = None

    if False:
      # One may wonder why this is here. This file was code generated.
      # This 'if False' allows subsequent conditions to all be elif.
      pass
    elif self.ac.soln_pds_adoption_basis == 'Existing Adoption Prognostications':
      pds_adoption_data_per_region = self.ad.adoption_data_per_region()
      pds_adoption_trend_per_region = self.ad.adoption_trend_per_region()
      pds_adoption_is_single_source = self.ad.adoption_is_single_source()

    ht_ref_adoption_initial = pd.Series(
      [55.418723948374556, 1.374902800958828, 0.049897295303677716, 4.292985516188078, 0.41937969656046536,
       12.138577652661485, 4.6261055160089875, 3.3303919448438495, 17.146488383747197, 9.810373894058708],
       index=REGIONS)
    ht_ref_adoption_final = ref_tam_per_region.loc[2050] * (ht_ref_adoption_initial / ref_tam_per_region.loc[2014])
    ht_ref_datapoints = pd.DataFrame(columns=REGIONS)
    ht_ref_datapoints.loc[2014] = ht_ref_adoption_initial
    ht_ref_datapoints.loc[2050] = ht_ref_adoption_final.fillna(0.0)
    ht_pds_adoption_initial = ht_ref_adoption_initial
    ht_regions, ht_percentages = zip(*self.ac.pds_adoption_final_percentage)
    ht_pds_adoption_final_percentage = pd.Series(list(ht_percentages), index=list(ht_regions))
    ht_pds_adoption_final = ht_pds_adoption_final_percentage * pds_tam_per_region.loc[2050]
    ht_pds_datapoints = pd.DataFrame(columns=REGIONS)
    ht_pds_datapoints.loc[2014] = ht_pds_adoption_initial
    ht_pds_datapoints.loc[2050] = ht_pds_adoption_final.fillna(0.0)
    self.ht = helpertables.HelperTables(ac=self.ac,
        ref_datapoints=ht_ref_datapoints, pds_datapoints=ht_pds_datapoints,
        pds_adoption_data_per_region=pds_adoption_data_per_region,
        ref_adoption_limits=ref_tam_per_region, pds_adoption_limits=pds_tam_per_region,
        pds_adoption_trend_per_region=pds_adoption_trend_per_region,
        pds_adoption_is_single_source=pds_adoption_is_single_source)

    self.ef = emissionsfactors.ElectricityGenOnGrid(ac=self.ac)

    self.ua = unitadoption.UnitAdoption(ac=self.ac,
        ref_total_adoption_units=ref_tam_per_region, pds_total_adoption_units=pds_tam_per_region,
        soln_ref_funits_adopted=self.ht.soln_ref_funits_adopted(),
        soln_pds_funits_adopted=self.ht.soln_pds_funits_adopted(),
        bug_cfunits_double_count=True)
    soln_pds_tot_iunits_reqd = self.ua.soln_pds_tot_iunits_reqd()
    soln_ref_tot_iunits_reqd = self.ua.soln_ref_tot_iunits_reqd()
    conv_ref_tot_iunits = self.ua.conv_ref_tot_iunits()
    soln_net_annual_funits_adopted=self.ua.soln_net_annual_funits_adopted()

    self.fc = firstcost.FirstCost(ac=self.ac, pds_learning_increase_mult=2,
        ref_learning_increase_mult=2, conv_learning_increase_mult=2,
        soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
        soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
        conv_ref_tot_iunits=conv_ref_tot_iunits,
        soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
        soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
        conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
        fc_convert_iunit_factor=rrs.TERAWATT_TO_KILOWATT)

    self.oc = operatingcost.OperatingCost(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
        soln_pds_tot_iunits_reqd=soln_pds_tot_iunits_reqd,
        soln_ref_tot_iunits_reqd=soln_ref_tot_iunits_reqd,
        conv_ref_annual_tot_iunits=self.ua.conv_ref_annual_tot_iunits(),
        soln_pds_annual_world_first_cost=self.fc.soln_pds_annual_world_first_cost(),
        soln_ref_annual_world_first_cost=self.fc.soln_ref_annual_world_first_cost(),
        conv_ref_annual_world_first_cost=self.fc.conv_ref_annual_world_first_cost(),
        single_iunit_purchase_year=2017,
        soln_pds_install_cost_per_iunit=self.fc.soln_pds_install_cost_per_iunit(),
        conv_ref_install_cost_per_iunit=self.fc.conv_ref_install_cost_per_iunit(),
        conversion_factor=rrs.TERAWATT_TO_KILOWATT)

    self.c4 = ch4calcs.CH4Calcs(ac=self.ac,
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted)

    self.c2 = co2calcs.CO2Calcs(ac=self.ac,
        ch4_ppb_calculator=self.c4.ch4_ppb_calculator(),
        soln_pds_net_grid_electricity_units_saved=self.ua.soln_pds_net_grid_electricity_units_saved(),
        soln_pds_net_grid_electricity_units_used=self.ua.soln_pds_net_grid_electricity_units_used(),
        soln_pds_direct_co2_emissions_saved=self.ua.soln_pds_direct_co2_emissions_saved(),
        soln_pds_direct_ch4_co2_emissions_saved=self.ua.soln_pds_direct_ch4_co2_emissions_saved(),
        soln_pds_direct_n2o_co2_emissions_saved=self.ua.soln_pds_direct_n2o_co2_emissions_saved(),
        soln_pds_new_iunits_reqd=self.ua.soln_pds_new_iunits_reqd(),
        soln_ref_new_iunits_reqd=self.ua.soln_ref_new_iunits_reqd(),
        conv_ref_new_iunits=self.ua.conv_ref_new_iunits(),
        conv_ref_grid_CO2_per_KWh=self.ef.conv_ref_grid_CO2_per_KWh(),
        conv_ref_grid_CO2eq_per_KWh=self.ef.conv_ref_grid_CO2eq_per_KWh(),
        soln_net_annual_funits_adopted=soln_net_annual_funits_adopted,
        fuel_in_liters=False)

    self.r2s = rrs.RRS(total_energy_demand=ref_tam_per_region.loc[2014, 'World'],
        soln_avg_annual_use=self.ac.soln_avg_annual_use,
        conv_avg_annual_use=self.ac.conv_avg_annual_use)

