
"""
Created on Fri Mar 11 12:55:39 2023

@author: Xie
"""

"""
storage energy right project 
 back-end code for calculation 
 token: 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
"""

import math


def energy_storage_data_calculation(potential_energy, pumping_efficiency,
                                    generation_efficiency, usable_fraction_of_water_volume,
                                    dam_cost, power_benchmark_cost, energy_benchmark_cost,
                                    exchange_rate_to_USD, head, separation, power_rating,
                                    stored_energy, equity_fraction, equity_rate_of_return,
                                    bank_interest_rate, inflation_rate,
                                    system_life,
                                    pumping_generating_cycles_annually, water_to_rock,
                                    average_purchased_price_of_energy_for_storage):
    # 14
    available_reservoir_water_volume = stored_energy * 3600.0 / (9.8 * generation_efficiency * head)

    # 13
    total_reservoir_water_volume = available_reservoir_water_volume / usable_fraction_of_water_volume

    # 15
    rock_volume = total_reservoir_water_volume / water_to_rock

    # 7
    reservoir_cost = dam_cost / rock_volume

    # 8
    tunnel_cost = ((66000 * power_rating + 17000000) + separation * (1280 * power_rating +
                                                                     210000) * head ** (-0.54)) / 1000000
    # 9
    powerhouse_cost = 63500000 * head ** (-0.5) * power_rating ** (0.75)


# 8 
# tunnel cost calculation
def tunnel_cost (pr,sp,head):
     
    tunnelCost = ((66000*pr+17000000)+sp*(1280*pr+210000)*(head**(-0.54)))/10000
    
    return tunnelCost

# 9
# powerhouse cost calculation
def powerhouse_cost (head,pr):
    powerhouseCost=0 # modify later
    return powerhouseCost

# 13,14,15
# rock volume calculation
# available reservoir water volume calculation firstly
# then calculate total reservoir water volume
# finally get rock volume 
def rock_volume (trwv,wrr):
    rockVolume = trwv / wrr
    return rockVolume
    
# 13
def total_reservoir_water_volume(arwv, ufwv):
    trwv = arwv/ufwv
    return trwv

# 14
def available_reservoir_water_volume(se,ge,head):
    arwv  = se*3600/(9.0*ge*head)
    return arwv
    
# 7
# reservoirs cost calculation
def reservoirs_cost (damCost,rockVolume):
    reservoirsCost = damCost / rockVolume
    return reservoirsCost

# 1
# power capital cost calculation
def power_capital_cost (tunnelCost,powerhouseCost,pr):
    powerCapitalCost = (tunnelCost+powerhouseCost)*10 # modify later
    return powerCapitalCost

# 2
# energy capital cost calculation
def energy_capital_cost (reserveCost,se):
    energyCapitalCost = reserveCost/se
    return energyCapitalCost

# 3
# capital cost calculation
def capital_cost (tunnelCost,powerhouseCost,reserveCost):
    capitalCost = tunnelCost+powerhouseCost+reserveCost
    return capitalCost
    
# 4
def cost_class (ebc):
    if ebc<1:
        return "A"
    elif ebc >=1 and ebc<1.25:
        return "B"
    elif ebc >=1.25 and ebc<1.5:
        return "C"
    elif ebc >=1.5 and ebc<1.75:
        return "D"
    elif ebc >=1.75 and ebc<2:
        return "E"
    # dont get less than E. need to ask 

# 5
# capital cost per KW calculation
def capital_cost_pKW(capitalCost,pr):
    ccpkw = capitalCost*1000/pr
    return ccpkw
    
# 6 
# capital cost per KWh calculation
def capital_cost_pKWh(capitalCost,se):
    ccpkwh = capitalCost*1000/se
    return ccpkwh

# 10
def reservoirs_to_capital(reservoirsCost,capitalCost):
    rtc = reservoirsCost/capitalCost
    return rtc
    
# 11 
def tunnel_to_capital(tunnelCost,capitalCost):
    ttc = tunnelCost/capitalCost
    return ttc
    
# 12
def powerhouse_to_capital(powerhouseCost,capitalCost):
    ptc = powerhouseCost/capitalCost
    return ptc


# 16
def slope(head,sp):
    slope = head/sp
    return slope

# 17 
def operation_hours(se,pr):
    oh = se*1000/pr
    return oh

# 18
def upper_reservoir_area(trwv):
    ura = trwv*1000 # fomula is not correct
    return ura

# 19
def diameter_circular_reservoir(ura):
    dcr = (ura*10000*4/3.142)**0.5/1000
    return dcr

# 20
def bank_debt_fraction(ef):
    bdf = 1-ef
    return bdf
    
# 21
def nominal_discount_rate(ef,er,bdf,bir):
    ndr = ef*er+bdf*bir
    return ndr    

# 22
def real_discount_rate(ndr, ir):
    rdr = ndr-ir
    return rdr

# 23
def npv_refurbishment(pr,rdr):
    npvr = 0 # the fomula is incorrect
    return npvr

# 24
def npv_refurbishment_to_capital(npvr,capitalCost):
    npvrtc = npvr/capitalCost
    return npvrtc

# 25
def annual_energy_purchased():
    aep = 0 # fomula is not correct
    return aep

# 26
def annual_energy_sold():
    aes = 0 # incorrect fomula
    return aes
    
# 27

    
    















