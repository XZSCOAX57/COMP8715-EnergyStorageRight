# Author: Jingran
# The cost model of PHES module based on
# https://docs.google.com/spreadsheets/d/11bFXnNKr1owT3xGqLR3pNUcy8UGSeM15/edit#gid=1789734258

import logging
import numpy as np
import numpy_financial as npf
import os
import sys

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PHES_Main_Model.DefualtParameters import *


class InputParameters:
    def __init__(self, params):
        self.initial_parameter = params

    def get_parameters(self):
        return self.initial_parameter

    def print_parameters(self):
        print(self.initial_parameter)


class PHESCostModel:

    def __init__(self, params):
        self.__potential_energy = POTENTIAL_ENERGY
        self.__pumping_efficiency = PUMPING_EFFICIENCY
        self.__generation_efficiency = GENERATION_EFFICIENCY
        self.__usable_fraction_water_volume = USABLE_FRACTION_WATER_VOLUME
        self.__dam_cost = DAM_COST
        self.__power_benchmark_cost = POWER_BENCHMARK_COST
        self.__energy_benchmark_cost = ENERGY_BENCHMARK_COST

        self.exchange_rate_to_USD = float(params["exchange_rate_to_USD"])
        self.head = float(params["head"])
        self.separation = float(params["separation"])
        self.power_rating = float(params["power_rating"])
        self.stored_energy = float(params["stored_energy"])
        self.equity_fraction = float(params["equity_fraction"])
        self.equity_rate_of_return = float(params["equity_rate_of_return"])
        self.bank_interest_rate = float(params["bank_interest_rate"])
        self.inflation_rate = float(params["inflation_rate"])
        self.energy_purchase_price = float(params["energy_purchase_price"])
        self.system_life = float(params["system_life"])
        self.pumping_generating_cycles_annually = float(params["pumping_generating_cycles_annually"])
        self.water_to_rock = float(params["water_to_rock"])
        self.__pmt = 0.0  # in USD
        self.__initial_outlay = 0.0  # in USD

        # financial fields -> (USD,  AUD)
        self.__result = {
            "power_capital_cost": (0.0, 0.0),
            "energy_capital_cost": (0.0, 0.0),
            "capital_cost": (0.0, 0.0),
            "cost_class": "",
            "capital_cost_pkw": (0.0, 0.0),
            "capital_cost_pkwh": (0.0, 0.0),
            "reservoir_cost": (0.0, 0.0),
            "tunnel_cost": (0.0, 0.0),
            "powerhouse_cost": (0.0, 0.0),
            "reservoirs_to_capital": 0.0,  # %
            "tunnel_to_capital": 0.0,  # %
            "powerhouse_to_capital": 0.0,  # %
            "total_reservoir_water_volume": 0.0,
            "available_reservoir_water_volume": 0.0,
            "rock_volume": 0.0,
            "slope": 0.0,
            "operation_hours": 0.0,
            "upper_reservoir_area": 0.0,
            "diameter_circular_reservoir": 0.0,
            "bank_debt_fraction": 0.0,
            "nominal_discount_rate": 0.0,
            "real_discount_rate": 0.0,
            "npv_refurbishment": 0.0,
            "npv_refurbishment_to_capital": 0.0,
            "annual_energy_purchased": 0.0,
            "annual_energy_sold": 0.0,
            "cost_lost_energy_mwh": (0.0, 0.0),
            "capital_cost_mwh": (0.0, 0.0),
            "om_cost_mwh": (0.0, 0.0),
            "levelised_cost_of_storage_mwh": (0.0, 0.0),
            "total_cost": (0.0, 0.0),
            "cost_to_benchmark": 0.0,
            "irr": 0.0,
            "roi": 0.0,
            "annual_om_rate": 0.0,
            "annual_fixed_om_pmw": (0.0, 0.0),
            "annual_variable_om_pmw": (0.0, 0.0)
        }

    def get_result(self):
        return self.__result

    def __get_tunnel_cost(self):
        usd = ((66000.0 * self.power_rating + 17000000.0) + self.separation *
               (1280.0 * self.power_rating + 210000.0) * self.head ** (-0.54)) / 1000000
        aud = usd / self.exchange_rate_to_USD
        self.__result["tunnel_cost"] = (usd, aud)
        return self.__result["tunnel_cost"]

    def __get_powerhouse_cost(self):
        usd = 63.5 * self.head ** (-0.5) * self.power_rating ** 0.75
        aud = usd / self.exchange_rate_to_USD
        self.__result["powerhouse_cost"] = (usd, aud)
        return self.__result["powerhouse_cost"]

    def __get_power_capital_cost(self):
        usd = (self.__result["tunnel_cost"][0] + self.__result["powerhouse_cost"][0]) \
              * 1000 / self.power_rating
        aud = usd / self.exchange_rate_to_USD
        self.__result["power_capital_cost"] = (usd, aud)
        return self.__result["power_capital_cost"]

    def __get_available_reservoir_water_volume(self):
        self.__result["available_reservoir_water_volume"] = self.stored_energy * 3600 / \
                                                            (9.8 * self.__generation_efficiency * self.head)
        return self.__result["available_reservoir_water_volume"]

    def __get_total_reservoir_water_volume(self):
        self.__result["total_reservoir_water_volume"] = self.__result["available_reservoir_water_volume"] \
                                                        / self.__usable_fraction_water_volume
        return self.__result["total_reservoir_water_volume"]

    def __get_rock_volume(self):
        self.__result["rock_volume"] = self.__result["total_reservoir_water_volume"] / self.water_to_rock
        return self.__result["rock_volume"]

    def __get_reservoir_cost(self):
        usd = self.__dam_cost / self.__result["rock_volume"]
        aud = usd / self.exchange_rate_to_USD
        self.__result["reservoir_cost"] = (usd, aud)
        return self.__result["reservoir_cost"]

    def __get_capital_cost(self):
        usd = self.__result["reservoir_cost"][0] + self.__result["tunnel_cost"][0] + \
              self.__result["powerhouse_cost"][0]
        aud = usd / self.exchange_rate_to_USD
        self.__result["capital_cost"] = (usd, aud)
        return self.__result["capital_cost"]

    def __get_reservoirs_to_capital(self):
        self.__result["reservoirs_to_capital"] = self.__result["reservoir_cost"][0] / self.__result["capital_cost"][
            0] * 100
        return self.__result["reservoirs_to_capital"]

    def __get_tunnel_to_capital(self):
        self.__result["tunnel_to_capital"] = self.__result["tunnel_cost"][0] / self.__result["capital_cost"][
            0] * 100
        return self.__result["tunnel_to_capital"]

    def __get_powerhouse_to_capital(self):
        self.__result["powerhouse_to_capital"] = self.__result["powerhouse_cost"][0] / \
                                                 self.__result["capital_cost"][0] * 100
        return self.__result["powerhouse_to_capital"]

    def __get_energy_capital_cost(self):
        usd = self.__result["reservoir_cost"][0] / self.stored_energy
        aud = usd / self.exchange_rate_to_USD
        self.__result["energy_capital_cost"] = (usd, aud)
        return self.__result["energy_capital_cost"]

    def __get_capital_cost_pkw(self):
        usd = self.__result["capital_cost"][0] * 1000 / self.power_rating
        aud = usd / self.exchange_rate_to_USD
        self.__result["capital_cost_pkw"] = (usd, aud)
        return self.__result["capital_cost_pkw"]

    def __get_capital_cost_pkwh(self):
        usd = self.__result["capital_cost"][0] * 1000 / self.stored_energy
        aud = usd / self.exchange_rate_to_USD
        self.__result["capital_cost_pkwh"] = (usd, aud)
        return self.__result["capital_cost_pkwh"]

    def __get_scope(self):
        self.__result["slope"] = self.head / self.separation
        return self.__result["slope"]

    def __get_operation_hours(self):
        self.__result["operation_hours"] = self.stored_energy * 1000 / self.power_rating
        return self.__result["operation_hours"]

    def __get_upper_reservoir_area(self):
        self.__result["upper_reservoir_area"] = 100 * self.__result["total_reservoir_water_volume"] / 15
        return self.__result["upper_reservoir_area"]

    def __get_diameter_circular_reservoir(self):
        self.__result["diameter_circular_reservoir"] = (self.__result["upper_reservoir_area"]
                                                        * 10000 * 4 / 3.142) ** 0.5 / 1000
        return self.__result["diameter_circular_reservoir"]

    def __get_bank_debt_fraction(self):
        self.__result["bank_debt_fraction"] = 1 - self.equity_fraction
        return self.__result["bank_debt_fraction"]

    def __get_nominal_discount_rate(self):
        self.__result["nominal_discount_rate"] = self.equity_fraction * self.equity_rate_of_return + \
                                                 self.__result["bank_debt_fraction"] * self.bank_interest_rate
        return self.__result["nominal_discount_rate"]

    def __get_real_discount_rate(self):
        self.__result["real_discount_rate"] = self.__result["nominal_discount_rate"] - self.inflation_rate
        return self.__result["real_discount_rate"]

    def __get_npv_refurbishment(self):
        usd = 112000 * self.power_rating * (np.exp(-1 * self.__result["real_discount_rate"] * 20)
                                            + np.exp(-1 * self.__result["real_discount_rate"] * 40)) / 1000000
        aud = usd / self.exchange_rate_to_USD
        self.__result["npv_refurbishment"] = (usd, aud)
        return self.__result["npv_refurbishment"]

    def __get_npv_refurbishment_to_capital(self):
        self.__result["npv_refurbishment_to_capital"] = self.__result["npv_refurbishment"][0] \
                                                        / self.__result["capital_cost"][0]
        return self.__result["npv_refurbishment_to_capital"]

    def __get_annual_energy_purchased(self):
        self.__result["annual_energy_purchased"] = (self.stored_energy / self.__generation_efficiency) * \
                                                   self.pumping_generating_cycles_annually / 1000
        return self.__result["annual_energy_purchased"]

    def __get_annual_energy_sold(self):
        self.__result["annual_energy_sold"] = (self.stored_energy * self.__generation_efficiency) * \
                                              self.pumping_generating_cycles_annually / 1000
        return self.__result["annual_energy_sold"]

    def __get_cost_lost_energy_mwh(self):
        usd = (self.__result["annual_energy_purchased"] - self.__result["annual_energy_sold"]) \
              * self.energy_purchase_price / self.__result["annual_energy_sold"]
        aud = usd / self.exchange_rate_to_USD
        self.__result["cost_lost_energy_mwh"] = (usd, aud)
        return self.__result["cost_lost_energy_mwh"]

    def __get_capital_cost_mwh(self):
        usd = ((self.__result["capital_cost"][0] + self.__result["npv_refurbishment"][0])
               * self.__result["real_discount_rate"]) / (1 - np.exp(-1 * self.__result["real_discount_rate"] *
                                                                    self.system_life)) / self.__result[
                  "annual_energy_sold"]
        aud = usd / self.exchange_rate_to_USD
        self.__result["capital_cost_mwh"] = (usd, aud)
        return self.__result["capital_cost_mwh"]

    def __get_annual_fixed_om_pmw(self):
        usd = 8210 * self.power_rating / 1000000
        aud = usd / self.exchange_rate_to_USD
        self.__result["annual_fixed_om_pmw"] = (usd, aud)
        return self.__result["annual_fixed_om_pmw"]

    def __get_annual_variable_om_pmw(self):
        usd = 0.3 * 2 * self.pumping_generating_cycles_annually * self.stored_energy / 1000
        aud = usd / self.exchange_rate_to_USD
        self.__result["annual_variable_om_pmw"] = (usd, aud)
        return self.__result["annual_variable_om_pmw"]

    def __get_annual_fixed_om_rate(self):
        self.__result["annual_om_rate"] = (self.__result["annual_fixed_om_pmw"][0] +
                                           self.__result["annual_variable_om_pmw"][0]) / \
                                          self.__result["capital_cost"][0]
        return self.__result["annual_om_rate"]

    def __get_om_cost_mwh(self):
        usd = self.__result["annual_om_rate"] * self.__result["capital_cost"][0] / self.__result[
            "annual_energy_sold"]
        aud = usd / self.exchange_rate_to_USD
        self.__result["om_cost_mwh"] = (usd, aud)
        return self.__result["om_cost_mwh"]

    def __get_levelised_cost_of_storage_mwh(self):
        usd = self.__result["cost_lost_energy_mwh"][0] + self.__result["capital_cost_mwh"][0] \
              + self.__result["om_cost_mwh"][0]
        aud = usd / self.exchange_rate_to_USD
        self.__result["levelised_cost_of_storage_mwh"] = (usd, aud)
        return self.__result["levelised_cost_of_storage_mwh"]

    def __get_total_cost(self):
        usd = self.__power_benchmark_cost * self.stored_energy + self.__energy_benchmark_cost / 1000 * self.power_rating
        aud = usd / self.exchange_rate_to_USD
        self.__result["total_cost"] = (usd, aud)
        return self.__result["total_cost"]

    def __get_cost_to_benchmark(self):
        self.__result["cost_to_benchmark"] = self.__result["capital_cost"][0] / self.__result["total_cost"][0]
        return self.__result["cost_to_benchmark"]

    def __get_cost_class(self):
        if self.__result["cost_to_benchmark"] < 1:
            self.__result["cost_class"] = "A"
        elif self.__result["cost_to_benchmark"] < 1.25:
            self.__result["cost_class"] = "B"
        elif self.__result["cost_to_benchmark"] < 1.5:
            self.__result["cost_class"] = "C"
        elif self.__result["cost_to_benchmark"] < 1.75:
            self.__result["cost_class"] = "D"
        elif self.__result["cost_to_benchmark"] < 2:
            self.__result["cost_class"] = "E"
        else:
            self.__result["cost_class"] = "Less than E"

    def compute_result(self):
        self.__get_tunnel_cost()
        self.__get_powerhouse_cost()
        self.__get_power_capital_cost()
        self.__get_available_reservoir_water_volume()
        self.__get_total_reservoir_water_volume()
        self.__get_rock_volume()
        self.__get_reservoir_cost()
        self.__get_capital_cost()
        self.__get_reservoirs_to_capital()
        self.__get_tunnel_to_capital()
        self.__get_powerhouse_to_capital()
        self.__get_energy_capital_cost()
        self.__get_capital_cost_pkw()
        self.__get_capital_cost_pkwh()
        self.__get_scope()
        self.__get_operation_hours()
        self.__get_upper_reservoir_area()
        self.__get_diameter_circular_reservoir()
        self.__get_bank_debt_fraction()
        self.__get_nominal_discount_rate()
        self.__get_real_discount_rate()
        self.__get_npv_refurbishment()
        self.__get_npv_refurbishment_to_capital()
        self.__get_annual_energy_purchased()
        self.__get_annual_energy_sold()
        self.__get_cost_lost_energy_mwh()
        self.__get_capital_cost_mwh()
        self.__get_annual_fixed_om_pmw()
        self.__get_annual_variable_om_pmw()
        self.__get_annual_fixed_om_rate()
        self.__get_om_cost_mwh()
        self.__get_levelised_cost_of_storage_mwh()
        self.__get_total_cost()
        self.__get_cost_to_benchmark()
        self.__get_cost_class()
        self.__get_pmt()
        self.__get_inital_outlay()
        self.__get_irr()
        self.__get_roi()

    def __get_pmt(self):
        self.__pmt = self.__result["annual_energy_sold"] * 1000000 * self.energy_purchase_price - self.__result[
            "capital_cost"][0] * self.__result["annual_om_rate"] * 1000000
        return self.__pmt

    def __get_inital_outlay(self):
        self.__initial_outlay = -1 * (
                self.__result["capital_cost"][0] + self.__result["npv_refurbishment"][0]) * 1000000
        return self.__initial_outlay

    def __get_irr(self):
        cf = [self.__pmt] * int(self.system_life)
        cf.insert(0, self.__initial_outlay)
        cf_array = np.array(cf)
        self.__result["irr"] = npf.irr(cf_array)
        return self.__result["irr"]

    def __get_roi(self):
        cf = [self.__pmt] * int(self.system_life)
        cf.insert(0, self.__initial_outlay)
        cf_array = np.array(cf)
        npv = npf.npv(self.__result["real_discount_rate"], cf_array)
        self.__result["roi"] = npv / (self.__result["capital_cost"][0] * 1000000)
        return self.__result["roi"]
    
if __name__ == '__main__':
    params = {"exchange_rate_to_USD": 0.7,
              "power_rating": 1000,
              "stored_energy": 24,
              "water_to_rock": 10,
              "equity_fraction": 0.3,
              "equity_rate_of_return": 0.1,
              "bank_interest_rate": 0.05,
              "inflation_rate": 0.015,
              "energy_purchase_price": 40,
              "system_life": 20,
              "pumping_generating_cycles_annually": 150,
              "head": 500,
              "separation": 5000
              }
    inputs = InputParameters(params).get_parameters()
    cm = PHESCostModel(inputs)

    cm.compute_result()
    print(cm.get_result())
