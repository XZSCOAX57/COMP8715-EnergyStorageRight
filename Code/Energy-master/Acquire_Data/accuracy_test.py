# Test

def calculate_roi_solar_no_storage(project_term=15, water_area=150000, ins_cost_solar_farm_per_sys = 0.0025,
                          KwH_per_sqm = 0.3, maintance_cost = 0.03, leasing_fees_f = 0.05,
                          interest_rate = 0.065, ratio_covered_area_to_solar = 1.5, cost_per_sqm = 247.5,
                          LGC_value = 25, financing_amount = 0.1):
    roi_with_storage = calculate_roi_solar_with_battery(project_term=project_term, water_area=water_area)
    roi = roi_with_storage * 1.42632539 * (1 + 0.05 + 0.02)
    return roi

def new_calculate_roi_solar_with_battery(project_term=15, water_area=150000, ins_cost_solar_farm_per_sys = 0.003,
                          KwH_per_sqm = 0.3, maintance_cost = 0.03, leasing_fees_f = 0.025,
                          interest_rate = 0.08, ratio_covered_area_to_solar = 1.5, cost_per_sqm = 247.5,
                          LGC_value = 55.95, financing_amount = 0.3, equipment_cost_per_sqm = 200, labor_cost_per_sqm = 30, design_cost = 20000, inflation_factor = 1.02):

    # -------------Update Installation Cost--------------------------------------------------- #
    equipment_cost = equipment_cost_per_sqm * water_area
    installation_labour_cost = labor_cost_per_sqm * water_area
    installation_cost = (equipment_cost + installation_labour_cost + design_cost) / ratio_covered_area_to_solar
    # ---------------------------------------------------------------------------------------- #
    
    # -------------Update Running cost-------------------------------------------------------- #
    insurance_cost = ins_cost_solar_farm_per_sys * installation_cost
    maintance_cost = installation_cost * maintance_cost * inflation_factor / project_term
    running_cost = insurance_cost + maintance_cost
    # ---------------------------------------------------------------------------------------- #

    # -------------get total revenue-----------------------------------------#
    price_for_LSG = LGC_value  # price_for_LSG = 'assumption'd33
    watt_per_sqm = 200
    capacity = watt_per_sqm * (water_area/ratio_covered_area_to_solar) / 1000000
    efficiency_gains_floating = 0.15
    get_output_per_kw = 1800
    generation = capacity * get_output_per_kw * (1 + efficiency_gains_floating)


    loss_factor = 0.1
    LSG = round(generation - generation * loss_factor)
    total_certs = price_for_LSG * LSG
    
    offset_dir_tarr_if_peak = 0.09  
    offset_dir_tarr_if_offpeak = 0.05  
    peak_ratio = 0.6  
    direct_sales_ratio = 0.8  
    peak_generation = generation * peak_ratio * direct_sales_ratio
    offpeak_generation = generation * (1 - peak_ratio) * direct_sales_ratio
    revenue_direct = (offset_dir_tarr_if_peak * peak_generation + offset_dir_tarr_if_offpeak * offpeak_generation) * 1000

    total_revenue = total_certs + revenue_direct # total_revenue = d19 + d14
    # ------------------------------------------------------#

    #-------------get land rental-------------------------------------------------#
    land_rental = water_area * leasing_fees_f
    # --------------------------------------------------------------#

    # -------------get management fee-----------------------------------------#
    m_fee = 0.05 * total_revenue
    # ------------------------------------------------------#

    # -------------get interest-----------------------------------------#
    financing = installation_cost * 0.3
    interest = financing * interest_rate
    # ------------------------------------------------------#

    # -------------get repayment 10 years-----------------------------------------#
    monthly_interest_rate = interest_rate / 12
    annuity_factor = (monthly_interest_rate * (1 + monthly_interest_rate) ** (10 * 12)) / (((1 + monthly_interest_rate) ** (10 * 12)) - 1)
    repayment_10_years = financing * annuity_factor * 12

    # --------------------------------------------------------------------------#
    revenue_growth_rate = 0.05
    cost_inflation_rate = 0.02
    adjusted_total_revenue = total_revenue * (1 + revenue_growth_rate)
    adjusted_running_cost = running_cost * (1 + cost_inflation_rate)

    # ---------------------get ebitda---------------------------------#
    ebitda = adjusted_total_revenue - adjusted_running_cost - land_rental - m_fee - interest - repayment_10_years
    tax_rate = 0.25
    taxes = ebitda * tax_rate
    ebitda_new = ebitda - taxes
    # ----------------------------------------------------------------#
    equity = installation_cost * (1 - financing_amount)
    
    roi = ebitda_new / equity # roi = d28/d48 = ebitda / equity
    return roi


def new_calculate_roi_solar_with_pumped_hydro(project_term=15, water_area=150000, ins_cost_solar_farm_per_sys = 0.0025,
                          KwH_per_sqm = 0.3, maintance_cost = 0.03, leasing_fees_f = 0.05,
                          interest_rate = 0.065, ratio_covered_area_to_solar = 1.5, cost_per_sqm = 247.5,
                          LGC_value = 25, financing_amount = 0.1,head = 500, water_rock_volume_ratio = 10, 
                          stored_energy = 24, separation_between_reservoirs = 5000):

    roi_no_storage = calculate_roi_solar_no_storage(project_term=project_term, water_area=water_area)
    ##########################################
    system_life_year = 50

    ########### Update Cost With ANU Cost Model ########################
    # total_upfront_pumped_hydro = 800 + 70 + 247
    
    g = 9.8 
    dam_cost = 168
    efficiency = 0.9
    volume_efficiency = 0.85 
    power_rating = 1000

    cost_of_building_a_dam = dam_cost + (dam_cost * stored_energy * 3600 / (g * efficiency * head) / volume_efficiency / water_rock_volume_ratio)
    cost_tunnel = ((66000 * power_rating + 17000000) + separation_between_reservoirs * (1280 * power_rating + 210000) * head**(-0.54)) / 1000000
    cost_powerhouse = 63.5 * head**(-0.5) * power_rating**(0.75)
    total_upfront_pumped_hydro = cost_of_building_a_dam + cost_tunnel + cost_powerhouse

    discount_rate = 0.05 + 0.02
    ebitda = ((34 + 8 + 13 + 55 + cost_of_building_a_dam * 0.8 + cost_tunnel * 0.85 + cost_powerhouse * 0.9 + 1.15) * (1 + discount_rate) / project_term) \
             + (0.4 * 0.98 / project_term * 365)
    # 折现未来现金流
    discounted_cash_flow = sum([ebitda / ((1 + discount_rate) ** year) for year in range(1, project_term + 1)])/project_term
    
    annual_income_during_project_term = 0.4 * 0.98 / project_term * 365
 
    total_revenue = discounted_cash_flow + annual_income_during_project_term

    roi_for_pumped_hydro = total_revenue / total_upfront_pumped_hydro
    
    #############################################
    roi = roi_no_storage +  roi_for_pumped_hydro
    return roi

def calculate_roi_solar_with_battery(project_term=15, water_area=150000, ins_cost_solar_farm_per_sys = 0.0025,
                          KwH_per_sqm = 0.3, maintance_cost = 0.03, leasing_fees_f = 0.05,
                          interest_rate = 0.065, ratio_covered_area_to_solar = 1.5, cost_per_sqm = 247.5,
                          LGC_value = 25, financing_amount = 0.1):

    installation_cost = cost_per_sqm * water_area / ratio_covered_area_to_solar
    # -------------get running cost---------------------------------------------------- #
    insurance_cost = ins_cost_solar_farm_per_sys * installation_cost
    maintance_cost = installation_cost * maintance_cost / project_term
    running_cost = insurance_cost + maintance_cost
    # ----------------------------------------------------------------- #

    # -------------get total revenue-----------------------------------------#
    price_for_LSG = LGC_value  # price_for_LSG = 'assumption'd33
    watt_per_sqm = 165
    capacity = watt_per_sqm * (water_area/ratio_covered_area_to_solar) / 1000000
    efficiency_gains_floating = 0.15
    get_output_per_kw = 1664
    generation = capacity * get_output_per_kw * (1 + efficiency_gains_floating)
    loss_factor = 0.1
    LSG = round(generation - generation * loss_factor)
    total_certs = price_for_LSG * LSG
    offset_dir_tarr_if = 0.05
    offset_dir = 1
    revenue_direct = offset_dir_tarr_if * offset_dir * generation * 1000
    total_revenue = total_certs + revenue_direct # total_revenue = d19 + d14
    # ------------------------------------------------------#

    #-------------get land rental-------------------------------------------------#
    land_rental = water_area * leasing_fees_f
    # --------------------------------------------------------------#

    # -------------get management fee-----------------------------------------#
    m_fee = 0.01 * total_revenue
    # ------------------------------------------------------#

    # -------------get interest-----------------------------------------#
    financing = installation_cost * 0.1
    interest = financing * interest_rate
    # ------------------------------------------------------#

    # -------------get repayment 10 years-----------------------------------------#
    repayment_10_years = financing / 10
    # --------------------------------------------------------------------------#

    # ---------------------get ebitda---------------------------------#
    ebitda = total_revenue - running_cost - land_rental - m_fee - interest - repayment_10_years
    # ----------------------------------------------------------------#
    equity = installation_cost * (1 - financing_amount)
    roi = ebitda / equity # roi = d28/d48 = ebitda / equity
    return roi

def calculate_roi_solar_with_pumped_hydro(project_term=15, water_area=150000, ins_cost_solar_farm_per_sys = 0.0025,
                          KwH_per_sqm = 0.3, maintance_cost = 0.03, leasing_fees_f = 0.05,
                          interest_rate = 0.065, ratio_covered_area_to_solar = 1.5, cost_per_sqm = 247.5,
                          LGC_value = 25, financing_amount = 0.1):

    roi_no_storage = calculate_roi_solar_no_storage(project_term=project_term, water_area=water_area)
    ##########################################
    system_life_year = 50
    total_upfront_pumped_hydro = 800 + 70 + 247
    discount_rate = 0.05 + 0.02
    ebitda = ((34 + 8 + 13 + 55 + 800 * 0.8 + 70 * 0.85 + 1.15) * (1 + discount_rate) / system_life_year) \
             + (0.4 * 0.98 / project_term * 365)

    equity_cost = -1 * (total_upfront_pumped_hydro)
    roi_for_pumped_hydro = ebitda / equity_cost
    #############################################
    roi = roi_no_storage +  roi_for_pumped_hydro
    #print(roi_for_pumped_hydro)
    return roi


new_roi_1 = new_calculate_roi_solar_with_battery()
new_roi_2 = new_calculate_roi_solar_with_pumped_hydro()

old_roi_1 = calculate_roi_solar_with_battery()
old_roi_2 = calculate_roi_solar_with_pumped_hydro()

print("Update solar with battery", new_roi_1)
print("Update solar with PHES", new_roi_2)
print("Solar with battery", old_roi_1)
print("Solar with PHES", old_roi_2)













