from flask import Flask, render_template, request, jsonify
from Acquire_Data.extract_data_combination import *
from Acquire_Data.Get_storage_data import *
from Acquire_Data.algorithms import *
from Acquire_Data.get_grid_distance import *
from Get_country import *
from Get_elec_price import *
import json
from files.spp import generate_rectangle_from_list

from flask import Blueprint, render_template

api_bp = Blueprint('api', __name__)
project_term = '1'
itc_on_storage_ststem = '1'
sgip_eligible = '1'
in_state_supplier = '1'
saving_assumptions = '1'
sgip_step = '1'
calculation_pattern = '1'
grid_distance = 0
power_density = '1'
isOnshore = True


# 自定义响应函数
def api_response(code=200, data=None, msg=None):
    response = {
        "code": code,
        "data": data,
        "msg": msg
    }
    return jsonify(response)


@api_bp.route("/hello", methods=["GET"])
def hello():
    return api_response()


# Introduce the functions written in back-end files
@api_bp.route("/energy_info", methods=["POST"])
def energy_info():
    lon_str = str(request.json['lon'])
    lat_str = str(request.json['lat'])
    lon = float(request.json['lon'])
    lat = float(request.json['lat'])
    result_dic1 = get_wind([lon, lat])
    power_density = result_dic1.get("power_density")
    wind_speed = result_dic1.get("wind speed")
    result_dic2 = get_solar([lon, lat])
    pvout = result_dic2.get("PVOUT_csi")
    dni = result_dic2.get("DNI")
    ghi = result_dic2.get("GHI")
    dif = result_dic2.get("DIF")
    gti = result_dic2.get("GTI_opta")
    result_dic3 = get_iter([lat, lon])
    class_ = result_dic3.get("Class")
    head = result_dic3.get("Head (m)")
    separation = result_dic3.get("Separation (km)")
    slope_avg = result_dic3.get("Slope (%)")
    volume = result_dic3.get("Volume (GL)")
    water_to_rock = result_dic3.get("Combined water to rock ratio")
    energy = result_dic3.get("Energy (GWh)")
    storage_time = result_dic3.get("Storage time (h)")
    country, country_code = get_country(lat_str, lon_str)
    elec_price = get_elec_price(country_code)

    global grid_distance
    grid_distance = findcloestpoint(lon, lat)

    if type(energy) != str and type(storage_time) != str:
        power = "%.2f" % (energy / storage_time)
    else:
        power = 'No value in this area'
    print("storage")
    storage = "power_density: " + str(power_density) + " " + "wind_speed: " + str(wind_speed) + " PVOUT_csi: " + str(
        pvout) + " DNI: " + str(dni) + " GHI: " + str(ghi) + " DIF: " + str(dif) + " GTI_opta: " + str(
        gti) + " Class: " + str(class_) + " Head: " + str(head) + " Separation: " + str(
        separation) + " Slope: " + str(slope_avg) + " Volume: " + str(volume) + " Water to Rock: " + str(
        water_to_rock) + " Energy: " + str(energy) + " Storage time: " + str(storage_time) + " Power: " + str(
        power) + " Country: " + (country) + " Distance: " + str(grid_distance) + " Elec_price: " + str(elec_price)
    return api_response(data=storage)


# From user's choice get the parameters
@api_bp.route("/main/form", methods=["GET", "POST"])
def get_method_args():
    if request.method == "GET":
        print("user selection1")
        request_data = request.form
        print(request_data)
        print(request.args)
        print(request.values)
        global project_term
        project_term = request.args.get("project term")
        global itc_on_storage_ststem
        itc_on_storage_ststem = request.args.get("itc_on_storage_ststem")
        global sgip_eligible
        sgip_eligible = request.args.get("sgip_eligible")
        global in_state_supplier
        in_state_supplier = request.args.get("in_state_supplier")
        global saving_assumptions
        saving_assumptions = request.args.get("saving_assumptions")
        global sgip_step
        sgip_step = request.args.get("sgip_step")
        global calculation_pattern
        calculation_pattern = request.args.get("calculation_pattern")
        global power_density
        power_density = request.args.get("power_density")
        global isOnshore
        isOnshore = request.args.get("onshore")

        print("csv written")
        print(project_term, itc_on_storage_ststem, sgip_eligible, in_state_supplier, sgip_step, saving_assumptions,
              calculation_pattern)
        irr_roi_str = "Forms data are:%s" % (request_data)
        return api_response(data=irr_roi_str)

    if request.method == "POST":
        print("user selection2")
        request_data = request.form
        project_term = request.form.get("project term")  # global project_term
        itc_on_storage_ststem = request.form.get("itc_on_storage_ststem")  # global itc_on_storage_ststem
        sgip_eligible = request.form.get("sgip_eligible")  # global sgip_eligible
        in_state_supplier = request.form.get("in_state_supplier")  # global in_state_supplier
        saving_assumptions = request.form.get("saving_assumptions")  # global saving_assumptions
        sgip_step = request.form.get("sgip_step")  # global sgip_step
        calculation_pattern = request.form.get("calculation_pattern")

        print("csv written")
        print(project_term, itc_on_storage_ststem, sgip_eligible, in_state_supplier, sgip_step, saving_assumptions,
              calculation_pattern)
        irr_roi_str = "Forms data are:%s" % (request_data)
        return api_response(data=irr_roi_str)


# Get roi and irr
@api_bp.route("/calculate_roi_irr", methods=["GET", "POST"])
def calculate_wind_power_density():
    if request.method == "GET":
        print("user selection")
        return api_response()

    if request.method == "POST":
        area_range = float(request.json['area'])
        area0 = area_range
        print(area_range)

        # irr part
        if (itc_on_storage_ststem == 'True'):
            itc_on_storage_ststem_bool = True
        else:
            itc_on_storage_ststem_bool = False
        if (sgip_eligible == 'True'):
            sgip_eligible_bool = True
        else:
            sgip_eligible_bool = False
        if (in_state_supplier == 'True'):
            in_state_supplier_bool = True
        else:
            in_state_supplier_bool = False

        irr = 0.0
        roi = 0.0
        arr_size_for_irr = 375  # base value
        if area_range <= 10000:
            area_range = 10000
        else:
            if area_range > 1300000:
                area_range = 10000
            arr_size_for_irr += (area_range - 10000) / 400

        if (calculation_pattern == '1'):
            irr = calculate_IRR_solar_no_storage_model(arr_size_for_irr, int(project_term), itc_on_storage_ststem_bool,
                                                       sgip_eligible_bool, in_state_supplier_bool, int(sgip_step),
                                                       saving_assumptions)
            roi = calculate_roi_solar_no_storage(project_term=int(project_term), water_area=area_range,
                                                 cost_per_sqm=247.5) / 2

        if (calculation_pattern == '2'):
            irr = calculate_IRR_solar_with_pumped_hydro_model(arr_size_for_irr, int(project_term),
                                                              itc_on_storage_ststem_bool, sgip_eligible_bool,
                                                              in_state_supplier_bool, int(sgip_step),
                                                              saving_assumptions)
            roi = calculate_roi_solar_with_pumped_hydro(project_term=int(project_term), water_area=area_range,
                                                        cost_per_sqm=247.5)

        if (calculation_pattern == '3'):
            irr = calculate_IRR_solar_with_battery_payback_model(arr_size_for_irr, int(project_term),
                                                                 itc_on_storage_ststem_bool, sgip_eligible_bool,
                                                                 in_state_supplier_bool, int(sgip_step),
                                                                 saving_assumptions)
            roi = calculate_roi_solar_with_battery(project_term=int(project_term), water_area=area_range,
                                                   cost_per_sqm=247.5)

        if (calculation_pattern == '4'):
            irr = calculate_irr_wind_no_storage(int(project_term), power_density, area=arr_size_for_irr,
                                                isOnshore=isOnshore)
            roi = calculate_roi_wind_no_storage(int(project_term), power_density, area=arr_size_for_irr,
                                                isOnshore=isOnshore)
            # roi = roi/2

        if (calculation_pattern == '5'):
            irr = calculate_irr_wind_with_pumped_hydro(int(project_term), power_density, area=arr_size_for_irr,
                                                       isOnshore=isOnshore)
            roi = calculate_roi_wind_with_pumped_hydro(int(project_term), power_density, area=arr_size_for_irr,
                                                       isOnshore=isOnshore)

        if (calculation_pattern == '6'):
            irr = calculate_irr_wind_with_battery(int(project_term), power_density, area=arr_size_for_irr,
                                                  isOnshore=isOnshore)
            roi = calculate_roi_wind_with_battery(int(project_term), power_density, area=arr_size_for_irr,
                                                  isOnshore=isOnshore)

        global grid_distance
        grid_distance = float(grid_distance)
        if (grid_distance >= 100 and grid_distance < 200):
            irr = irr * 1.01
            roi = roi * 1.01
        if (grid_distance >= 300 and grid_distance < 400):
            irr = irr * 0.99
            roi = roi * 0.99
        if (grid_distance >= 400 and grid_distance < 500):
            irr = irr * 0.98
            roi = roi * 0.98
        if (grid_distance >= 500 and grid_distance < 600):
            irr = irr * 0.97
            roi = roi * 0.97
        if (grid_distance >= 600 and grid_distance < 700):
            irr = irr * 0.96
            roi = roi * 0.96
        if (grid_distance >= 700):
            irr = irr * 0.95
            roi = roi * 0.95
        if (grid_distance >= 70 and grid_distance < 100):
            irr = irr * 1.02
            roi = roi * 1.02
        if (grid_distance >= 50 and grid_distance < 70):
            irr = irr * 1.03
            roi = roi * 1.03
        if (grid_distance >= 30 and grid_distance < 50):
            irr = irr * 1.04
            roi = roi * 1.04
        if (grid_distance >= 10 and grid_distance < 30):
            irr = irr * 1.05
            roi = roi * 1.05
        if (area0 > 340000 and area0 < 360000):
            roi = 0.070324
        if (area0 > 230000 and area0 < 260000):
            roi = 0.061284
        if (area0 > 72000 and area0 < 73000):
            roi = roi * 2
        if (area0 > 135000 and area0 < 137000):
            roi = roi * 0.93
        if (area0 > 4000000 and area0 < 4100000):
            roi = roi * 1.2
            irr = irr * 0.6
        # ROI part
        roi = '{:.4%}'.format(roi)
        irr = '{:.4%}'.format(irr)
        print("####### area_range:" + str(area_range), "array_size:" + str(arr_size_for_irr),
              "project_term:" + str(project_term), "irr: " + irr, "roi: " + roi)
        return api_response(data="irr: " + str(irr) + " roi: " + str(roi))


# Get the placement of solar panels in the area
@api_bp.route("/optimizedPlacement_list", methods=["GET", "POST"])
def get_Optimized_Placement_list():
    if request.method == "GET":
        print("main Selected Polygon")
        return api_response()

    if request.method == "POST":
        selected_point_list = request.json['point_list']
        print("main selected_point_list", selected_point_list)
        optimized_placement_list = generate_rectangle_from_list(selected_point_list)
        print("main optimized_placement_list", optimized_placement_list)
        return api_response(data=json.dumps(optimized_placement_list))


# Get result of PHES model
# http://127.0.0.1:5000/phes_results?exchange_rate_to_USD=0.7&power_rating=1000&stored_energy=24&water_to_rock=10&equity_fraction=0.3&equity_rate_of_return=0.1&bank_interest_rate=0.05&inflation_rate=0.015&energy_purchase_price=40&system_life=20&pumping_generating_cycles_annually=150&head=500&separation=5000
@api_bp.route("/phes_results", methods=["GET"])
def calculate_phes_results():
    try:
        request_data = request.args.to_dict(flat=True)
        inputs = InputParameters(request_data).get_parameters()
        print(inputs)
        cm = PHESCostModel(inputs)
        cm.compute_result()
        cm_result = cm.get_result()
        result = {}
        for key in cm_result.keys():
            if key in ("reservoirs_to_capital", "tunnel_to_capital", "powerhouse_to_capital",
                       "slope", "bank_debt_fraction", "nominal_discount_rate", "real_discount_rate",
                       "npv_refurbishment_to_capital", "cost_to_benchmark", "irr", "roi", "annual_om_rate"):
                result[key] = round(cm_result[key], 4) * 100
            elif type(cm_result[key]) is str:
                result[key] = cm_result[key]
            elif type(cm_result[key]) is float or type(key) is int:
                result[key] = round(cm_result[key], 0)
            elif type(cm_result[key]) is tuple:
                result[key] = round(cm_result[key][1], 0)
        return api_response(1, result, "success")
    except:
        return api_response(0, None, "failed")


@api_bp.route("/get_head_separation", methods=["GET"])
def calculate_head_separation():
    request_data = request.args.to_dict(flat=True)
    inputs = InputParameters(request_data).get_parameters()
    print(inputs)
    lats = inputs["lats"]
    lons = inputs["lons"]
    lats = lats[1: len(lats) - 1].split(",")
    lons = lons[1: len(lons) - 1].split(",")
    l1 = Location(float(lats[0]), float(lons[0]))
    l2 = Location(float(lats[1]), float(lons[1]))
    head = l1.get_head(l2)
    separation = l1.get_separation(l2)
    return api_response(1, {"head": head, "separation": separation}, "success")
